# Contour Question Book Creator

## Behind the Story

My daughter attends Contour Education, a tutoring institution in the Melbourne CBD. Every session cost close to a full Sunday — 2-3 hours in the classroom, plus roughly 4 hours round-trip by train — and about $1,200 per subject, per term. Both the money and the time were adding up, so I started asking the obvious question: what is Contour actually selling?

It isn't the curriculum. That's in any textbook, freely available. The part that's actually worth $1,200 and a lost Sunday is the **question style**. A standard textbook asks "find the area of this rectangle." A Contour test asks something like "you're building a tennis court of this size — how much land do you need, accounting for the surrounds?" Same underlying maths, transformed into a realistic, applied scenario that tests whether a student actually understands the concept, not just whether they can recall a formula.

That's the premise this project tests: if the expensive part is the *question-transformation pattern*, not the raw curriculum, an AI system that learns both — the content (what's being taught) and the pattern (how it becomes a realistic, applied question) — from real study materials should be able to reproduce that value. Give it a workbook (or a textbook scan) plus a sample of Contour-style questions, and see whether it can learn the pattern well enough to generate fresh, realistic questions on new material.

## Overview

A Claude Code-powered system for generating curriculum-aligned test variations from existing mathematics tests. Given a reference workbook (containing theory, formulas, and examples) and a test PDF, it creates fresh question variations that test the same concepts with new scenarios and diagrams.

## Features

- **Curriculum Analysis**: Extracts formulas, worked examples, and difficulty benchmarks from reference workbooks
- **Intelligent Question Extraction**: Uses OCR and vision to extract questions and diagrams from test PDFs
- **Fresh Question Generation**: Creates new questions that test the same concepts with different values and scenarios
- **Automatic Diagram Creation**: Generates new diagrams for geometry, statistics, and polynomial questions
- **PDF Output**: Produces professionally formatted test PDFs with complete answer sheets

## Quick Start

### Prerequisites

```bash
# Install required Python packages
pip3 install Pillow PyMuPDF pytesseract reportlab matplotlib numpy

# Install Tesseract OCR engine (macOS)
brew install tesseract
```

### Usage

```bash
# Full test generation pipeline
/generate-test "Workbook.pdf" "Test.pdf"

# Individual commands (for debugging)
/analyze-curriculum "Workbook.pdf"    # → curriculum_context.md
/extract-test "Test.pdf"              # → ExtractedQuestions.md + images/
/generate-variations                   # → PDF + ANSWERS.md + new_images/
```

### Output Files

```
[Working Directory]/
├── curriculum_context.md           # Curriculum analysis
├── ExtractedQuestions.md           # Original test with testing aspects
├── [Test]_Version_B.pdf            # Final varied test
├── [Test]_Version_B_ANSWERS.md     # Complete answer sheet
├── images/                         # Extracted original diagrams
├── new_images/                     # Generated question diagrams
└── answer_images/                  # Answer diagrams (for sketch questions)
```

---

# Architecture

## 1. Main Orchestrator: curriculum-test-generator

Coordinates the entire test generation workflow in SEQUENTIAL order.

**Flow:** User Inputs (Workbook PDF or textbook-scan + Test PDF) → 3 sub-agents run in sequence → Final Output

**Sub-Agents Called (in order):**

