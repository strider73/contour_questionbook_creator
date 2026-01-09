# OCR Processing Guidelines for Math Workbooks

## Image Quality Requirements

### Recommended Specifications:
- **Resolution**: 300+ DPI for clear text recognition
- **Format**: JPEG, PNG (RGB color mode)
- **Lighting**: Even, natural lighting without shadows or glare
- **Orientation**: Pages should be upright and properly aligned
- **Clarity**: Sharp focus, no motion blur

### Common Issues to Avoid:
- Shadows across text or equations
- Reflective glare from glossy pages
- Skewed or rotated pages
- Low contrast (faded text)
- Incomplete pages (cut-off edges)

## Mathematical Content Challenges

### Symbols That May Be Misrecognized:

| Symbol | Common OCR Error | Correct Symbol |
|--------|------------------|----------------|
| × (multiply) | x (letter) | × or \times |
| ÷ (divide) | + or - | ÷ or \div |
| π (pi) | n or II | π or \pi |
| √ (square root) | V or / | √ or \sqrt{} |
| ≈ (approximately) | = | ≈ or \approx |
| ≤ / ≥ | < / > | ≤ or \leq / ≥ or \geq |
| ∫ (integral) | I or f | ∫ or \int |
| Σ (sigma/sum) | E | Σ or \sum |
| ∞ (infinity) | 8 or oo | ∞ or \infty |
| ° (degree) | o or 0 | ° |

### Fraction Recognition:
- **Inline fractions**: 1/2, 3/4 → May read correctly or as division
- **Stacked fractions**: More difficult, described as "numerator over denominator"
- **Mixed numbers**: 2½ → May split into "2" and "1/2"
- **LaTeX format**: Preferred output: `\frac{numerator}{denominator}`

### Exponents and Subscripts:
- **Superscripts** (x², x³): → Convert to `x^2`, `x^3` or LaTeX `x^{2}`, `x^{3}`
- **Subscripts** (x₁, a₀): → Convert to `x_1`, `a_0` or LaTeX `x_{1}`, `a_{0}`
- **Combined**: x₁² → `x_1^2` or LaTeX `x_{1}^{2}`

### Equation Recognition:
- **Simple equations**: 2x + 3 = 7 → Usually accurate
- **Complex equations**: Multi-line derivations may lose structure
- **Aligned equations**: Preserve alignment with LaTeX `align` environment if possible

## Workbook Structure Recognition

### Common Workbook Patterns:

1. **Title Pages**:
   - Year/Grade level
   - Subject name (Mathematics)
   - Topic or chapter (AOS X Revision)
   - Workbook type (Workbook, Test, Mock CAT)

2. **Section Headers**:
   - Bold or larger text
   - Often includes topic name
   - Examples: "Section A: Two-Step Experiments and Venn Diagrams"

3. **Question Numbering**:
   - Sequential: Question 1, Question 2, Q1, Q2
   - Sectioned: 1a, 1b, 1c or (i), (ii), (iii)
   - Mark allocations in parentheses: (2 marks), [3], (5 points)

4. **Special Labels**:
   - **"Walkthrough"**: Step-by-step guided problems
   - **"Tech Active"**: Requires calculator or technology
   - **"Extension"**: Advanced or challenge problems
   - **"Test/Practice"**: Indicates assessment vs. practice

5. **Answer Sections**:
   - Separate answer key pages
   - Inline answers (in boxes or different color)
   - End-of-chapter solutions

### Question Type Indicators:

- **Multiple Choice**: (A), (B), (C), (D) options
- **True/False**: T/F checkboxes or circles
- **Short Answer**: Blank lines or answer boxes
- **Long Answer/Working**: Large blank spaces with "Show working" instruction
- **Diagram-Based**: "Draw", "Sketch", "Label" instructions

## OCR Processing Workflow

### Step 1: Pre-Processing
1. Check image quality and orientation
2. Identify document structure (title, sections, pages)
3. Note any special formatting or diagrams

