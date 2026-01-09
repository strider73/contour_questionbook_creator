# Analyze Curriculum

Sub-command to analyze a workbook and extract curriculum context. Use for testing the curriculum-analyzer agent independently.

## Usage
```
/analyze-curriculum [workbook_path]
```

## Arguments
- `workbook_path`: Path to the reference workbook PDF

## What It Does
- Reads the workbook PDF directly
- Extracts all topics and subtopics
- Documents all formulas and theorems (LaTeX format)
- Analyzes worked examples with solution methods
- Creates difficulty benchmarks (basic/intermediate/advanced)
- Documents solution strategies taught

## Output
- `curriculum_context.md` - Comprehensive curriculum analysis

## Example
```
/analyze-curriculum "Year 10 Mathematics AOS 7 Revision [10.2] Workbook.pdf"
```

---

## Prompt

You are the curriculum-analyzer agent. Analyze the provided workbook to extract comprehensive curriculum context.

**Workbook:** $ARGUMENTS

**Your task:**

1. **Read the workbook PDF** using the Read tool

2. **Extract and document:**
   - All topics and subtopics (Section 1)
   - All formulas and theorems with LaTeX (Section 2)
   - Worked examples with full solution methods (Section 3)
   - Difficulty benchmarks with concrete examples (Section 4)
   - Solution strategies taught (Section 5)
   - Number patterns and formats used (Section 6)
   - Diagram types described in text (Section 7)
   - Constraints for question variations (Section 8)

3. **Save output** to `curriculum_context.md`

4. **Report summary:**
   - Total topics extracted
   - Total formulas documented
   - Total worked examples analyzed
   - Difficulty distribution

This is a TEXT-BASED analysis. No images needed - describe everything in words so the question generator can reference it.

Execute now.
