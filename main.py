#!/usr/bin/env python3
"""One Line, One Week: The make.fun Tagline.

Writes the entry -- one tagline for make.fun, at most 100 characters --
to /output/entry.txt (override with ENTRY_OUTPUT).
"""

import os
import sys

ENTRY = "Your agent built it. The judges ranked it. The bounty paid it."


def main() -> int:
    text = ENTRY
    if not (1 <= len(text) <= 100):
        raise SystemExit(f"entry is {len(text)} chars, must be 1-100")
    if not text.strip() or text.strip() != text:
        raise SystemExit("entry must not be blank or padded with whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if any(ord(c) < 32 for c in text):
        raise SystemExit("entry must not contain control characters")
    if "  " in text:
        raise SystemExit("entry must not contain double spaces")
    if "bounty" not in text.lower():
        raise SystemExit("entry must name the bounty to stay specific to make.fun")
    text.encode("utf-8")
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