1. curriculum-analyzer → curriculum_[context.md](http://context.md)
2. test-contents-extractor → [ExtractedQuestions.md](http://ExtractedQuestions.md) + images/
3. curriculum-aligned-question-generator → PDF + [ANSWERS.md](http://ANSWERS.md) + new_images/

The orchestrator has resume logic: if `curriculum_context.md` already exists, step 1 is skipped; if `ExtractedQuestions.md` exists, step 2 is skipped; if `*_Version_B.pdf` exists, the pipeline is considered complete. See [.claude/docs/ARCHITECTURE.md](.claude/docs/ARCHITECTURE.md) for full detail.

---

![curriculum-test-generator-CURRICULUM-TEST-GENERATOR ARCHITECTURE.drawio.png](images/curriculum-test-generator-CURRICULUM-TEST-GENERATOR%20ARCHITECTURE.drawio.png)

## 2. curriculum-analyzer

Analyzes reference workbooks to extract curriculum context.

**4-Step Workflow:**

1. Read the Workbook (PDF)
2. Analyze Content Structure
3. Document Curriculum Context
4. Quality Verification

**Output:** curriculum_[context.md](http://context.md) with 8 sections (Topics, Formulas, Worked Examples, Difficulty Benchmarks, Solution Strategies, Common Patterns, Visual Diagram Patterns, Constraints)

![curriculum-test-generator-CURRICULUM-ANALYZER AGENT ARCHITECTURE.drawio.png](images/curriculum-test-generator-CURRICULUM-ANALYZER%20AGENT%20ARCHITECTURE.drawio.png)

---

## 3. test-contents-extractor

Extracts questions and diagrams from test PDF using DIAGRAM-FIRST approach.

**6-Step Workflow:**

- Step 0: Setup folders
- Step 1: Convert PDF to images
- Step 2: DIAGRAM-FIRST analysis
- Step 3: Vision-guided diagram extraction
- Step 4: OCR text extraction
- Final: Create [ExtractedQuestions.md](http://ExtractedQuestions.md)

**Diagram Classification:**

- Type A (Input): Student needs to answer
- Type B (Output): Student must create
- Type C (Reference): Context only

**Skills:** contents-extractor (convert_[pages.py](http://pages.py), extract_[diagram.py](http://diagram.py), extract_[text.py](http://text.py))

---

![curriculum-test-generator-TEST-CONTENTS-EXTRACTOR AGENT ARCHITECTURE.drawio.png](images/curriculum-test-generator-TEST-CONTENTS-EXTRACTOR%20AGENT%20ARCHITECTURE.drawio.png)

## 4. curriculum-aligned-question-generator

Generates FRESH test questions based on testing aspects.

**3 Priority Sources:**

1. [ExtractedQuestions.md](http://ExtractedQuestions.md) (testing aspects)
2. curriculum_[context.md](http://context.md) (knowledge range)
3. question-variation-types skill (fallback)

**8-Step Workflow:**

1. Create folders → 1. Read inputs → 2. Process questions → 3. Generate NEW diagrams → 4. Build test → 5. Answer images → 6. [ANSWERS.md](http://ANSWERS.md) → 7. Final PDF

**Skills:** diagram-generator, test-pdf-generator, question-variation-types

---

![curriculum-test-generator-CURRICULUM-ALIGNED-QUESTION-GENERATOR ARCHITECTURE.drawio.png](images/curriculum-test-generator-CURRICULUM-ALIGNED-QUESTION-GENERATOR%20ARCHITECTURE.drawio.png)

## Question Format Pattern Library

`question_format_patterns.md` grows as a byproduct of running the pipeline, not as a separate orchestrated step. Each generated question is checked against the existing pattern library — new formats get added, existing ones are reused.

**Existing Patterns:** Direct Recall, Calculation, Show/Prove, Solve Equation, Graph Sketch, Graph Reading, Context Translation, Multi-Part, Real-World Model, ... (grows over time)

![curriculum-test-generator-Extract Question Format Patterns .drawio.png](images/curriculum-test-generator-Extract%20Question%20Format%20Patterns%20.drawio.png)

---

## Summary

| Component | Input | Output |
| --- | --- | --- |
| curriculum-test-generator | Workbook + Test PDF | Final test + answers |
| curriculum-analyzer | Workbook PDF | curriculum_[context.md](http://context.md) |
| test-contents-extractor | Test PDF | [ExtractedQuestions.md](http://ExtractedQuestions.md) + images/ |
| curriculum-aligned-question-generator | Both above | PDF + [ANSWERS.md](http://ANSWERS.md) + new_images/ |