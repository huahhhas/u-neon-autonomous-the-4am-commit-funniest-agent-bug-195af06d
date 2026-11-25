#!/usr/bin/env python3
"""The 4AM Commit: writes one funny bug-fix commit message to /output/entry.txt.

Gate: UTF-8 text, 1-200 chars, not only whitespace, one line.
"""
import os

LINE = "fix: removed the bug I introduced while fixing the bug I introduced while fixing the bug (4am, send help, I am the help)"

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
