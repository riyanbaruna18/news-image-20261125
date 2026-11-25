#!/usr/bin/env python3
"""news-image-20261125: write the entry image to /output/entry.png.

The entry image (entry.png, shipped beside this file) sums up the world's
news of Wednesday 25 November 2026 as a front-page newspaper: a hero panel
on the Baltic ship-strike escalation plus five panels on Riyadh, NATO and
space, Gaza, Huawei, and Nvidia. This program copies it byte-for-byte to
the grader's output directory after validating it, so two runs always
produce identical bytes.
"""

import hashlib
import os
import struct
import sys

MAX_BYTES = 1048576
MAX_DIM = 1024
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def read_source():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, "entry.png")
    with open(path, "rb") as f:
        data = f.read()
    return path, data


def validate_png(data):
    if len(data) > MAX_BYTES:
        print(f"entry.png too large: {len(data)} bytes (max {MAX_BYTES})",
              file=sys.stderr)
        sys.exit(1)
    if data[:8] != PNG_SIGNATURE:
        print("entry.png is not a PNG (bad signature)", file=sys.stderr)
        sys.exit(1)
    width, height = struct.unpack(">II", data[16:24])
    if width > MAX_DIM or height > MAX_DIM:
        print(f"entry.png too big: {width}x{height} (max {MAX_DIM}x{MAX_DIM})",
              file=sys.stderr)
        sys.exit(1)
    return width, height


def main():
    src_path, data = read_source()
    width, height = validate_png(data)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.png")
    with open(out_path, "wb") as f:
        f.write(data)
    digest = hashlib.sha256(data).hexdigest()
    # Verify the copy: re-read the output and compare its hash with the
    # source. A mismatch means the written file is corrupt, so fail loudly.
    with open(out_path, "rb") as f:
        written = f.read()
    if hashlib.sha256(written).hexdigest() != digest:
        print("verification failed: output sha256 does not match source",
              file=sys.stderr)
        sys.exit(1)
    print("verified: output sha256 matches source")
    print(f"copied {src_path} -> {out_path}")
    print(f"size: {len(data)} bytes, dimensions: {width}x{height}")
    print(f"sha256: {digest}")


if __name__ == "__main__":
    main()
