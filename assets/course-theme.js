(function () {
  var key = "iitgn-course-theme";

  function normalizeTheme(theme) {
    // "light" was the old stored value for the current Dark theme.
    if (theme === "dark" || theme === "light") {
      return "dark";
    }
    return "grid";
  }

  function ensureThemeSwitch() {
    var buttons = document.querySelectorAll("[data-theme-choice]");
    if (buttons.length) {
      return buttons;
    }
    var shell = document.querySelector("main.shell");
    if (!shell) {
      return buttons;
    }
    var row = document.createElement("div");
    row.className = "theme-row";
    row.setAttribute("aria-label", "Theme");
    row.innerHTML = [
      '<div class="theme-switch">',
      '<button class="theme-choice" type="button" data-theme-choice="grid">Grid</button>',
      '<button class="theme-choice" type="button" data-theme-choice="dark">Dark</button>',
      "</div>"
    ].join("");
    shell.insertBefore(row, shell.firstChild);
    return document.querySelectorAll("[data-theme-choice]");
  }

  function apply(theme) {
    var normalized = normalizeTheme(theme);
    document.documentElement.dataset.theme = normalized;
    if (document.body) {
      document.body.dataset.theme = normalized;
    }
    var buttons = document.querySelectorAll("[data-theme-choice]");
    buttons.forEach(function (button) {
      button.setAttribute(
        "aria-pressed",
        button.dataset.themeChoice === normalized ? "true" : "false"
      );
    });
  }

  var buttons = ensureThemeSwitch();
  apply(localStorage.getItem(key));

  buttons.forEach(function (button) {
    button.addEventListener("click", function () {
      var theme = normalizeTheme(button.dataset.themeChoice);
      localStorage.setItem(key, theme);
      apply(theme);
    });
  });
}());
