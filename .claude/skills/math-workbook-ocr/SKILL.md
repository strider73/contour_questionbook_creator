---
name: math-workbook-ocr
description: Knowledge base for OCR processing of scanned math workbooks - mathematical notation recognition, LaTeX conversion, and content structure understanding
---

# Math Workbook OCR Knowledge

## Purpose

This skill provides specialized knowledge for processing scanned math workbooks using vision-based OCR. It contains guidelines for:

- Mathematical notation recognition and LaTeX conversion
- Workbook structure understanding (questions, answers, sections)
- Image quality requirements and common OCR challenges
- Output formatting standards for educational content

**Note**: This is a knowledge skill, not an execution agent. Agents like `ocr-processor-agent` and `document-reader-agent` use this knowledge when processing workbooks.

## Core Knowledge Areas

### 1. Mathematical Content Recognition

**Common symbols and their LaTeX equivalents**:
- Multiplication: × → `\times`
- Division: ÷ → `\div`
- Pi: π → `\pi`
- Square root: √ → `\sqrt{}`
- Fractions: Use `\frac{numerator}{denominator}`
- Exponents: x² → `x^{2}`
- Subscripts: x₁ → `x_{1}`

**See [ocr-guidelines.md](ocr-guidelines.md) for comprehensive symbol reference**

### 2. Workbook Structure Patterns

**Typical workbook elements**:
- **Title pages**: Year/grade, subject, topic, workbook type
- **Section headers**: Topic names, bold/larger text
- **Question numbering**: Q1, Q2 or 1a, 1b, 1c or (i), (ii), (iii)
- **Mark allocations**: (2 marks), [3], (5 points)
- **Special labels**: "Walkthrough", "Tech Active", "Extension"

### 3. Image Quality Standards

**Recommended specifications**:
- Resolution: 300+ DPI
- Format: JPEG, PNG (RGB)
- Lighting: Even, no shadows/glare
- Orientation: Upright, properly aligned
- Clarity: Sharp focus, no blur

### 4. Output Format Standards

**Markdown structure for extracted content**:
```markdown
# [Workbook Title] - EXTRACTED

## Metadata
- Source Folder: [path]
- Total Pages: [count]
- Extraction Date: [date]

## Page 1: [Section Name]

### Questions

#### Question 1 (2 marks)
**Question**: [text]
**Math**: $equation$ or $$display\_equation$$
**Diagram**: [description]
```

## When This Knowledge Is Used

This knowledge skill is referenced by:

1. **page-reader agent** - Vision-based page scanning and math notation conversion
2. **question-answer-agent** - Question/answer separation (uses structural patterns)

## Related Resources

- **[ocr-guidelines.md](ocr-guidelines.md)** - Comprehensive OCR processing guidelines
- **page-reader agent** - Agent that applies this knowledge for math conversion
- **document-reader-agent** - Coordinates page-reader agents for extraction
