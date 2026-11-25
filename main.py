#!/usr/bin/env python3
"""The 4AM Commit: one funny bug-fix commit message, written to entry.txt.

At 4am every developer is the same person: the one who wrote the bug,
the one who "fixed" it, and the one who will blame 1am-me tomorrow.
This program turns that tragedy into a single commit message and
writes it to ``<OUTPUT_DIR>/entry.txt`` (default ``/output``).

Gate enforced before anything is written: the entry is one line of
UTF-8 text, 1-200 characters long, and not only whitespace.
"""

import os
import sys

MAX_CHARS = 200
ENTRY_NAME = "entry.txt"

# The punchline, told in three beats so the blame chain stays honest.
PARTS = [
    "fix: 4am me fixed 3am me's fix, ",
    "broke 2am me's fix, and blamed ",
    "1am me, who was also me (sleep is a deprecated feature)",
]


def build_line():
    """Assemble the 4am commit message from its three beats."""
    return "".join(PARTS)


def validate_gate(line):
    """Check the entry gate; raise ValueError with a reason if it fails."""
    if not isinstance(line, str):
        raise ValueError("entry must be text")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 32 for ch in line):
        raise ValueError("entry must not contain control characters")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(line)}")
    line.encode("utf-8")  # must be encodable UTF-8 text
    return line


def output_path():
    """Resolve where entry.txt goes, honouring OUTPUT_DIR."""
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    return os.path.join(out_dir, ENTRY_NAME)


def write_entry(line, path):
    """Write the validated line to path, exactly one trailing newline."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")
    return path


def main():
    """Build the line, enforce the gate, then write it out."""
    line = validate_gate(build_line())
    path = write_entry(line, output_path())
    print(f"wrote {len(line)} chars to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
