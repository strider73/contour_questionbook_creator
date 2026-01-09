#!/usr/bin/env python3
"""
Text Extraction Script with Diagram Integration
Extracts text from page images using OCR and integrates diagram references.
"""

import sys
import json
from pathlib import Path

try:
    import pytesseract
    from PIL import Image
    PYTESSERACT_AVAILABLE = True
except ImportError:
    PYTESSERACT_AVAILABLE = False

def extract_text_with_diagrams(pages_dir, output_dir=None, output_format="markdown"):
    """
    Extract text from page images using OCR and integrate diagram references.

    Args:
        pages_dir: Directory containing page images (e.g., "temp_pages")
        output_dir: Directory to save extracted text (default: "text" relative to pages_dir parent)
        output_format: Output format - "markdown" or "text" (default: "markdown")

    Returns:
        Dictionary with extraction results
    """
    if not PYTESSERACT_AVAILABLE:
        print("Error: pytesseract is not installed")
        print("Install it with: pip3 install pytesseract")
        print("\nNote: You also need to install Tesseract OCR:")
        print("  macOS: brew install tesseract")
        print("  Ubuntu: sudo apt-get install tesseract-ocr")
        print("  Windows: Download from https://github.com/UB-Mannheim/tesseract/wiki")
        sys.exit(1)

    pages_path = Path(pages_dir)

    if not pages_path.exists():
        raise FileNotFoundError(f"Pages directory not found: {pages_path}")

    # Determine output directory
    if output_dir is None:
        output_path = pages_path.parent / "text"
    else:
        output_path = Path(output_dir)

    output_path.mkdir(parents=True, exist_ok=True)

    # Load diagram metadata if available
    metadata_file = pages_path.parent / "images" / "diagrams_metadata.json"
    diagrams_metadata = {}
    if metadata_file.exists():
        with open(metadata_file, "r", encoding="utf-8") as f:
            diagrams_metadata = json.load(f)
        print(f"✓ Loaded diagram metadata: {len(diagrams_metadata)} pages with diagrams")

    # Get all page images
    page_files = sorted(pages_path.glob("page-*.png"))

    if not page_files:
        raise FileNotFoundError(f"No page images found in {pages_path}")

    print(f"\nExtracting text from {len(page_files)} pages...")
    print(f"OCR Engine: Tesseract")

    page_texts = []
    total_chars = 0

    for page_file in page_files:
        # Extract page number from filename (e.g., "page-08.png" -> "08")
        page_num = page_file.stem.split('-')[-1]
        page_key = f"page_{page_num}"

        print(f"\n  Processing page {page_num}...")

        # Load page image
        page_img = Image.open(page_file)

        # Check if this page has diagrams
        page_diagrams = diagrams_metadata.get(page_key, [])

        # Extract text using OCR
        try:
            text = pytesseract.image_to_string(page_img)
        except Exception as e:
            print(f"    ⚠ OCR failed: {e}")
            text = f"[OCR failed for page {page_num}]\n"

        # If page has diagrams, insert references
        if page_diagrams:
            diagram_refs = []
            for diagram in page_diagrams:
                diagram_type = diagram['type']
                filename = diagram['filename']
                diagram_refs.append(f"![{diagram_type} diagram](../images/{filename})")

            # Insert diagram references at the end of page text for now
            # (More sophisticated placement would require analyzing OCR layout)
            if output_format == "markdown":
                text += "\n\n" + "\n\n".join(diagram_refs) + "\n"

            print(f"    ✓ Inserted {len(page_diagrams)} diagram reference(s)")

        page_texts.append(text)
        total_chars += len(text)

        # Save individual page
        page_file_out = output_path / f"page_{page_num}.txt"
        with open(page_file_out, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"    ✓ Page {page_num} extracted ({len(text)} chars)")

    # Create full document file
    if output_format == "markdown":
        full_text_file = output_path / "full_text.md"
        with open(full_text_file, "w", encoding="utf-8") as f:
            for i, text in enumerate(page_texts):
                page_num = page_files[i].stem.split('-')[-1]
                f.write(f"# Page {int(page_num)}\n\n")
                f.write(text)
                f.write("\n\n---\n\n")
    else:
        full_text_file = output_path / "full_text.txt"
        with open(full_text_file, "w", encoding="utf-8") as f:
            f.write("\n\n".join(page_texts))

    # Count total diagrams integrated
    total_diagrams = 0
    for pf in page_files:
        page_num = pf.stem.split("-")[-1]
        page_key = f"page_{page_num}"
        total_diagrams += len(diagrams_metadata.get(page_key, []))

    print(f"\n✓ Text extraction complete!")
    print(f"  - Output directory: {output_path}")
    print(f"  - Full text: {full_text_file.name}")
    print(f"  - Individual pages: {len(page_texts)} files")
    print(f"  - Total characters: {total_chars:,}")
    print(f"  - Diagrams integrated: {total_diagrams}")

    return {
        "output_dir": str(output_path),
        "page_count": len(page_texts),
        "total_chars": total_chars,
        "full_text_file": str(full_text_file)
    }

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: extract_text.py <pages_dir> [output_dir] [format]")
        print("Example: extract_text.py temp_pages text markdown")
        print("\nExtracts text from page images using OCR and integrates diagram references.")
        print("Format options: 'markdown' or 'text' (default: markdown)")
        print("\nRequires: pip3 install pytesseract")
        sys.exit(1)

    pages_dir = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None
    output_format = sys.argv[3] if len(sys.argv) > 3 else "markdown"

    try:
        extract_text_with_diagrams(pages_dir, output_dir, output_format)
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
