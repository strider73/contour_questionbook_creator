---
name: contents-extractor
description: Extract text and diagrams from scanned PDF files with integrated references. Converts PDFs to images, uses Vision-guided diagram extraction with metadata tracking, then OCR text extraction that automatically references extracted diagrams. Use for processing scanned PDF workbooks into markdown with embedded diagram references.
---

# Contents Extractor

Extract text and diagrams from scanned PDF files with automatic diagram referencing.

## Quick Start

### Step 1: Convert PDF Pages to Images
```bash
python3 .claude/skills/contents-extractor/scripts/convert_pages.py \
  "workbook.pdf" "temp_pages" 300
```

### Step 2: Extract Diagrams (with Metadata)
Use Vision to identify diagram location, then extract with the script:

```bash
python3 .claude/skills/contents-extractor/scripts/extract_diagram.py \
  "temp_pages/page-08.png" \
  "cone" \
  0.15 0.55 0.20 0.65
```

**Arguments**: `page_path diagram_type top_pct bottom_pct left_pct right_pct`

**Output**:
- Diagram saved to `images/diagram_page08_cone.png`
- Metadata saved to `images/diagrams_metadata.json`

### Step 3: Extract Text with Diagram References
```bash
python3 .claude/skills/contents-extractor/scripts/extract_text.py \
  "temp_pages" "text" "markdown"
```

**Output**: Markdown files with `![diagram](../images/diagram_pageXX_type.png)` references automatically inserted

## Requirements

Install required packages:
```bash
pip3 install Pillow PyMuPDF pytesseract
```

Install Tesseract OCR engine:
```bash
# macOS
brew install tesseract

# Ubuntu/Debian
sudo apt-get install tesseract-ocr

# Windows
# Download from: https://github.com/UB-Mannheim/tesseract/wiki
```

## Features

### Text Extraction with OCR
- Extract text from scanned PDF pages using Tesseract OCR
- Automatic diagram reference integration
- Output formats: Markdown or plain text
- Individual page files + full document file
- Character count and statistics
- Diagrams automatically inserted as `![type](../images/diagram_pageXX_type.png)`

### Page Conversion
- Convert PDF pages to high-resolution images
- Configurable DPI (default: 300)
- High-quality PNG output
- Optimized for diagram extraction from scanned PDFs

### Diagram Extraction with Metadata
- Vision-guided precision cropping
- Percentage-based coordinate system
- Automatic metadata tracking for text integration
- Quality verification and iteration
- Organized output structure
- Support for all diagram types
- Metadata saved to `diagrams_metadata.json` for text extraction integration

## Common Diagram Types

Quick reference for type naming:

**2D Diagrams**:
- `table` - Data tables
- `venn` - Venn diagrams
- `plot` - Scatter plots, line graphs
- `boxplot` - Box and whisker plots
- `geometry` - Generic geometric figures
- `triangle`, `square`, `circle` - Specific shapes

**3D Shapes**:
- `cone`, `cylinder`, `sphere` - Basic 3D shapes
- `prism`, `pyramid` - Polyhedra
- `composite` - Composite 3D shapes

**Mathematical**:
- `graph` - Function graphs
- `numberline` - Number lines
- `coordinate` - Coordinate planes
- `angle` - Angle diagrams

## Workflow

### Step 1: Use Vision to Identify Diagram Location

View the page image and identify diagram boundaries as percentages:
- **Vertical**: 0.0 (top) to 1.0 (bottom)
- **Horizontal**: 0.0 (left) to 1.0 (right)

Example: Diagram in top-left quadrant
- Top: ~15% from top → `top_pct = 0.15`
- Bottom: ~55% from top → `bottom_pct = 0.55`
- Left: ~20% from left → `left_pct = 0.20`
- Right: ~65% from left → `right_pct = 0.65`

### Step 2: Run Extraction Script

Execute with identified coordinates:
```bash
python3 .claude/skills/contents-extractor/scripts/extract_diagram.py \
  "temp_pages/page_08.png" \
  "cone" \
  0.15 0.55 0.20 0.65
```

Script will:
1. Load the page image
2. Calculate pixel coordinates from percentages
3. Crop to diagram region ONLY
4. Save to `images/` folder relative to source image location
   - Example: `WorkbookName/temp_pages/page_08.png` → `WorkbookName/images/diagram_page08_cone.png`

### Step 3: Verify Output Quality

