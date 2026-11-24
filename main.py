#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters.

Writes a single loading-screen tip for stressed developers and AI
coding agents to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os

ENTRY = "Tip: I read all 4,000 lines of the error log so you don't have to \u2014 the bug is on line 3, and yes, you wrote it."


def main():
    # Gate: UTF-8 text of 1-200 characters, not only whitespace, one line.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip() and "\n" not in ENTRY.strip(), "entry must be one line"
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    print("wrote", path)


if __name__ == "__main__":
    main()
