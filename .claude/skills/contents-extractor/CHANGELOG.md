# Changelog

## Version 3.0 - 2026-01-07

### Major Features

#### Integrated Diagram Reference System
The biggest change: text extraction now automatically references extracted diagrams!

**New Workflow**:
1. Convert PDF pages to images
2. Extract diagrams (creates metadata automatically)
3. Extract text with OCR → diagrams automatically inserted as markdown references

**Example Output** (full_text.md):
```markdown
# Page 8

Calculate the volume of the cone shown below.

![cone diagram](../images/diagram_page08_cone.png)

Answer: 628 cm³
```

### Script Changes

#### extract_diagram.py
- **NEW**: Automatic metadata tracking
- Saves `images/diagrams_metadata.json` with diagram positions and types
- Metadata format: `{"page_08": [{"type": "cone", "filename": "...", "position": {...}}]}`
- Fully backward compatible (still extracts diagrams the same way)

#### extract_text.py (Restored and Enhanced)
- **NEW**: OCR text extraction using Tesseract
- **NEW**: Automatic diagram reference integration
- Reads `diagrams_metadata.json` and inserts `![](../images/...)` references
- Usage: `extract_text.py <pages_dir> [output_dir] [format]`
- Requires: `pip3 install pytesseract` + Tesseract OCR engine

#### convert_pages.py (Renamed from extract_images.py)
- Renamed for clarity (only converts pages, doesn't extract embedded images)
- Removed unused embedded image extraction functionality
- Simplified interface

### Requirements Updated

```bash
# Python packages
pip3 install Pillow PyMuPDF pytesseract

# System dependency (new)
brew install tesseract  # macOS
sudo apt-get install tesseract-ocr  # Ubuntu
```

### Breaking Changes
- **Workflow order changed**: Must extract diagrams BEFORE text extraction
- **extract_text.py usage changed**: Now takes `pages_dir` instead of PDF path
  - Old: `extract_text.py workbook.pdf text markdown`
  - New: `extract_text.py temp_pages text markdown`

### Migration Guide

**Old Workflow (v2.x)**:
```bash
python3 convert_pages.py workbook.pdf temp_pages 300
python3 extract_diagram.py temp_pages/page-08.png cone 0.15 0.55 0.20 0.65
# (no text extraction or manual diagram referencing)
```

**New Workflow (v3.0)**:
```bash
# 1. Convert pages
python3 convert_pages.py workbook.pdf temp_pages 300

# 2. Extract ALL diagrams (creates metadata)
python3 extract_diagram.py temp_pages/page-08.png cone 0.15 0.55 0.20 0.65
# ... repeat for all diagrams ...

# 3. Extract text with automatic diagram references
python3 extract_text.py temp_pages text markdown
```

### Benefits
- ✅ Automatic diagram referencing in markdown
- ✅ No manual markdown editing needed
- ✅ OCR text extraction from scanned PDFs
- ✅ Complete, ready-to-use markdown documents
- ✅ Metadata tracking for integration

---

## Version 2.1 - 2026-01-07 (Deprecated)

### Breaking Changes
- **Removed embedded image extraction** - Skill now focused on scanned PDFs only
- **Renamed script**: `extract_images.py` → `convert_pages.py`

---

## Version 2.0 - 2026-01-07

### Major Changes
- **Renamed**: `diagram-extractor` → `contents-extractor`
- **Expanded scope**: Now handles text, images, AND diagrams

### New Features

#### Text Extraction
- Extract text from all PDF pages
- Support for text-based PDFs via PyMuPDF
- Output formats: Markdown or plain text
- Individual page files + combined full document
- Character count statistics

**Script**: `scripts/extract_text.py`

#### Image Extraction
- Convert PDF pages to high-resolution images (300 DPI default)
- Extract embedded images from PDFs
- Configurable minimum size filtering
- Automatic format detection (PNG, JPG)
- Dual-mode operation: page conversion or embedded extraction

**Script**: `scripts/convert_pages.py` (was `extract_images.py` in v2.0)

#### Diagram Extraction (Preserved)
- Existing Vision-guided cropping functionality maintained
- All features from v1.0 preserved
- Updated paths to reflect new skill name

**Script**: `scripts/extract_diagram.py`

### New Documentation
- `OVERVIEW.md` - Architecture, roadmap, and migration plan
- `scripts/README.md` - Comprehensive script usage guide
- Updated `SKILL.md` - Full feature documentation
- `CHANGELOG.md` - This file

### Dependencies Updated
```bash
# Previous
pip3 install Pillow

# Current
pip3 install Pillow PyMuPDF
# Optional: pip3 install pytesseract
```

### Breaking Changes
- **Skill name changed**: Update any references from `diagram-extractor` to `contents-extractor`
- **Script paths changed**: Update paths in existing workflows
  - Old: `.claude/skills/diagram-extractor/scripts/`
  - New: `.claude/skills/contents-extractor/scripts/`

### Migration Guide

#### Update Existing Workflows

**Before**:
```bash
python3 .claude/skills/diagram-extractor/scripts/extract_diagram.py ...
```

**After**:
```bash
python3 .claude/skills/contents-extractor/scripts/extract_diagram.py ...
```

#### Install New Dependencies

```bash
pip3 install PyMuPDF
```

### File Structure

```
contents-extractor/
├── OVERVIEW.md          (NEW)
├── SKILL.md             (UPDATED)
├── CHANGELOG.md         (NEW)
├── references/
│   └── EXTRACTION.md    (PRESERVED)
└── scripts/
    ├── extract_diagram.py   (PRESERVED - paths updated)
    ├── extract_text.py      (NEW)
    ├── convert_pages.py     (NEW - renamed from extract_images.py in v2.1)
    └── README.md            (NEW)
```

### Backward Compatibility

All existing diagram extraction functionality is preserved:
- Same script interface
- Same arguments
- Same output format
- Same coordinate system

Only the skill name and paths have changed.

---

## Version 1.0 - 2026-01-06

### Initial Release
- Diagram extraction using Vision + PIL
- Percentage-based coordinate system
- Support for all diagram types
- Quality verification workflow
- Organized output structure

**Features**:
- Vision-guided cropping
- High-resolution extraction (300 DPI support)
- Iterative refinement
- Comprehensive documentation

**Script**: `scripts/extract_diagram.py`
