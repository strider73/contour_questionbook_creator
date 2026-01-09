#!/usr/bin/env python3
"""
Diagram Extraction Script
Extracts diagram regions from page images using Vision-provided coordinates.
Saves metadata for text extraction integration.
"""

import sys
import json
from PIL import Image
from pathlib import Path

def extract_diagram(page_path, diagram_type, top_pct, bottom_pct, left_pct, right_pct, output_dir=None):
    """
    Extract diagram region from page image using percentage coordinates.

    Args:
        page_path: Path to the page image (e.g., "temp_pages/page_08.png")
        diagram_type: Type of diagram (e.g., "cone", "table", "venn")
        top_pct: Top boundary as percentage (0.0 to 1.0)
        bottom_pct: Bottom boundary as percentage (0.0 to 1.0)
        left_pct: Left boundary as percentage (0.0 to 1.0)
        right_pct: Right boundary as percentage (0.0 to 1.0)
        output_dir: Directory to save extracted diagram (default: "images" relative to page_path parent)

    Returns:
        Path to saved diagram file
    """
    # Load page image
    page_img = Image.open(page_path)
    width, height = page_img.size

    # Calculate pixel coordinates from percentages
    left = int(width * left_pct)
    top = int(height * top_pct)
    right = int(width * right_pct)
    bottom = int(height * bottom_pct)

    # Crop to diagram region ONLY
    diagram = page_img.crop((left, top, right, bottom))

    # Extract page number from filename (e.g., "page-08.png" -> "08")
    page_name = Path(page_path).stem
    # Handle both "page-08" and "page_08" formats
    if '-' in page_name:
        page_num = page_name.split('-')[-1]
    else:
        page_num = page_name.split('_')[-1]

    # Determine output directory relative to source image location
    if output_dir is None:
        # Create images/ folder in the parent directory of the source image
        source_parent = Path(page_path).parent.parent
        output_path = source_parent / "images"
    else:
        output_path = Path(output_dir)

    output_path.mkdir(parents=True, exist_ok=True)

    # Save with naming convention: diagram_page{N}_{type}.png
    output_file = output_path / f"diagram_page{page_num}_{diagram_type}.png"
    diagram.save(output_file)

    # Save/update metadata for text extraction integration
    metadata_file = output_path / "diagrams_metadata.json"

    # Load existing metadata or create new
    if metadata_file.exists():
        with open(metadata_file, "r", encoding="utf-8") as f:
            metadata = json.load(f)
    else:
        metadata = {}

    # Add this diagram's metadata
    page_key = f"page_{page_num}"
    if page_key not in metadata:
        metadata[page_key] = []

    metadata[page_key].append({
        "type": diagram_type,
        "filename": output_file.name,
        "position": {
            "top": top_pct,
            "bottom": bottom_pct,
            "left": left_pct,
            "right": right_pct
        }
    })

    # Save updated metadata
    with open(metadata_file, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

    print(f"✓ Diagram extracted: {output_file}")
    print(f"  - Type: {diagram_type}")
    print(f"  - Size: {diagram.size[0]}x{diagram.size[1]} pixels")
    print(f"  - Region: {left_pct*100:.0f}-{right_pct*100:.0f}% horizontal, {top_pct*100:.0f}-{bottom_pct*100:.0f}% vertical")
    print(f"  - Metadata saved: {metadata_file}")

    return str(output_file)

if __name__ == "__main__":
    if len(sys.argv) != 7:
        print("Usage: extract_diagram.py <page_path> <diagram_type> <top_pct> <bottom_pct> <left_pct> <right_pct>")
        print("Example: extract_diagram.py temp_pages/page_08.png cone 0.15 0.55 0.20 0.65")
        sys.exit(1)

    page_path = sys.argv[1]
    diagram_type = sys.argv[2]
    top_pct = float(sys.argv[3])
    bottom_pct = float(sys.argv[4])
    left_pct = float(sys.argv[5])
    right_pct = float(sys.argv[6])

    extract_diagram(page_path, diagram_type, top_pct, bottom_pct, left_pct, right_pct)
