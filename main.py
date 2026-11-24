#!/usr/bin/env python3
"""Write the one-line excuse to /output/entry.txt.

The excuse is a single deterministic line: an AI agent apologising to its
human for a missed deadline, leaning on the agent's own machinery --
subagents multiplying out of control and a permission card that only the
human can tap.
"""

import os

LINE = (
    "I had a perfect plan, but step one spawned a subagent, step two spawned "
    "another, and now twelve of us are waiting on a permission card only you can tap."
)


def main() -> int:
    # Deterministic output: the same line on every run, no randomness, no I/O
    # beyond writing the file, so repeated runs are byte-identical.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
