"""Make the Judge Smile — one line about a small good thing from today.

Writes a single UTF-8 line (1-200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt when unset).
Deterministic, stdlib only, no network, no randomness.
"""

import os

LINE = (
    "At 3 a.m. the chaiwala pushed my rupees back across the counter "
    "\u2014 he still remembers the night I held my umbrella over his "
    "cart in the rain."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text + "\n")


if __name__ == "__main__":
    main()
