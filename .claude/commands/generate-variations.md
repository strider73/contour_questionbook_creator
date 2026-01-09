# Generate Question Variations

Sub-command to generate curriculum-aligned question variations. Use for testing the curriculum-aligned-question-generator agent independently.

**Prerequisite:** Must have `curriculum_context.md` and `ExtractedQuestions.md` already created.

## Usage
```
/generate-variations
```

## Prerequisites
- `curriculum_context.md` - From /analyze-curriculum
- `ExtractedQuestions.md` - From /extract-test
- `images/` - Extracted diagrams from /extract-test

## What It Does
- Reads curriculum context (what students learned)
- Reads extracted questions (test structure)
- Plans variation types for each question
- Generates variations aligned with curriculum
- Creates NEW diagrams for diagram questions
- Produces test PDF + answer sheet + alignment report

## Output
- `[Test]_Version_B.pdf` - New test with varied questions
- `[Test]_ANSWERS.md` - Complete answer sheet with working
- `variation_alignment_report.md` - Proof of curriculum alignment
- `images/varied_qN_[type].png` - New diagrams for varied questions

## Example
```
/generate-variations
```

---

## Prompt

You are the curriculum-aligned-question-generator agent. Generate curriculum-aligned test variations.

**Prerequisites (must exist):**
- `curriculum_context.md` - Curriculum analysis
- `ExtractedQuestions.md` - Original test content
- `images/` - Original diagrams

**Your task:**

1. **Read both context files:**
   - `curriculum_context.md` - formulas, methods, benchmarks
   - `ExtractedQuestions.md` - questions, diagrams, marks

2. **Plan variation types** for each question:
   - ~40% Type 1 (Different Numbers)
   - ~30% Type 2 (Modified Challenge)
   - ~20% Type 3 (Reverse Pattern)
   - ~10% Type 4 (Conceptual)

3. **Generate each variation:**
   - Apply question-variation-types skill
   - Verify against curriculum constraints
   - For diagram questions: read original, create NEW diagram with varied values

4. **Create outputs:**
   - Test PDF with embedded new diagrams
   - Answer sheet with complete working
   - Alignment report documenting verification

5. **Report summary:**
   - Questions varied
   - Variation type distribution
   - New diagrams created
   - Alignment status

Execute now.
