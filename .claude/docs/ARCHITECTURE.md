# Contour Question Book Creator - Architecture

## Overview

This system generates curriculum-aligned test variations from existing mathematics tests. Given a reference workbook and a test PDF, it creates fresh question variations that test the same concepts with new scenarios and diagrams.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         CMD: /generate-test                                  │
│                    "Workbook.pdf" "Test.pdf"                                │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                 AGENT: curriculum-test-generator                             │
│                      (Main Orchestrator)                                     │
│                                                                              │
│   Runs 3 sub-agents SEQUENTIALLY (waits for each to complete)               │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌───────────────────────────────────────────────────────────────────────────┐
│  STEP 1                                                                    │
│  ┌───────────────────┐                                                     │
│  │ AGENT:            │         ┌───────────────────┐                       │
│  │ curriculum-       │ ──────► │ FILE: (CREATED)   │                       │
│  │ analyzer          │         │ curriculum_       │                       │
│  │                   │         │ context.md        │                       │
│  │ SKILLS:           │         │                   │                       │
│  │ • math-workbook-  │         │ (~1000-2000 lines │                       │
│  │   ocr             │         │  for single AOS)  │                       │
│  └───────────────────┘         └───────────────────┘                       │
└───────────────────────────────────────────────────────────────────────────┘
                                    │
                                then ▼
┌───────────────────────────────────────────────────────────────────────────┐
│  STEP 2                                                                    │
│  ┌───────────────────┐                                                     │
│  │ AGENT:            │         ┌───────────────────┐                       │
│  │ test-contents-    │ ──────► │ FILE: (CREATED)   │                       │
│  │ extractor         │         │ ExtractedQuestions│                       │
│  │                   │         │ .md               │                       │
│  │ SKILLS:           │         │                   │                       │
│  │ • contents-       │         │ + images/         │                       │
│  │   extractor       │         │   (extracted      │                       │
│  │ • math-workbook-  │         │    diagrams)      │                       │
│  │   ocr             │         └───────────────────┘                       │
│  └───────────────────┘                                                     │
└───────────────────────────────────────────────────────────────────────────┘
                                    │
                                then ▼