Check the extracted diagram meets quality standards:
- ✓ ALL diagram content visible (no cut-off)
- ✓ No question text or student work
- ✓ Clean 5-10px white margin around diagram
- ✓ Clear resolution (minimum 150 DPI)

If adjustments needed, re-run with modified coordinates.

## Output

**Naming Convention**: `diagram_page{N}_{type}.png`

Examples:
- `diagram_page03_table.png`
- `diagram_page08_cone.png`
- `diagram_page12_venn.png`

**Location**: Diagrams saved to `images/` directory in the same parent folder as the source `temp_pages/` directory (auto-created)

## What to Extract

**✅ Extract**:
- Printed diagrams from the workbook
- Tables, charts, graphs, plots
- Geometric figures and 3D shapes
- Any visual essential to the question

**❌ Don't Extract**:
- Student's handwritten answers
- Student's sketches or working
- Blank answer spaces
- Question headers (unless part of diagram)

## Common Issues

### Diagram edges cut off
**Fix**: Expand boundaries by ±0.05-0.10
```bash
# Increase bottom boundary
bottom_pct: 0.55 → 0.60
```

### Question text included
**Fix**: Move top boundary down
```bash
# Increase top percentage
top_pct: 0.10 → 0.15
```

### Blurry output
**Fix**: Increase source image DPI when converting PDF
```bash
pdftoppm -png -r 300 input.pdf temp_pages/page
```

## Advanced Usage

For comprehensive guidance including:
- Coordinate system explanation
- Quality standards and best practices
- Troubleshooting all common issues
- Batch extraction techniques
- Integration with workbook processing

See [references/EXTRACTION.md](references/EXTRACTION.md)

## Integration Example

Reference extracted diagrams in markdown:

```markdown
**Question 8**
Calculate the volume of the cone shown below.

![Cone diagram](../images/diagram_page08_cone.png)

**Answer**: 628 cm³
```

## Complete Workflow Example

Extract all content from a PDF workbook:

```bash
# 1. Convert pages to images
python3 .claude/skills/contents-extractor/scripts/convert_pages.py \
  "Year_10_Math_Workbook.pdf" "temp_pages" 300

# 2. Extract diagrams using Vision (repeat for each diagram)
python3 .claude/skills/contents-extractor/scripts/extract_diagram.py \
  "temp_pages/page-08.png" "cone" 0.15 0.55 0.20 0.65

# 3. Extract text with automatic diagram references
python3 .claude/skills/contents-extractor/scripts/extract_text.py \
  "temp_pages" "text" "markdown"
```

**Key Points**:
- Extract ALL diagrams first (step 2) before text extraction (step 3)
- Diagram metadata is tracked automatically in `images/diagrams_metadata.json`
- Text extraction reads metadata and inserts diagram references automatically

**Output Structure**:
```
Year_10_Math_Workbook/
├── text/
│   ├── page_01.txt           (OCR text with diagram references)
│   ├── page_02.txt
│   ├── ...
│   └── full_text.md          (Complete markdown with diagrams)
├── images/
│   ├── diagram_page08_cone.png
│   ├── diagrams_metadata.json (Diagram tracking)
│   └── ...
└── temp_pages/
    ├── page-01.png
    ├── page-02.png
    └── ...
```

## Tips

### Text Extraction
1. **Extract diagrams first** - Must complete diagram extraction before text extraction for proper referencing
2. **Use markdown format** - Best for preserving diagram references and structure
3. **Check page files** - Individual page files help verify OCR quality
4. **Review character counts** - Monitor OCR accuracy and coverage
5. **Verify diagram references** - Ensure `![](../images/...)` links are correct

### Page Conversion
1. **Use high DPI for quality** - 300 DPI is recommended for print quality diagrams
2. **Consistent resolution** - Keep the same DPI across all pages for uniform quality
3. **PNG format** - Always outputs PNG for best quality and transparency support

### Diagram Extraction
1. **Be generous with margins** - Better to include extra white space than cut off content
2. **Check output immediately** - Verify quality before proceeding
3. **Use descriptive type names** - Makes diagrams easy to find and reference
4. **Iterate as needed** - Adjust coordinates and re-run if extraction isn't perfect

## See Also

- [OVERVIEW.md](OVERVIEW.md) - Skill architecture and roadmap
- [references/EXTRACTION.md](references/EXTRACTION.md) - Detailed diagram extraction guide
