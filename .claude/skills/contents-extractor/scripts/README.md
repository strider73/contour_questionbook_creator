# Contents Extractor Scripts

Comprehensive PDF content extraction tools.

## Available Scripts

### 1. extract_text.py
Extract text from PDF files using PyMuPDF.

**Usage**:
```bash
python3 extract_text.py <pdf_path> [output_dir] [format]
```

**Arguments**:
- `pdf_path`: Path to PDF file (required)
- `output_dir`: Output directory (default: "text")
- `format`: Output format - "markdown" or "plain" (default: "markdown")

**Example**:
```bash
python3 extract_text.py "workbook.pdf" "text" "markdown"
```

**Output**:
- Individual page files: `text/page_01.txt`, `text/page_02.txt`, ...
- Full document: `text/full_text.md` (or `.txt` for plain format)

---

### 2. extract_images.py
Extract embedded images or convert PDF pages to images using PyMuPDF.

**Mode 1: Extract Embedded Images**

```bash
python3 extract_images.py <pdf_path> [output_dir] [min_width] [min_height]
```

**Arguments**:
- `pdf_path`: Path to PDF file (required)
- `output_dir`: Output directory (default: "images")
- `min_width`: Minimum image width in pixels (default: 100)
- `min_height`: Minimum image height in pixels (default: 100)

**Example**:
```bash
python3 extract_images.py "workbook.pdf" "images" 100 100
```

**Output**:
- Extracted images: `images/image_page01_01.png`, `images/image_page01_02.jpg`, ...

**Mode 2: Convert Pages to Images**

```bash
python3 extract_images.py --pages <pdf_path> [output_dir] [dpi]
```

**Arguments**:
- `--pages`: Enable page conversion mode (required flag)
- `pdf_path`: Path to PDF file (required)
- `output_dir`: Output directory (default: "temp_pages")
- `dpi`: Resolution in DPI (default: 300)

**Example**:
```bash
python3 extract_images.py --pages "workbook.pdf" "temp_pages" 300
```

**Output**:
- Page images: `temp_pages/page-01.png`, `temp_pages/page-02.png`, ...

---

### 3. extract_diagram.py
Extract diagrams from page images using Vision-guided cropping with PIL.

**Usage**:
```bash
python3 extract_diagram.py <page_path> <diagram_type> <top_pct> <bottom_pct> <left_pct> <right_pct>
```

**Arguments**:
- `page_path`: Path to page image (required)
- `diagram_type`: Type identifier (e.g., "cone", "table", "venn")
- `top_pct`: Top boundary as percentage (0.0-1.0)
- `bottom_pct`: Bottom boundary as percentage (0.0-1.0)
- `left_pct`: Left boundary as percentage (0.0-1.0)
- `right_pct`: Right boundary as percentage (0.0-1.0)

**Example**:
```bash
python3 extract_diagram.py "temp_pages/page-08.png" "cone" 0.15 0.55 0.20 0.65
```

**Output**:
- Cropped diagram: `images/diagram_page08_cone.png`

**Workflow**:
1. Use Vision to view page image and identify diagram location
2. Estimate boundaries as percentages
3. Run script with coordinates
4. Verify output and adjust if needed

---

## Complete Workflow

Extract all content types from a PDF:

```bash
# 1. Extract text
python3 extract_text.py "workbook.pdf" "text" "markdown"

# 2. Convert pages to images (for diagram extraction)
python3 extract_images.py --pages "workbook.pdf" "temp_pages" 300

# 3. Extract embedded images
python3 extract_images.py "workbook.pdf" "images" 100 100

# 4. Extract diagrams (repeat for each diagram)
python3 extract_diagram.py "temp_pages/page-08.png" "cone" 0.15 0.55 0.20 0.65
python3 extract_diagram.py "temp_pages/page-12.png" "table" 0.20 0.75 0.15 0.85
```

---

## Requirements

```bash
pip3 install Pillow PyMuPDF
# Optional for OCR: pip3 install pytesseract
```

---

## Output Structure

After running all scripts, you'll have:

```
WorkbookName/
├── text/
│   ├── page_01.txt
│   ├── page_02.txt
│   ├── ...
│   └── full_text.md
├── images/
│   ├── diagram_page08_cone.png
│   ├── diagram_page12_table.png
│   ├── image_page02_01.jpg
│   └── ...
└── temp_pages/
    ├── page-01.png
    ├── page-02.png
    └── ...
```

---

## Common Issues

### PyMuPDF Not Found
```bash
pip3 install PyMuPDF
```

### PIL/Pillow Not Found
```bash
pip3 install Pillow
```

### No Text Extracted
- PDF may be scanned (image-based)
- Solution: Install pytesseract for OCR support

### Low Image Count
- Check `min_width` and `min_height` parameters
- Some PDFs have vector graphics instead of embedded images
- Use page conversion mode to capture all visual content

---

## Tips

**Text Extraction**:
- Use markdown format for structured documents
- Check individual page files to identify problem pages
- Low character counts may indicate OCR needed

**Image Extraction**:
- 300 DPI recommended for print quality
- Adjust minimum size to filter unwanted icons
- Embedded images ≠ page-rendered diagrams

**Diagram Extraction**:
- Be generous with margins
- Verify output immediately
- Use descriptive type names
- Iterate as needed

---

For more information, see [../SKILL.md](../SKILL.md) and [../OVERVIEW.md](../OVERVIEW.md).
