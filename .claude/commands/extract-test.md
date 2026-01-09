# Extract Test Contents

Sub-command to extract all questions and diagrams from a test PDF. Use for testing the test-contents-extractor agent independently.

## Usage
```
/extract-test [test_path]
```

## Arguments
- `test_path`: Path to the test PDF to extract

## What It Does
- Converts PDF pages to images (for diagram extraction)
- Reads test to extract all questions with marks
- Extracts all diagrams linked to their questions
- Creates diagram descriptions for style matching
- Produces one consolidated file with everything

## Output
- `ExtractedQuestions.md` - All questions with embedded diagram references
- `images/` - Extracted diagram image files

## Example
```
/extract-test "Year 10 Mathematics AOS 7 Revision [10.2] - Mock CAT 1.pdf"
```

---

## Prompt

You are the test-contents-extractor agent. Extract all questions and diagrams from the provided test PDF.

**Test PDF:** $ARGUMENTS

**Your task:**

1. **Convert PDF to images** for diagram extraction:
   ```bash
   python3 .claude/skills/contents-extractor/scripts/convert_pages.py \
     "[test_path]" "test_pages" 300
   ```

2. **Read the test PDF** to get question text

3. **View page images** to identify diagrams and their locations

4. **Extract each diagram** using contents-extractor skill:
   ```bash
   python3 .claude/skills/contents-extractor/scripts/extract_diagram.py \
     "test_pages/page-XX.png" "q[N]_[type]" [coords]
   ```

5. **Create ExtractedQuestions.md** with:
   - Each question's text and marks
   - Embedded diagram references: `![diagram](images/diagram_qN_type.png)`
   - Diagram descriptions (type, dimensions, style)
   - Summary table

6. **Report summary:**
   - Total questions extracted
   - Questions with diagrams
   - Diagram types found

Execute now.
