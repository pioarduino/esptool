#!/usr/bin/env python
#
# SPDX-FileCopyrightText: 2026 Espressif Systems (Shanghai) CO LTD
# SPDX-License-Identifier: GPL-2.0-or-later
#
"""Generate trivial size / fill binary blobs for the esptool test suite.

These fixtures exercise flash I/O, merge-bin, and similar size/edge-case paths.
They are *not* firmware or partition goldens — those stay committed under
test/images/ and must not be produced with esptool/espsecure (circular).

Payload bytes are deterministic from the seeds below; they are *not* bit-identical
to the historical committed blobs (sizes and the one_kb 0xED magic are preserved).
Tests write-then-verify against the same generated file, so content drift is fine.

Called automatically from conftest.py before pytest runs, or manually:

    python test/bin_builder.py [--output test/images]
"""

import argparse
import struct
from pathlib import Path

# Distinct seeds so the size blobs are not prefixes of each other.
_SEED_ONE_KB = 0x0A1E1001
_SEED_ONE_MB = 0x0A1E1002
_SEED_FIFTY_KB = 0x0A1E1003
_SEED_SECTOR = 0x0A1E1004

# Byte 0 of one_kb.bin must be 0xED so test_image_info.py
# test_invalid_image_type_detection can assert "invalid magic number: 0xed".
_ONE_KB_MAGIC = 0xED


def xorshift_bytes(n: int, seed: int = 0xDEADBEEF) -> bytes:
    """Generate n pseudo-random bytes via xorshift32 (deterministic)."""
    state = seed & 0xFFFFFFFF
    out = bytearray(n)
    i = 0
    while i < n:
        state ^= (state << 13) & 0xFFFFFFFF
        state ^= (state >> 17) & 0xFFFFFFFF
        state ^= (state << 5) & 0xFFFFFFFF
        word = struct.pack("<I", state)
        chunk = min(4, n - i)
        out[i : i + chunk] = word[:chunk]
        i += chunk
    return bytes(out)


def build_bin_fixtures() -> dict[str, bytes]:
    """Return filename -> contents for all generated size/fill blobs."""
    one_kb = bytearray(xorshift_bytes(1024, _SEED_ONE_KB))
    one_kb[0] = _ONE_KB_MAGIC

    return {
        "one_kb.bin": bytes(one_kb),
        "one_mb.bin": xorshift_bytes(1024 * 1024, _SEED_ONE_MB),
        "fifty_kb.bin": xorshift_bytes(50 * 1024, _SEED_FIFTY_KB),
        "sector.bin": xorshift_bytes(4096, _SEED_SECTOR),
        "zerolength.bin": b"",
        "onebyte.bin": b"a",
        "one_kb_all_ef.bin": b"\xef" * 1024,
        "aes_key.bin": b"\x00" * 32,
    }


def materialize_bin_fixtures(dest_dir: Path) -> int:
    """Write all generated size/fill blobs into dest_dir (created if needed).

    Returns the number of files written.
    """
    dest_dir = Path(dest_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)
    fixtures = build_bin_fixtures()
    for name, data in fixtures.items():
        (dest_dir / name).write_bytes(data)
    return len(fixtures)


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description="Generate trivial size/fill .bin fixtures for esptool tests."
    )
    default_out = Path(__file__).resolve().parent / "images"
    parser.add_argument(
        "--output",
        type=Path,
        default=default_out,
        help=f"Destination directory (default: {default_out})",
    )
    args = parser.parse_args(argv)
    dest = Path(args.output)
    count = materialize_bin_fixtures(dest)
    print(f"Wrote {count} bin fixtures to {dest}")


if __name__ == "__main__":
    main()