### Step 2: Text Extraction
1. Extract all visible text from the page
2. Preserve spatial layout (top-to-bottom, left-to-right)
3. Identify text hierarchy (headers vs. body text)

### Step 3: Mathematical Content Handling
1. Identify mathematical expressions and equations
2. Convert symbols to LaTeX or Unicode equivalents
3. Preserve equation structure (fractions, exponents, etc.)
4. Note complex notation that requires manual review

### Step 4: Diagram and Table Processing
1. Describe diagrams in detail (type, labels, key features)
2. Extract table data preserving rows and columns
3. Note graph axes, scales, and plotted data
4. Identify geometric figures and measurements

### Step 5: Structure Preservation
1. Maintain question numbering and organization
2. Preserve section divisions
3. Keep mark allocations with questions
4. Link answers to corresponding questions

### Step 6: Quality Verification
1. Scan for obvious OCR errors
2. Verify mathematical notation accuracy
3. Check for missing or duplicated content
4. Flag unclear or ambiguous text for review

## Output Format Recommendations

### Markdown Structure:

```markdown
# [Workbook Title] - EXTRACTED

## Metadata
- **Source Folder**: [folder name]
- **Total Pages**: [count]
- **Extraction Date**: [YYYY-MM-DD]
- **Quality Notes**: [any issues or warnings]

---

## Page 1: [Title or Section Name]

### Content

[Extracted text content]

### Questions

#### Question 1 (2 marks)
**Question Text**: [question]

**Mathematical Content**:
- Equation: `$2x + 3 = 7$`
- Or LaTeX: `$$\\frac{numerator}{denominator}$$`

**Diagram**: [Description if present]

**Answer Space**: [Note if working space provided]

---

## Page 2: [Next Section]

[Continue same structure...]
```

### LaTeX Formatting:

- **Inline math**: Wrap in `$...$` for inline expressions
- **Display math**: Wrap in `$$...$$` for centered equations
- **Fractions**: `\frac{a}{b}`
- **Square roots**: `\sqrt{x}` or `\sqrt[n]{x}`
- **Exponents**: `x^{2}` or `x^{n+1}`
- **Subscripts**: `x_{1}` or `a_{n}`

## Error Handling

### When OCR Confidence is Low:

1. **Flag uncertain text**: Use `[?]` or `[UNCLEAR]` markers
2. **Provide alternatives**: `number [possibly 5 or 8]`
3. **Describe instead**: "Mathematical equation (handwritten, unclear)"
4. **Note for manual review**: Add to quality notes section

### When Diagrams Are Complex:

1. **Detailed description**: Type, labels, measurements, key features
2. **Reference to scan**: "See original scan page X for diagram"
3. **Simple reproduction**: Use ASCII art for basic shapes if helpful
4. **LaTeX recreation**: For geometric figures, suggest TikZ code outline

### When Pages Are Missing or Damaged:

1. **Note the gap**: "Pages X-Y missing or unreadable"
2. **Partial extraction**: Extract what's visible
3. **Quality warning**: Flag in metadata section
4. **Suggest rescan**: Recommend better quality scan if critical

## Validation Checklist

Before finalizing extraction:

- [ ] All pages processed in correct order
- [ ] Question numbering is sequential and correct
- [ ] Mathematical symbols converted accurately
- [ ] Tables and diagrams described or extracted
- [ ] Mark allocations preserved with questions
- [ ] Section headers properly identified
- [ ] No duplicate or missing content
- [ ] Quality issues documented in metadata
- [ ] Output file properly formatted and readable

## Tips for Improvement

1. **Multiple passes**: Review extracted content 2-3 times
2. **Cross-reference**: Compare with original scans for accuracy
3. **Pattern recognition**: Learn common question formats and layouts
4. **Math verification**: Double-check complex equations and expressions
5. **Context awareness**: Use surrounding text to clarify ambiguous symbols
6. **Consistent formatting**: Maintain uniform structure across all pages
