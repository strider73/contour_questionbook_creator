# Contour Education Test Generator

Generate professional mathematics tests in Contour Education format from scanned textbook materials.

## Scope

**This skill handles ONE workflow only:**
- Input: Scanned textbook pages (chapter objectives + review questions)
- Output: New Contour-format Mock CAT PDF

**For creating variations of existing Contour tests**, use the `curriculum-test-generator` agent instead (handles workbook + mock test PDFs).

---

## Input Requirements

Scanned textbook pages (JPEG/PNG/PDF) containing:

1. **Chapter Objectives / Study Goals** - What students should learn
   - List of skills and concepts covered
   - Key formulas and theorems introduced

2. **Chapter Review Questions / Practice Exercises** - Sample question types
   - Types of problems students need to solve
   - Difficulty range and question formats

## Output Format

### Test Structure (50 marks, 60 minutes)
- **Cover page** with Contour Education branding
- **Section A: Short Answer Questions** (36 marks) - Q1-19
- **Section B: Extended Response Questions** (14 marks) - Q20-21
- **Answer key** at the end

### Visual Elements (6-7 per test)
Include diagrams matching the topic:
- Number lines (inequalities)
- Coordinate graphs (simultaneous equations, linear functions)
- Geometric shapes with algebraic expressions
- Empty axes for student sketching
- Real-world context diagrams

---

## Workflow

### Step 1: Read Scanned Pages
Identify from the textbook scans:
- Topic name and scope
- Key concepts and formulas
- Learning objectives
- Types of questions students should master

### Step 2: Design Test Structure

```
Section A: Short Answer (36 marks)
├── Basic skills (Q1-5): 1 mark each = 5 marks
├── Intermediate (Q6-14): 1-2 marks each = ~18 marks
└── Multi-part (Q15-19): 2-4 marks each = ~13 marks

Section B: Extended Response (14 marks)
├── Comparison/Analysis (Q20): 6 marks
└── Optimization/Modeling (Q21): 8 marks
```

### Step 3: Create Questions
Map each learning objective to 1-3 questions:
- Direct computation (1 mark)
- Method-specific problems (substitution/elimination)
- Visual interpretation
- Word problems with real-world context
- Multi-step extended response

### Step 4: Generate LaTeX
Use Contour Education formatting:
```latex
% Contour Education styling
\newtcolorbox{questionbox}{...}  % Bordered question boxes
\fancyhead[L]{\textbf{\Large CONTOUR}\textsf{EDUCATION}}
\fancyhead[R]{Year 10 Mathematics}
```

### Step 5: Compile to PDF
```bash
/Library/TeX/texbin/pdflatex -interaction=nonstopmode -output-directory="[folder]" "[file].tex"
```

---

## Reference Example: Linear Equations Test

**Location**: `examples/generated_test_without_contour_pdf/Linear_Equations_Review_Test.pdf`

**Creation Log**: `examples/linear_equations_summary.md`

### Question Structure

| Question | Marks | Topic | Type |
|----------|-------|-------|------|
| Q1-4 | 1 each | Basic equation solving | Direct calculation |
| Q5 | 1 | Number line → inequality | Visual interpretation |
| Q6-7 | 1-2 | Rearranging formulas | Transposition |
| Q8 | 2 | Graph → equations, intersection | Visual + calculation |
| Q9-11 | 2 each | Simultaneous equations | Method-specific |
| Q12-14 | 2 each | Inequalities | Solve + represent |
| Q15, Q17 | 3 each | Geometry word problems | Multi-part with diagram |
| Q16 | 2 | Formula application | Real-world context |
| Q18-19 | 3-4 | Word problems | Set up + solve |
| Q20 | 6 | Cost comparison | Extended: graph + analyze |
| Q21 | 8 | Optimization | Extended: model + solve |

### Visual Elements Used

| Question | Visual Type | Description |
|----------|-------------|-------------|
| Q5 | Number line | Open circle at -2, arrow right (x > -2) |
| Q8 | Coordinate graph | Two intersecting lines L₁ and L₂ |
| Q12 | Number line | Empty line for student to draw solution |
| Q15 | Rectangle | Algebraic dimensions (2x+5) × (x+1) |
| Q17 | Isosceles triangle | Sides: (2x-1), (2x-1), (x+5) |
| Q20 | Empty axes | For sketching two cost equations |
| Q21 | Paddock diagram | Wall + three fenced sides |

### Real-World Contexts Used

1. **Phone plans** - Monthly fee + per-minute cost (Q18)
2. **Cinema tickets** - Adult vs child pricing (Q19)
3. **Car rental** - Two companies with different pricing models (Q20)
4. **Farming** - Fencing a paddock against a wall (Q21)
5. **Temperature** - Celsius to Fahrenheit conversion (Q16)

---

## Question Types by Category

### Section A (Short Answer)

| Type | Marks | Description |
|------|-------|-------------|
| Basic solve | 1 | Single equation solving |
| Transposition | 1-2 | Make variable the subject |
| Simultaneous | 2 | Substitution or elimination method |
| Inequalities | 2 | Solve and/or graph on number line |
| Word problems | 2-3 | Set up and solve equations |
| Multi-part | 3-4 | Connected sub-questions |

### Section B (Extended Response)

| Type | Marks | Description |
|------|-------|-------------|
| Comparison problem | 6 | Two scenarios, find break-even |
| Optimization/Area | 8 | Form expressions, solve, interpret |

---

## TikZ Diagrams Available

- Number lines with open/closed circles
- Coordinate grids with labeled axes
- Rectangles, triangles with dimension labels
- Function graphs (linear, intersecting lines)
- Real-world diagrams (paddocks, shapes)

---

## File Organization

```
[topic-folder]/
├── Scan.jpeg, Scan 1.jpeg, ...  (source material)
├── [Topic]_Review_Test.tex      (LaTeX source)
├── [Topic]_Review_Test.pdf      (compiled test)
└── [Topic]_Review_Test.aux/.log (LaTeX auxiliary)
```

---

## Quality Checklist

- [ ] Cover page with results table
- [ ] Questions in bordered boxes
- [ ] Marks clearly indicated per question
- [ ] 6-7 visual/diagram questions
- [ ] Mix of difficulty levels
- [ ] Real-world context problems
- [ ] Proper spacing for student answers
- [ ] Complete answer key
- [ ] Header/footer on each page

---

## Related Files

### In This Skill Folder

1. **`question_format_patterns.md`** - Question Pattern Library
   - 9 Categories of question formats
   - Pattern structure with examples

### Example Files

| File | Description |
|------|-------------|
| `examples/generated_test_without_contour_pdf/Linear_Equations_Review_Test.pdf` | Complete reference test |
| `examples/linear_equations_summary.md` | Detailed creation log |

---

## Topics Supported

| Topic | Visual Elements |
|-------|-----------------|
| Linear Equations | Number lines, coordinate graphs |
| Polynomials | Cubic/quartic curves |
| Circles | Circle diagrams |
| Statistics | Statistical displays |
| Geometry | 2D/3D shape diagrams |