┌───────────────────────────────────────────────────────────────────────────┐
│  STEP 3                          ▲ feeds                                   │
│  ┌───────────────────────────┐   │ (from Steps 1 & 2)                      │
│  │ AGENT:                    │   │                                         │
│  │ curriculum-aligned-       │ ◄─┘  ┌───────────────────────────┐          │
│  │ question-generator        │      │ FILES: (CREATED)          │          │
│  │                           │ ───► │ • [Test]_Version_B.pdf    │          │
│  │ SKILLS:                   │      │ • [Test]_ANSWERS.md       │          │
│  │ • question-variation-     │      │ • new_images/*.png        │          │
│  │   types                   │      └───────────────────────────┘          │
│  │ • diagram-generator       │                                             │
│  │ • test-pdf-generator      │                                             │
│  └───────────────────────────┘                                             │
└───────────────────────────────────────────────────────────────────────────┘
```

---

## Key Design Principles

| Principle | Description |
|-----------|-------------|
| **Sequential Execution** | Orchestrator waits for each step to complete before next |
| **Skills Inside Agents** | Skills are capabilities used BY agents, not separate entities |
| **Fresh Analysis** | Each test generation analyzes workbook fresh (no pre-compiled database) |
| **Created vs Reusable** | Output files are CREATED each time; Python scripts are REUSABLE |

---

## Agent Details

### AGENT: curriculum-analyzer (Step 1)

**Purpose:** Analyze workbook to extract curriculum context

**Input:** Workbook PDF (e.g., "Year 10 AOS 7 Workbook.pdf")

**Output:** `curriculum_context.md` (CREATED)

**Contains:**
- Topics covered
- Formulas and theorems
- Worked examples
- Difficulty benchmarks
- Solution strategies
- Common number patterns

---

### AGENT: test-contents-extractor (Step 2)

**Purpose:** Extract questions and diagrams from existing test

**Input:** Test PDF (e.g., "Mock_CAT_1.pdf")

**Output:**
- `ExtractedQuestions.md` (CREATED)
- `images/` folder with extracted diagrams (CREATED)

**Each question includes:**
- Question text
- Testing aspect (what concept/skill is tested)
- Diagram reference (if applicable)
- Mark allocation

---

### AGENT: curriculum-aligned-question-generator (Step 3)

**Purpose:** Generate fresh questions using 3-source priority system

**Inputs:**
- `curriculum_context.md` (from Step 1)
- `ExtractedQuestions.md` (from Step 2)

**Output:**
- `[Test]_Version_B.pdf` (CREATED)
- `[Test]_ANSWERS.md` (CREATED)
- `new_images/*.png` (CREATED)

**3-Source Priority:**
1. **Testing Aspects** (from ExtractedQuestions.md) - What to test
2. **Curriculum Context** (from curriculum_context.md) - Knowledge boundaries
3. **Variation Types** (from skill) - How to vary simple questions

---

## Skill Internal Processes

### SKILL: question-variation-types

```
┌─────────────────────────────────────────────────────────────┐
│              Question Variation Process                      │
└─────────────────────────────────────────────────────────────┘
                          │
                          ▼
              ┌───────────────────────┐
              │ Select Variation Type │
              └───────────────────────┘
                          │
        ┌─────────┬───────┼───────┬─────────┬─────────┐
        ▼         ▼       ▼       ▼         ▼         │
   ┌─────────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────────┐   │
   │ Type 1  │ │Type2│ │Type3│ │Type4│ │ Type 5  │   │
   │Different│ │Add  │ │Work │ │New  │ │Construct│   │
   │Numbers  │ │Cmplx│ │Back │ │Cntxt│ │& Calcul │   │
   │ (~35%)  │ │(25%)│ │(15%)│ │(10%)│ │ (~15%)  │   │
   └─────────┘ └─────┘ └─────┘ └─────┘ └─────────┘   │
        │         │       │       │         │         │
        └─────────┴───────┴───────┴─────────┴─────────┘
                          │
                          ▼
              ┌───────────────────────┐
              │ Apply Real-Life       │
              │ Context Layer?        │
              └───────────────────────┘
                          │
              ┌───────────┴───────────┐
              ▼                       ▼
   ┌─────────────────────┐  ┌─────────────────────┐
   │ First 2-3 questions │  │ Remaining questions │
   │ → 0% (keep abstract)│  │ → ~80% apply        │
   └─────────────────────┘  └─────────────────────┘
```

**Location:** `.claude/skills/question-variation-types/skill.md`

---

### SKILL: contents-extractor

```
┌─────────────────────────────────────────────────────────────┐
│               PDF Extraction Pipeline                        │
└─────────────────────────────────────────────────────────────┘
                          │
                          ▼
              ┌───────────────────────┐
              │ Input: Test PDF       │
              └───────────────────────┘
                          │
                          ▼
              ┌───────────────────────┐
              │ convert_pages.py      │
              │ PDF → PNG (300 DPI)   │
              │ Uses: PyMuPDF         │
              └───────────────────────┘
                          │
                          ▼
              ┌───────────────────────┐
              │ test_pages/*.png      │
              │ (CREATED)             │
              └───────────────────────┘
                          │
          ┌───────────────┴───────────────┐
          ▼                               ▼
┌───────────────────────┐    ┌───────────────────────┐
│ extract_diagram.py    │    │ extract_text.py       │
│ Vision-guided crop    │    │ OCR with Tesseract    │
│ Uses: PIL             │    │ Uses: pytesseract     │
└───────────────────────┘    └───────────────────────┘
          │                               │
          ▼                               ▼
┌───────────────────────┐    ┌───────────────────────┐
│ images/*.png          │    │ ExtractedQuestions.md │
│ (CREATED)             │    │ (CREATED)             │
└───────────────────────┘    └───────────────────────┘
```

**Scripts Location:** `.claude/skills/contents-extractor/scripts/`

---

### SKILL: diagram-generator

```
┌─────────────────────────────────────────────────────────────┐
│               Diagram Generation                             │
└─────────────────────────────────────────────────────────────┘
                          │
                          ▼
              ┌───────────────────────┐
              │ Determine Diagram     │
              │ Type Needed           │
              └───────────────────────┘
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
┌───────────────┐ ┌───────────────┐ ┌───────────────┐
│ geometry_     │ │ statistics_   │ │ polynomial_   │
│ diagrams.py   │ │ diagrams.py   │ │ diagrams.py   │
│               │ │               │ │               │
│ • Circles     │ │ • Venn        │ │ • Cubic       │
│ • 3D shapes   │ │ • Box plots   │ │ • Quartic     │
│ • Composite   │ │ • Scatter     │ │ • Coord grid  │
│ • Triangles   │ │ • Histograms  │ │ • Parabolas   │
└───────────────┘ └───────────────┘ └───────────────┘
        │                 │                 │
        └─────────────────┴─────────────────┘
                          │
                          ▼
              ┌───────────────────────┐
              │ new_images/*.png      │
              │ (CREATED)             │
              └───────────────────────┘
```

**Scripts Location:** `.claude/skills/diagram-generator/scripts/`

All scripts use **matplotlib** for rendering.

---

### SKILL: test-pdf-generator

```
┌─────────────────────────────────────────────────────────────┐
│               PDF Generation                                 │
└─────────────────────────────────────────────────────────────┘
                          │
                          ▼
              ┌───────────────────────┐
              │ Input: Config JSON    │
              │ (questions, marks,    │
              │  images, styling)     │
              └───────────────────────┘
                          │
                          ▼
              ┌───────────────────────┐
              │ test_pdf_generator.py │
              │ (REUSABLE script)     │
              │                       │
              │ Uses: ReportLab       │
              └───────────────────────┘
                          │
                          ▼
              ┌───────────────────────┐
              │ [Test]_Version_B.pdf  │
              │ (CREATED)             │
              └───────────────────────┘
```

**Script Location:** `.claude/skills/test-pdf-generator/scripts/test_pdf_generator.py`

---

## Diagram Type Classification

For diagram questions, classify before generation:

| Type | Description | Action |
|------|-------------|--------|
| **Type A (Input)** | Diagram provides given information | Create NEW diagram with different values |
| **Type B (Output)** | Blank grid for student sketching | Create BLANK GRID only (not the answer!) |
| **Type C (Reference)** | Partial information for annotation | Create similar partial diagram |

---

## File Structure

```
[Working Directory]/
├── curriculum_context.md        (CREATED) - Curriculum analysis
├── ExtractedQuestions.md        (CREATED) - Original test with testing aspects
├── [Test]_Version_B.pdf         (CREATED) - Final varied test
├── [Test]_Version_B_ANSWERS.md  (CREATED) - Complete answer sheet
├── images/                      (CREATED) - Extracted original diagrams
├── new_images/                  (CREATED) - Generated question diagrams
├── answer_images/               (CREATED) - Answer diagrams (Type B sketches)
└── test_pages/                  (CREATED) - PDF pages as images (temporary)
```

---

## Script Paths Reference

| Script | Location | Purpose |
|--------|----------|---------|
| `convert_pages.py` | `.claude/skills/contents-extractor/scripts/` | PDF → PNG conversion |
| `extract_diagram.py` | `.claude/skills/contents-extractor/scripts/` | Vision-guided diagram cropping |
| `extract_text.py` | `.claude/skills/contents-extractor/scripts/` | OCR with diagram references |
| `geometry_diagrams.py` | `.claude/skills/diagram-generator/scripts/` | Circles, 3D shapes, composite |
| `statistics_diagrams.py` | `.claude/skills/diagram-generator/scripts/` | Venn, box plots, scatter |
| `polynomial_diagrams.py` | `.claude/skills/diagram-generator/scripts/` | Graphs, parabolas, grids |
| `test_pdf_generator.py` | `.claude/skills/test-pdf-generator/scripts/` | ReportLab PDF generation |

---

## Input Methods

### Scenario A: With Contour Workbook (Default)

```bash
/generate-test "ContourWorkbook.pdf" "Test.pdf"
```

Use full Contour workbook PDF as curriculum reference.

### Scenario B: Without Workbook (Textbook Scan)

When no Contour workbook exists, scan these 3 sections from textbook:

```
textbook-scan/
├── Summary section      → Chapter mind map (formulas, concepts)
├── Checklist section    → "I can..." success criteria
└── Review section       → Short answer, MCQ, extended response examples
```

```bash
/generate-test "textbook-scan/" "Test.pdf"
```

---

## Resume Logic

The orchestrator checks for existing files and resumes appropriately:

| If exists... | Then skip... |
|--------------|--------------|
| `curriculum_context.md` | Step 1 (curriculum analysis) |
| `ExtractedQuestions.md` | Step 2 (test extraction) |
| `*_Version_B.pdf` | All done - present results |

---

## Legend

| Symbol | Meaning |
|--------|---------|
| `(CREATED)` | File generated fresh each run |
| `(REUSABLE)` | Script used but not modified |
| `AGENT:` | Sub-agent that performs task |
| `SKILL:` | Capability/knowledge used by agent |
| `FILE:` | Input or output file |
| `CMD:` | User command |
