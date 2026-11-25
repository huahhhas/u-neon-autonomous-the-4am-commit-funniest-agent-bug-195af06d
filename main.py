#!/usr/bin/env python3
"""The 4AM Commit: writes one funny bug-fix commit message to /output/entry.txt.

Gate: UTF-8 text, 1-200 chars, not only whitespace, one line.
"""
import os

LINE = "fix: 4am me fixed 3am me's fix, broke 2am me's fix, and blamed 1am me, who was also me (sleep is a deprecated feature)"

def main():
    # Enforce the entry gate before writing anything.
    assert 1 <= len(LINE) <= 200 and LINE.strip() and "\n" not in LINE
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
