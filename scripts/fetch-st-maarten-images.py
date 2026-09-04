#!/usr/bin/env python3
"""Download hero and content images from Unsplash (Unsplash License)."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMAGES = ROOT / "images"

# Site-provided; skipped by fetch (see images/ATTRIBUTION.md).
CUSTOM_IMAGES: frozenset[str] = frozenset({
    "hero-st-maarten.png",
    "st-maarten-cruise-port.png",
    "orient-beach-hero.png",
    "st-maarten-faq.png",
    "catamaran-sailing.png",
    "maho-beach-hero.png",
})

# NEW photo IDs (2026-09) — distinct from Aruba and Cozumel attraction binaries.
# Avoid Cozumel Mayan ruins (PsgyWVeJjOA) and jeep (bHavJvvmcAU), and prior shared slugs.
DOWNLOADS: list[tuple[str, str, int]] = [
    ("best-st-maarten-excursions.png", "AxC1BwokQrQ", 1920),  # St Martin / Saint Martin aerial
    ("one-day-st-maarten.png", "9XngoIpxcEo", 1920),  # Turquoise bay aerial
    ("st-maarten-snorkelling.png", "5QgIuuBxKwM", 1920),  # Underwater snorkel
    ("st-maarten-island-tours.png", "G85VuTpw6jg", 1920),  # Coastal scenery (not ruins)
    ("st-maarten-atv-buggy.png", "L-2p8fapOA8", 1920),  # Adventure / off-road feel
    ("dutch-french-side.png", "Oaqk7qqNh_c", 1920),  # Colourful Caribbean townscape
    ("st-maarten-private-tours.png", "2FPjlAyMQTA", 1920),  # Distinct sightseeing
    ("st-maarten-family.png", "p8Drpg_duLw", 1920),  # Beach day with people
    ("st-maarten-beaches.png", "rDEOVtE7vOs", 1920),  # Tropical beach
    ("st-maarten-intro.png", "7Z03R1wOdmI", 1920),  # Caribbean landscape intro
]


def download(filename: str, slug: str, width: int) -> bool:
    dest = IMAGES / filename
    url = f"https://unsplash.com/photos/{slug}/download?force=true&w={width}"
    print(f"  {filename} <- {slug}")
    result = subprocess.run(
        ["curl", "-fsSL", "-o", str(dest), url],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"    FAILED: {result.stderr.strip()}", file=sys.stderr)
        return False
    size = dest.stat().st_size
    if size < 10_000:
        print(f"    WARNING: small file ({size} bytes)", file=sys.stderr)
    print(f"    OK ({size // 1024} KB)")
    return True


def main() -> None:
    IMAGES.mkdir(parents=True, exist_ok=True)
    print("Downloading St Maarten images from Unsplash…")
    if CUSTOM_IMAGES:
        print(f"  Skipping custom (add your own): {', '.join(sorted(CUSTOM_IMAGES))}")
    failed = 0
    for filename, slug, width in DOWNLOADS:
        if filename in CUSTOM_IMAGES:
            continue
        if not download(filename, slug, width):
            failed += 1
    if failed:
        raise SystemExit(f"{failed} download(s) failed.")
    print("Done.")


if __name__ == "__main__":
    main()
