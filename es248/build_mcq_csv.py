#!/usr/bin/env python3
import csv

rows = [
    ["Question", "Correct Answer", "Option", "Option", "Option"],
]

# Q1
rows.append([
    "Q1. What is the time complexity of the following code in terms of n?\n\n"
    "for (int i = 1; i <= n; i = i * 2)\n"
    "    for (int j = 0; j < n; j++)\n"
    "        printf(\"*\");",
    "O(n log n)",
    "O(n)",
    "O(n^2)",
    "O(log n)",
])

# Q2 — Time
q2_code = (
    "void recursion(int N) {\n"
    "    if (N == 0) return;\n"
    "    printf(\"%d\\n\", N);\n"
    "    recursion(N - 1);\n"
    "}"
)
rows.append([
    "Q2 (Time). Consider:\n\n" + q2_code + "\n\nWhat is the TIME complexity?",
    "O(N)",
    "O(1)",
    "O(2^N)",
    "O(log N)",
])

# Q2 — Space
rows.append([
    "Q2 (Space). Consider:\n\n" + q2_code + "\n\nWhat is the SPACE complexity?",
    "O(N)",
    "O(1)",
    "O(log N)",
    "O(2^N)",
])

# Q3
rows.append([
    "Q3. What is the time complexity of the following code?\n\n"
    "void calc(int arr[], int N) {\n"
    "    int j = 0;\n"
    "    for (int i = 0; i < N; i++) {\n"
    "        while (j < N && arr[i] < arr[j]) {\n"
    "            j++;\n"
    "        }\n"
    "    }\n"
    "}",
    "O(N)",
    "O(log N)",
    "O(N * log N)",
    "O(N^2)",
])

# Q4
rows.append([
    "Q4. A singly linked list contains the nodes A -> B -> C -> D -> NULL, and head is a "
    "pointer to node A. After executing head->next = head->next->next;, which statement is "
    "correct?",
    "The list becomes A -> C -> D -> NULL; node B is leaked",
    "The list becomes A -> C -> D -> NULL; no memory leak",
    "The list becomes B -> C -> D -> NULL; node A is leaked",
    "The program crashes with a segmentation fault",
])

# Q5
rows.append([
    "Q5. A singly linked list maintains both head and tail pointers. "
    "Which of the following operations is NOT O(1)?",
    "Delete from tail",
    "Insert at head",
    "Insert at tail",
    "Delete from head",
])

# Q6
rows.append([
    "Q6. Consider the following function intended to free every node of a singly linked list:\n\n"
    "void destroyList(struct Node *head) {\n"
    "    while (head != NULL) {\n"
    "        free(head);\n"
    "        head = head->next;\n"
    "    }\n"
    "}\n\n"
    "What is wrong with this code?",
    "After free(head), accessing head->next reads freed memory — undefined behavior",
    "The base case is incorrect; should be head == NULL",
    "The function will crash with a segmentation fault if head is NULL when called",
    "The function correctly frees all nodes",
])

# Q7
rows.append([
    "Q7. A queue is implemented as a circular array of capacity 8, with fields front, "
    "rear (next insertion index), and size. Currently front = 6, rear = 2, size = 4. "
    "Which array indices currently hold queue elements?",
    "6, 7, 0, 1",
    "2, 3, 4, 5",
    "6, 7, 8, 0",
    "0, 1, 6, 7",
])

# Q8
rows.append([
    "Q8. Items 1, 2, 3, 4, 5 are pushed onto a stack in that order. They are then popped "
    "one at a time and each popped item is immediately enqueued onto a queue. After all five "
    "items are transferred, the queue is fully dequeued. In what order are the items dequeued?",
    "5, 4, 3, 2, 1",
    "1, 2, 3, 4, 5",
    "1, 3, 5, 4, 2",
    "5, 1, 4, 2, 3",
])

# Q9
rows.append([
    "Q9. What does the following declaration declare?\n\n"
    "int (*funcs[10])(int, int);",
    "An array of 10 pointers to functions, each taking two ints and returning an int",
    "An array of 10 functions, each returning an int and taking two int parameters",
    "A pointer to an array of 10 functions",
    "A function returning an array of 10 ints",
])

