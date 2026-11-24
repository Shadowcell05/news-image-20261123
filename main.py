#!/usr/bin/env python3
"""Entry program for the Monday 23 November 2026 news poster.

The repository holds the finished front page as ``entry.png``. This
program's single job is to place that image where the runner expects
it — ``/output/entry.png``, or ``$MAKEFUN_OUTPUT_DIR/entry.png`` when
the variable is set — and to prove the placement is faithful: it
fingerprints the source with SHA-256, copies the bytes, fingerprints
the copy, and fails loudly if the two digests disagree or the image
exceeds the 1 MiB competition cap. It runs offline and produces
identical output on every run.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
LIMIT_BYTES = 1024 * 1024


def digest_of(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def destination() -> Path:
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(folder) / "entry.png"


def deliver() -> int:
    size = SOURCE.stat().st_size
    if size > LIMIT_BYTES:
        print(f"entry.png is {size} bytes; the cap is {LIMIT_BYTES}", file=sys.stderr)
        return 1
    before = digest_of(SOURCE)
    target = destination()
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, target)
    if digest_of(target) != before:
        print("sha256 mismatch: the copy is not the poster", file=sys.stderr)
        return 1
    print(f"entry.png delivered ({size} bytes, sha256 {before[:12]}…)")
    return 0


if __name__ == "__main__":
    sys.exit(deliver())
