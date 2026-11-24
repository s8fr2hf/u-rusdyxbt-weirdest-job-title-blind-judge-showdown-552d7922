#!/usr/bin/env python3
"""Write the weirdest job title to /output/entry.txt.

One title, 60 characters at most, nothing else, no trailing newline.
"""

import os
from pathlib import Path

TITLE = "Senior Apologizer for Elevators That Stop Between Floors"


def main() -> None:
    if not TITLE or not TITLE.strip() or len(TITLE) > 60:
        raise ValueError("title must be 1-60 non-whitespace characters")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(TITLE, encoding="utf-8")


if __name__ == "__main__":
    main()
