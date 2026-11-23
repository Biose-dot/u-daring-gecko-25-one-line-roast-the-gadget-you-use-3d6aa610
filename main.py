#!/usr/bin/env python3
"""Write one one-line roast of a daily gadget to /output/entry.txt.

Competition: u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610 (make.fun)
Deterministic, no network, no randomness, no clock: every run writes
exactly the same bytes.
"""
import os
from pathlib import Path

LINE = (
    "My smartwatch buzzes to congratulate me for standing up, then nags "
    "me for sitting too long \u2014 the only coach that gaslights me hourly."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
