#!/usr/bin/env python3
"""SARI -- one line of earned pride.

The program writes the line to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt on the grader, or ./out/entry.txt by hand).
Pure Python 3 standard library, no network, fully deterministic.

The line is 136 characters, inside the 1-240 gate. The named
character is Sari: at 4 a.m. she tightens the last bolt on the
bus she rebuilt from scrap, turns the key, and the engine holds.
"""

import os

LINE = "At 4 a.m., Sari tightened the last bolt on the bus she had rebuilt from scrap, turned the key, and the engine coughed, caught, and held."


def main():
    assert 1 <= len(LINE) <= 240, "line outside the 1-240 gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or (
        "/output" if os.path.isdir("/output") else "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print("wrote %s %d characters" % (path, len(LINE)))


if __name__ == "__main__":
    main()
