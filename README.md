# Curriculum Test Generator - Architecture Diagrams

---

## 1. Main Orchestrator: curriculum-test-generator

Coordinates the entire test generation workflow in SEQUENTIAL order.

**Flow:** User Inputs (Workbook PDF + Test PDF) → Step 0-6 → Final Output

**Sub-Agents Called:**

- Step 2: curriculum-analyzer → curriculum_[context.md](http://context.md)
- Step 3: test-contents-extractor → [ExtractedQuestions.md](http://ExtractedQuestions.md) + images/
- Step 4: curriculum-aligned-question-generator → PDF + [ANSWERS.md](http://ANSWERS.md) + new_images/
- Step 5: Extract Question Patterns → question_format_[patterns.md](http://patterns.md)
- Step 6: Present Results

---

![curriculum-test-generator-CURRICULUM-TEST-GENERATOR ARCHITECTURE.drawio.png](attachment:a20eee71-c4a1-4a5c-8bc8-8c971195a6f3:curriculum-test-generator-CURRICULUM-TEST-GENERATOR_ARCHITECTURE.drawio.png)

## 2. curriculum-analyzer

Analyzes reference workbooks to extract curriculum context.

**4-Step Workflow:**

1. Read the Workbook (PDF)
2. Analyze Content Structure
3. Document Curriculum Context
4. Quality Verification

**Output:** curriculum_[context.md](http://context.md) with 8 sections (Topics, Formulas, Worked Examples, Difficulty Benchmarks, Solution Strategies, Common Patterns, Visual Diagram Patterns, Constraints)

![curriculum-test-generator-CURRICULUM-ANALYZER AGENT ARCHITECTURE.drawio.png](attachment:4c920126-f2b2-4421-8baf-fcad13d0015a:curriculum-test-generator-CURRICULUM-ANALYZER_AGENT_ARCHITECTURE.drawio.png)

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

![curriculum-test-generator-TEST-CONTENTS-EXTRACTOR AGENT ARCHITECTURE.drawio.png](attachment:8383481d-0198-4c0d-adab-44061ba614a7:curriculum-test-generator-TEST-CONTENTS-EXTRACTOR_AGENT_ARCHITECTURE.drawio.png)

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

![curriculum-test-generator-CURRICULUM-ALIGNED-QUESTION-GENERATOR ARCHITECTURE.drawio.png](attachment:1f0e0e84-c660-4573-8116-46ba9f1d2cc1:curriculum-test-generator-CURRICULUM-ALIGNED-QUESTION-GENERATOR_ARCHITECTURE.drawio.png)

## 5. Step 5: Extract Question Format Patterns (NEW PATTERN MANAGEMENT)

Discovers and adds NEW question format patterns to global library.

**Flow:**

1. For each question → Identify FORMAT PATTERN
2. Check: Does pattern EXIST in library?
    - YES → SKIP
    - NO → ADD to library!

**Result:** Pattern Library GROWS with each test processed.

**Existing Patterns:** Direct Recall, Calculation, Show/Prove, Solve Equation, Graph Sketch, Graph Reading, Context Translation, Multi-Part, Real-World Model, ... (grows over time)

![curriculum-test-generator-Extract Question Format Patterns .drawio.png](attachment:e48681d0-7be4-4a67-89bf-91285575045b:curriculum-test-generator-Extract_Question_Format_Patterns_.drawio.png)

---

## Summary

| Component | Input | Output |
| --- | --- | --- |
| curriculum-test-generator | Workbook + Test PDF | Final test + answers |
| curriculum-analyzer | Workbook PDF | curriculum_[context.md](http://context.md) |
| test-contents-extractor | Test PDF | [ExtractedQuestions.md](http://ExtractedQuestions.md) + images/ |
| curriculum-aligned-question-generator | Both above | PDF + [ANSWERS.md](http://ANSWERS.md) + new_images/ |
| Step 5 | [ExtractedQuestions.md](http://ExtractedQuestions.md) | question_format_[patterns.md](http://patterns.md) |