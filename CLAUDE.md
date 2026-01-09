# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Contour Question Book Creator is a system for generating curriculum-aligned test variations from existing mathematics tests. Given a reference workbook (containing theory/formulas/examples) and a test PDF, it creates fresh question variations that test the same concepts with new scenarios and diagrams.

## Commands

### Main Workflow
```bash
# Full test generation pipeline (orchestrates all sub-agents)
/generate-test "Workbook.pdf" "Test.pdf"
```

### Individual Sub-Commands (for debugging/testing)
```bash
# Analyze curriculum from workbook → curriculum_context.md
/analyze-curriculum "Workbook.pdf"

# Extract test questions and diagrams → ExtractedQuestions.md + images/
/extract-test "Test.pdf"

# Generate variations (requires prior analysis + extraction)
/generate-variations
```

### Python Script Commands
```bash
# Convert PDF pages to images
python3 .claude/skills/contents-extractor/scripts/convert_pages.py "input.pdf" "output_dir" 300

# Extract diagram from page image
python3 .claude/skills/contents-extractor/scripts/extract_diagram.py "page.png" "diagram_name" top_pct bottom_pct left_pct right_pct

# Generate diagrams (via Python import)
python3 -c "
import sys
sys.path.append('.claude/skills/diagram-generator/scripts')
from geometry_diagrams import generate_diagram
generate_diagram('circle_inscribed', {'outer_shape': 'circle', 'inner_shape': 'square', 'dimension': 9, 'output_path': 'new_images/q6.png'})
"

# Generate test PDF
python3 -c "
import sys
sys.path.append('.claude/skills/test-pdf-generator/scripts')
from test_pdf_generator import create_test_pdf
create_test_pdf(config_dict)
"
```

### Required Python Packages
```bash
pip3 install Pillow PyMuPDF pytesseract reportlab matplotlib numpy
brew install tesseract  # macOS OCR engine
```

## Architecture

### Agent Orchestration

```
/generate-test
    │
    ├─→ curriculum-analyzer         → curriculum_context.md
    │   (reads workbook, extracts formulas/methods/benchmarks)
    │
    ├─→ test-contents-extractor     → ExtractedQuestions.md + images/
    │   (extracts questions, testing aspects, captures diagrams)
    │
    └─→ curriculum-aligned-question-generator → PDF + ANSWERS.md + new_images/
        (creates FRESH questions + NEW diagrams)
```

Each agent runs SEQUENTIALLY - the orchestrator waits for each step to succeed before proceeding.

### Directory Structure
```
.claude/
├── agents/                          # Sub-agent definitions
│   ├── curriculum-analyzer.md       # Workbook analysis
│   ├── test-contents-extractor.md   # Test extraction + diagram capture
│   ├── curriculum-aligned-question-generator.md  # Fresh question creation
│   └── curriculum-test-generator.md # Main orchestrator
├── commands/                        # User-invocable slash commands
│   ├── generate-test.md            # /generate-test
│   ├── analyze-curriculum.md       # /analyze-curriculum
│   ├── extract-test.md            # /extract-test
│   └── generate-variations.md     # /generate-variations
└── skills/                         # Reusable capabilities
    ├── contents-extractor/        # PDF→images, diagram extraction, OCR
    │   └── scripts/
    │       ├── convert_pages.py   # PDF to PNG conversion
    │       ├── extract_diagram.py # Vision-guided diagram cropping
    │       └── extract_text.py    # OCR with diagram references
    ├── diagram-generator/         # Create new diagrams
    │   └── scripts/
    │       ├── geometry_diagrams.py    # Circles, 3D shapes, composite areas
    │       ├── statistics_diagrams.py  # Venn, box plots, scatter plots
    │       └── polynomial_diagrams.py  # Graphs, coordinate grids
    ├── test-pdf-generator/        # Create formatted test PDFs
    │   └── scripts/
    │       └── test_pdf_generator.py
    └── question-variation-types/  # Variation strategies for simple questions
```

### Three-Source Question Generation

Questions are generated using prioritized sources:
1. **Priority 1: Testing Aspects** (from ExtractedQuestions.md) - What concept/formula/skill is tested
2. **Priority 2: Curriculum Context** (from curriculum_context.md) - Knowledge range for enrichment
3. **Priority 3: Variation Types** - Fallback for simple questions (Type 1-4 variations)

### Diagram Type Classification

All diagram questions are classified before generation:
- **Type A (Input)**: Diagram provides given information → Create NEW diagram with different values
- **Type B (Output)**: Blank grid for student sketching → Create BLANK GRID only (not the answer!)
- **Type C (Reference)**: Partial information for annotation → Create similar partial diagram

## Key Concepts

### Testing Aspect Analysis
Each extracted question includes a "Testing Aspect" table documenting:
- Concept being tested
- Formula/theorem required
- Skill demonstrated
- Source (DIAGRAM or TEXT)

### Curriculum Alignment
Generated questions must:
- Use only formulas from curriculum_context.md
- Match taught difficulty levels
- Follow documented solution strategies
- Stay within number patterns used in workbook

### Output Files
```
[Working Directory]/
├── curriculum_context.md           # Curriculum analysis
├── ExtractedQuestions.md           # Original test with testing aspects
├── [Test]_Version_B.pdf            # Final varied test
├── [Test]_Version_B_ANSWERS.md     # Complete answer sheet
├── images/                         # Extracted original diagrams
├── new_images/                     # Generated question diagrams
├── answer_images/                  # Answer diagrams (for Type B sketch questions)
└── test_pages/                     # PDF pages as images (temporary)
```

### Resume Logic
The orchestrator checks for existing files and resumes from the appropriate step:
- `curriculum_context.md` exists → Skip curriculum analysis
- `ExtractedQuestions.md` exists → Skip test extraction
- `*_Version_B.pdf` exists → All done, present results
