"""Weirdest Job Title entry.

Writes exactly one job title, 60 characters or fewer, to entry.txt
inside the grader's output directory (MAKEFUN_OUTPUT_DIR, /output by
default). Nothing else is written; the file holds the title alone.
"""

import os

TITLE = "Senior Apologizer for Self-Checkout Machines"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TITLE)


if __name__ == "__main__":
    main()
