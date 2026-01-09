#!/usr/bin/env python3
"""
Page Conversion Script
Converts PDF pages to high-resolution images for diagram extraction.
"""

import sys
import fitz  # PyMuPDF
from pathlib import Path

def convert_page_to_image(pdf_path, page_num, output_path, dpi=300):
    """
    Convert a specific PDF page to an image.

    Args:
        pdf_path: Path to the PDF file
        page_num: Page number (1-indexed)
        output_path: Output image path
        dpi: Resolution in DPI (default: 300)

    Returns:
        Path to saved image
    """
    doc = fitz.open(pdf_path)

    if page_num < 1 or page_num > len(doc):
        raise ValueError(f"Invalid page number: {page_num} (PDF has {len(doc)} pages)")

    page = doc[page_num - 1]

    # Render page to pixmap
    zoom = dpi / 72  # 72 is the default DPI
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat)

    # Save as PNG
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    pix.save(output_path)
    doc.close()

    print(f"✓ Page {page_num} converted to image: {output_path}")
    print(f"  - Resolution: {pix.width}x{pix.height}px ({dpi} DPI)")

    return str(output_path)

def convert_all_pages_to_images(pdf_path, output_dir=None, dpi=300):
    """
    Convert all PDF pages to images.

    Args:
        pdf_path: Path to the PDF file
        output_dir: Directory to save page images (default: "temp_pages" relative to PDF location)
        dpi: Resolution in DPI (default: 300)

    Returns:
        List of saved image paths
    """
    pdf_path = Path(pdf_path)

    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    doc = fitz.open(pdf_path)

    # Determine output directory
    if output_dir is None:
        output_path = pdf_path.parent / "temp_pages"
    else:
        output_path = Path(output_dir)

    output_path.mkdir(parents=True, exist_ok=True)

    print(f"Converting PDF pages to images...")
    print(f"Total pages: {len(doc)}")
    print(f"Resolution: {dpi} DPI")

    saved_images = []
    zoom = dpi / 72

    for page_num in range(len(doc)):
        page = doc[page_num]

        # Render page
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat)

        # Save image
        image_path = output_path / f"page-{page_num + 1:02d}.png"
        pix.save(image_path)
        saved_images.append(str(image_path))

        print(f"  ✓ Page {page_num + 1:02d}: {pix.width}x{pix.height}px")

    doc.close()

    print(f"\n✓ Page conversion complete!")
    print(f"  - Output directory: {output_path}")
    print(f"  - Total images: {len(saved_images)}")

    return saved_images

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: convert_pages.py <pdf_path> [output_dir] [dpi]")
        print("Example: convert_pages.py workbook.pdf temp_pages 300")
        print("\nConverts all PDF pages to high-resolution images for diagram extraction.")
        sys.exit(1)

    pdf_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None
    dpi = int(sys.argv[3]) if len(sys.argv) > 3 else 300

    try:
        convert_all_pages_to_images(pdf_path, output_dir, dpi)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
