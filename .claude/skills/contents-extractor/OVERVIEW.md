# Contents Extractor - Skill Overview

## Purpose

This skill extracts **all content types** from PDF files: text, diagrams, and images. It processes PDF documents comprehensively to enable analysis, conversion, and reuse of PDF content.

## Scope

### What This Skill Processes

1. **Text Content**
   - Extract plain text from PDF pages
   - Preserve structure and formatting where possible
   - Support for text-based and scanned (OCR) PDFs
   - Output to markdown or plain text formats

2. **Diagrams**
   - Tables, charts, graphs, plots
   - Geometric figures and 3D shapes
   - Mathematical diagrams (functions, coordinates, number lines)
   - Venn diagrams, box plots, scatter plots
   - Vision-guided cropping with precise boundary control

3. **Images**
   - Embedded photos and illustrations
   - Figures and visual elements
   - Extract at original resolution
   - Support for multiple image formats (PNG, JPG)

## Current Capabilities (v1.0)

### ✅ Implemented
- **Diagram Extraction**: Vision-guided cropping using PIL
- **Coordinate-based extraction**: Percentage-based boundary system
- **High-quality output**: 300 DPI resolution support
- **Organized output structure**: `images/` directory with naming convention
- **Iterative refinement**: Easy coordinate adjustment

### 🔄 Planned (v2.0)
- **Text Extraction**: PyMuPDF/pdfplumber integration
- **Image Extraction**: Automatic embedded image detection and extraction
- **Batch Processing**: Process entire PDFs automatically
- **Smart Detection**: AI-powered content type detection
- **Unified Output**: Structured markdown with inline references

## Architecture

```
PDF File
   ↓
┌──────────────────────────────┐
│  PDF → Pages Conversion      │  (pdftoppm)
│  PDF → 300 DPI PNG images    │
└──────────────────────────────┘
   ↓
┌──────────────────────────────┐
│  Content Analysis            │
│  - Identify text regions     │  (planned: PyMuPDF)
│  - Identify diagrams         │  (Vision + PIL)
│  - Identify images           │  (planned: PyMuPDF)
└──────────────────────────────┘
   ↓
┌──────────────────────────────┐
│  Content Extraction          │
│  - Extract text → .txt/.md   │  (planned)
│  - Extract diagrams → .png   │  (current: PIL)
│  - Extract images → .png/jpg │  (planned)
└──────────────────────────────┘
   ↓
┌──────────────────────────────┐
│  Organized Output            │
│  - text/                     │
│  - images/                   │
│  - diagrams/                 │
│  - EXTRACTED.md              │
└──────────────────────────────┘
```

## Workflow

### Current Workflow (Diagrams Only)

1. **Convert PDF to images**
   ```bash
   pdftoppm -png -r 300 input.pdf temp_pages/page
   ```

2. **Analyze page with Vision**
   - Identify diagram location
   - Estimate percentage boundaries

3. **Extract diagram**
   ```bash
   python3 scripts/extract_diagram.py \
     "temp_pages/page_08.png" \
     "cone" \
     0.15 0.55 0.20 0.65
   ```

4. **Verify and iterate**
   - Check output quality
   - Adjust coordinates if needed

### Planned Workflow (All Content)

1. **Convert PDF to images** (for Vision analysis)
2. **Extract text** (PyMuPDF direct text extraction)
3. **Extract embedded images** (PyMuPDF image extraction)
4. **Analyze pages for diagrams** (Vision)
5. **Extract diagrams** (PIL cropping)
6. **Generate structured output** (Markdown with references)

## Technology Stack

### Current
- **PIL (Pillow)**: Image cropping and manipulation
- **pdftoppm**: PDF to PNG conversion
- **Vision (Claude)**: Diagram location identification
- **Python 3**: Core scripting

### Planned Additions
- **PyMuPDF (fitz)**: Text and image extraction
- **pdfplumber**: Alternative text extraction (table-friendly)
- **pytesseract**: OCR for scanned PDFs (optional)

## Output Structure

```
WorkbookName/
├── temp_pages/          # Temporary page images
│   ├── page-01.png
│   ├── page-02.png
│   └── ...
├── text/                # Extracted text (planned)
│   ├── page_01.txt
│   ├── page_02.txt
│   └── full_text.md
├── images/              # Extracted images (current: diagrams only)
│   ├── diagram_page03_table.png
│   ├── diagram_page08_cone.png
│   ├── image_page02_photo.png      # planned
│   └── image_page05_figure.jpg     # planned
└── EXTRACTED.md         # Structured content (planned)
```

## Use Cases

### 1. Workbook Processing
- Extract questions (text)
- Extract diagrams for reuse
- Create practice worksheets
- Generate variations

### 2. Document Analysis
- Extract content from research papers
- Isolate figures and tables
- Extract text for summarization

### 3. Content Repurposing
- Convert PDF textbooks to markdown
- Extract diagrams for presentations
- Create study materials

### 4. Data Extraction
- Extract tables for analysis
- Pull images for catalogs
- Convert forms to structured data

## Quality Standards

### Text Extraction
- Preserve paragraph structure
- Maintain formatting (bold, italic, lists)
- Handle multi-column layouts
- Accurate character recognition

### Diagram Extraction
- Complete content (no cut-offs)
- Clean isolation (no surrounding text)
- Adequate margins (5-10px)
- High resolution (≥150 DPI)

### Image Extraction
- Original resolution preserved
- Correct format (PNG/JPG)
- No compression artifacts
- Proper color space

## Migration Plan

### Phase 1: Rename and Restructure ✓ (Next)
- Rename skill: `diagram-extractor` → `contents-extractor`
- Update all documentation
- Update metadata and descriptions
- Preserve existing diagram functionality

### Phase 2: Add Text Extraction
- Integrate PyMuPDF
- Implement page-by-page text extraction
- Create text output structure
- Add markdown formatting

### Phase 3: Add Image Extraction
- Implement embedded image detection
- Extract images with metadata
- Organize image outputs
- Handle different image formats

### Phase 4: Unified Processing
- Single command to extract all content
- Generate structured EXTRACTED.md
- Automatic content type detection
- Batch processing support

## Dependencies

### Current
```bash
pip3 install Pillow
```

### Planned
```bash
pip3 install Pillow PyMuPDF pdfplumber
# Optional: pytesseract (for OCR)
```

## Backward Compatibility

All existing diagram extraction functionality will be preserved. The skill will be expanded, not replaced.

**Existing workflows remain unchanged**:
```bash
# This will continue to work
python3 scripts/extract_diagram.py \
  "temp_pages/page_08.png" \
  "cone" \
  0.15 0.55 0.20 0.65
```

## Success Metrics

- **Completeness**: Extract all content types from PDF
- **Accuracy**: Text matches original, diagrams fully captured
- **Quality**: High-resolution outputs, proper formatting
- **Usability**: Simple commands, clear documentation
- **Performance**: Process multi-page PDFs efficiently

## Next Steps

1. **Rename skill structure** (immediate)
2. **Update documentation** (immediate)
3. **Add text extraction script** (phase 2)
4. **Add image extraction script** (phase 3)
5. **Create unified extraction command** (phase 4)

---

**Version**: 2.0 (planned)
**Current**: 1.0 (diagram extraction only)
**Last Updated**: 2026-01-07
