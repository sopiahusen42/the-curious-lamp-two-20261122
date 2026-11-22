"""Writes one text to entry.txt for make.fun's "Make the AI judge feel curious" bounty."""

import os
from pathlib import Path

TEXT = "Seam 14 on the Duncairn header was shot Tuesday. Film 240 by 80, source at 900, four minutes, density 2.4. It reads clean: cap, fusion line, backing ring, root. At 210 millimetres sits a second seam, whole, its own root and cap, crossing the first."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    target = Path(out_dir) if out_dir else Path(__file__).resolve().parent / "output"
    target.mkdir(parents=True, exist_ok=True)
    (target / "entry.txt").write_text(TEXT + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
