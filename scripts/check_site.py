#!/usr/bin/env python3
"""Check tracked static links and course class-page reachability."""

from __future__ import annotations

import posixpath
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        for name in ("href", "src"):
            value = attributes.get(name)
            if value is not None:
                self.links.append(value)


ROOT = Path(
    subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
)
TRACKED = {
    path
    for path in subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    ).stdout.decode().split("\0")
    if path
}
HTML_FILES = {path for path in TRACKED if path.endswith(".html")}


def resolve_local(source: str, raw_link: str) -> str | None:
    """Resolve a local URL to a tracked repository path, if it has one."""
    url = urlsplit(raw_link)
    if url.scheme or url.netloc:
        return None

    link_path = unquote(url.path)
    if not link_path:
        return source

    if link_path.startswith("/"):
        target = link_path.lstrip("/")
    else:
        target = posixpath.join(posixpath.dirname(source), link_path)
    target = posixpath.normpath(target)
    if target == ".." or target.startswith("../"):
        return target
    if target == ".":
        target = ""

    if target in TRACKED:
        return target
    index_target = posixpath.join(target, "index.html")
    if index_target in TRACKED:
        return index_target
    return target


def parse_links(path: str) -> list[str]:
    parser = LinkParser()
    parser.feed((ROOT / path).read_text(encoding="utf-8"))
    return parser.links


def main() -> int:
    broken: list[tuple[str, str, str]] = []
    graph: dict[str, set[str]] = {path: set() for path in HTML_FILES}

    for source in sorted(HTML_FILES):
        for raw_link in parse_links(source):
            target = resolve_local(source, raw_link)
            if target is None:
                continue
            if target not in TRACKED:
                broken.append((source, raw_link, target))
            elif target in HTML_FILES:
                graph[source].add(target)

    class_pages_by_course: dict[str, set[str]] = {}
    for path in HTML_FILES:
        parts = path.split("/")
        if (
            len(parts) == 4
            and parts[1] == "classes"
            and parts[2].startswith("class-")
            and parts[3] == "index.html"
        ):
            class_pages_by_course.setdefault(parts[0], set()).add(path)

    unreachable: list[tuple[str, str]] = []
    for course, class_pages in sorted(class_pages_by_course.items()):
        homepage = f"{course}/index.html"
        if homepage not in HTML_FILES:
            unreachable.extend((homepage, page) for page in sorted(class_pages))
            continue

        reachable: set[str] = set()
        pending = [homepage]
        while pending:
            page = pending.pop()
            if page in reachable:
                continue
            reachable.add(page)
            pending.extend(graph[page] - reachable)

        unreachable.extend(
            (homepage, page) for page in sorted(class_pages - reachable)
        )

    if broken:
        print("Broken local links:", file=sys.stderr)
        for source, raw_link, target in broken:
            print(f"  {source}: {raw_link!r} -> {target}", file=sys.stderr)
    if unreachable:
        print("Class pages unreachable from their course homepage:", file=sys.stderr)
        for homepage, page in unreachable:
            print(f"  {page} (from {homepage})", file=sys.stderr)
    if broken or unreachable:
        return 1

    print(
        f"Checked {len(HTML_FILES)} HTML files: all local links resolve and "
        f"all {sum(map(len, class_pages_by_course.values()))} class pages are reachable."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
