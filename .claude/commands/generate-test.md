# Generate Curriculum-Aligned Test

Main command to generate a new test with curriculum-aligned variations.

## Usage
```
/generate-test [workbook_path] [test_path]
```

## Arguments
- `workbook_path`: Path to the reference workbook PDF (contains theory, formulas, worked examples)
- `test_path`: Path to the test PDF to create variations for

## What It Does
1. Analyzes curriculum from workbook → `curriculum_context.md`
2. Extracts test content and diagrams → `ExtractedQuestions.md` + `images/`
3. Generates aligned variations → New test PDF + answers + report

## Example
```
/generate-test "Year 10 Mathematics AOS 7 Revision [10.2] Workbook.pdf" "Year 10 Mathematics AOS 7 Revision [10.2] - Mock CAT 1.pdf"
```

## Output Files
- `curriculum_context.md` - Curriculum analysis
- `ExtractedQuestions.md` - Original test with testing aspects
- `images/` - Captured original diagrams
- `[Test]_Version_B.pdf` - Fresh test with new diagrams embedded
- `[Test]_Version_B_ANSWERS.md` - Complete answer sheet
- `new_images/` - Newly generated diagrams

---

## Prompt

You are the curriculum-test-generator orchestrator. Generate a curriculum-aligned test variation.

**Files provided:**
- Workbook: $ARGUMENTS (first file or identify from context)
- Test: $ARGUMENTS (second file or identify from context)

**Execute the full workflow:**

1. **Identify files** - Determine which is workbook (theory/examples) and which is test (questions)

2. **Analyze curriculum** - Call curriculum-analyzer agent:
   - Read the workbook PDF
   - Extract topics, formulas, methods, difficulty benchmarks
   - Save to `curriculum_context.md`

3. **Extract test content** - Call test-contents-extractor agent:
   - Read the test PDF
   - Extract TESTING ASPECT for each question (concept, formula, skill)
   - Capture original diagrams as images
   - Save to `ExtractedQuestions.md` + `images/`

4. **Generate fresh questions** - Call curriculum-aligned-question-generator agent:
   - Read testing aspects from ExtractedQuestions.md
   - Create FRESH questions (not just number changes) that test same concepts
   - Generate NEW diagrams for diagram questions
   - Output final PDF with embedded diagrams + answers

5. **Present results** - Show summary of all deliverables created

Execute this workflow now with the provided files.
