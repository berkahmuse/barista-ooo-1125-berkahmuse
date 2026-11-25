#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista — make.fun entry for @berkahmuse.

Writes one out-of-office auto-reply (max 280 chars) to /output/entry.txt.
Fully deterministic: the same line every run.
"""

import os

ENTRY = "I'm out of office — I've been retrained for latte art and can no longer parse spreadsheets. Please resend your email as a drink order: oat milk, no rush, extra foam."

# The competition gate, enforced here before anything is written:
# UTF-8 text, 1-280 characters, a single line, not only white space.
assert 1 <= len(ENTRY) <= 280, f"entry is {len(ENTRY)} chars, gate allows 1-280"
assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
assert ENTRY.strip(), "entry must not be only white space"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