# Q10
q10_correct = (
    "int cmp(const void *a, const void *b) {\n"
    "    struct Student *sa = (struct Student*)a;\n"
    "    struct Student *sb = (struct Student*)b;\n"
    "    if (sa->score != sb->score)\n"
    "        return sb->score - sa->score;\n"
    "    return strcmp(sa->name, sb->name);\n"
    "}"
)
q10_distract_a = (
    "int cmp(const void *a, const void *b) {\n"
    "    return ((struct Student*)b)->score - ((struct Student*)a)->score;\n"
    "}"
)
q10_distract_c = (
    "int cmp(const void *a, const void *b) {\n"
    "    struct Student *sa = (struct Student*)a;\n"
    "    struct Student *sb = (struct Student*)b;\n"
    "    if (sa->score != sb->score)\n"
    "        return sa->score - sb->score;\n"
    "    return strcmp(sa->name, sb->name);\n"
    "}"
)
q10_distract_d = (
    "int cmp(const void *a, const void *b) {\n"
    "    return ((struct Student*)b)->score - ((struct Student*)a)->score\n"
    "         + strcmp(((struct Student*)a)->name, ((struct Student*)b)->name);\n"
    "}"
)
rows.append([
    "Q10. Which qsort comparator sorts an array of struct Student by score in DESCENDING "
    "order, with ties broken alphabetically by name?\n\n"
    "struct Student { char name[100]; int score; };",
    q10_correct,
    q10_distract_a,
    q10_distract_c,
    q10_distract_d,
])

# Q11
q11_correct = (
    "int cmp(const void *a, const void *b) {\n"
    "    return strcmp(*(char **)a, *(char **)b);\n"
    "}"
)
q11_distract_b = (
    "int cmp(const void *a, const void *b) {\n"
    "    return strcmp((char *)a, (char *)b);\n"
    "}"
)
q11_distract_d = (
    "int cmp(const void *a, const void *b) {\n"
    "    return *(char *)a - *(char *)b;\n"
    "}"
)
rows.append([
    "Q11. You want to sort the following array of strings alphabetically:\n\n"
    "char *names[] = {\"banana\", \"apple\", \"cherry\"};\n"
    "qsort(names, 3, sizeof(char *), cmp);\n\n"
    "Which definition of cmp works correctly?",
    q11_correct,
    "Pass strcmp directly as cmp",
    q11_distract_b,
    q11_distract_d,
])

# Q12
rows.append([
    "Q12. Assume a hypothetical system where sizeof(char) = 1, sizeof(int) = 4, alignment "
    "is 4 bytes (every member starts at a 4-byte boundary, struct size rounded up to a "
    "multiple of 4).\n\n"
    "struct S {\n"
    "    char a;\n"
    "    int  b;\n"
    "    char c;\n"
    "};\n\n"
    "What is sizeof(struct S)?",
    "12",
    "6",
    "9",
    "16",
])

# Q13
rows.append([
    "Q13. On a BIG-ENDIAN system (the most-significant byte is stored at the lowest memory "
    "address). Assume sizeof(int) = 4 and sizeof(char) = 1.\n\n"
    "union U {\n"
    "    int  i;\n"
    "    char c[4];\n"
    "};\n"
    "union U u;\n"
    "u.i = 0x12345678;\n\n"
    "What is the value of u.c[0]?",
    "0x12",
    "0x78",
    "0x34",
    "0x56",
])

# Q14
rows.append([
    "Q14. Given int arr[3][4]; and sizeof(int) = 2, what is (address of arr[2][2]) - "
    "(address of arr[1][2]), in bytes?",
    "8",
    "16",
    "4",
    "12",
])

# Q15
rows.append([
    "Q15. Consider:\n\n"
    "int a[3][4];\n"
    "int *q       = a[0];\n"
    "int (*p)[4]  = a;\n\n"
    "Initially q and p hold the same address — the address of a[0][0]. After executing q++ "
    "and p++ (assume sizeof(int) = 2), by how many bytes have q and p moved, respectively?",
    "2 bytes, 8 bytes",
    "4 bytes, 16 bytes",
    "8 bytes, 8 bytes",
    "2 bytes, 2 bytes",
])

with open("/Users/anup/work/iitgn/ES248/end-sem-mcq.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerows(rows)

print(f"Wrote {len(rows)} rows (1 header + {len(rows)-1} questions)")
