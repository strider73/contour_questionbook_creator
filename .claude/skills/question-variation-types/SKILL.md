---
name: question-variation-types
description: Library of question variation strategies (Types 1-5) plus Real-Life Context Layer for creating practice questions that test true understanding. Types define mathematical variation approaches; Real-Life Context Layer wraps questions in real-world scenarios where students must extract information from context.
---

# Question Variation Types - Strategy Library

## Purpose

This skill provides a library of variation strategies for generating practice questions from original workbook questions. It helps create variations that test true understanding, not just memorization.

**Used by**: `question-answer-agent` when generating PRACTICE.md files

---

## 📝 EDITABLE LIBRARY

**This is a living document - update it as you discover better approaches!**

You can:
- ✏️ Add new variation types (Type 5, 6, 7...)
- ✏️ Modify existing types based on what works for your student
- ✏️ Adjust percentages and guidelines
- ✏️ Update examples to be more relevant
- ✏️ Remove types that don't test understanding effectively

---

## Core Principle

**Goal**: Create variations that test understanding, not just memorization

**Rule**: Generate **1 variation per original question**, choosing the BEST type to test the concept

---

## Variation Types

### Type 1: Different Numbers (Same Structure)

**When to use**:
- Basic calculation questions
- Simple data analysis
- Building confidence with familiar patterns
- Student needs practice with mechanics

**Approach**:
- Keep question structure **IDENTICAL** to original
- Change **ONLY the numerical values**
- Ensure new values create reasonable answers
- Maintain **exact same difficulty** level
- Same number of steps required

**Example**:
```markdown
Original: Calculate the range of {5, 1, 9, 12, 3, 8}
Variation: Calculate the range of {7, 2, 11, 15, 4, 9}
```

**Diagram rule**: If original has diagram, variation uses same diagram

---

### Type 2: Modified Challenge (Add Complexity)

**When to use**:
- Student shows mastery of basic concept
- Ready for slight extension of thinking
- Combining related concepts already learned
- Pushing beyond comfort zone (but still achievable)

**Approach**:
- Add **one additional requirement** (not multiple!)
- Combine with related concept student should know
- Increase data size or steps **slightly**
- Still achievable at same grade level
- Don't double the difficulty - just extend it

**Example**:
```markdown
Original: Calculate the range of {5, 1, 9, 12, 3, 8}
Variation: Calculate the range AND interquartile range (IQR) of {4, 2, 8, 15, 6, 11, 3, 9}
```

**Diagram rule**: If original has diagram, variation uses same diagram (may reference additional parts)

---

### Type 3: Reverse Pattern (Work Backwards)

**When to use**:
- Testing true understanding of relationships
- Moving beyond formula application
- Checking if student understands the "why" not just the "how"
- Deeper comprehension needed

**Approach**:
- Give the answer, ask for the input
- Work backwards from result
- Test inverse understanding
- Requires reasoning, not just calculation
- Student must understand relationship between variables

**Example**:
```markdown
Original: Calculate the range of {5, 1, 9, 12, 3, 8}
Variation: A data set has a range of 15 and a minimum value of 3. What is the maximum value?
```

**Diagram rule**: If original has diagram, variation may use diagram differently (e.g., "Given this diagram with range=15...")

---

### Type 4: Conceptual Application (Different Context)

**When to use**:
- Testing whether student understands concept vs. memorized procedure
- Checking if they can apply knowledge to new situations
- Real-world application needed
- Compare/contrast understanding

**Approach**:
- Apply same concept to new scenario
- Compare or contrast options
- Test conceptual understanding
- May change format (multiple choice, comparison, real-world context)
- Ask "why" or "explain your reasoning"

**Example**:
```markdown
Original: Calculate the range of {5, 1, 9, 12, 3, 8}
Variation: Which data set has the larger range?
- Set A: {3, 7, 11, 15}
- Set B: {5, 8, 10, 14, 18}
Explain your reasoning.
```

**Diagram rule**: If original has diagram, variation may use similar diagram type in different context

---

### Type 5: Construct & Calculate (No Diagram Given)

**When to use**:
- Testing visualization and spatial reasoning skills
- Checking if student truly understands shape properties
- Composite shapes (cylinders + cones, prisms + pyramids, etc.)
- Multi-step problems requiring geometric reasoning
- Student needs practice translating text descriptions to diagrams
- Assessing deeper understanding beyond "plug into formula"

**Approach**:
- Provide **text description only** - NO diagram given
- Include a real-world context (rocket, building, container, etc.)
- Give some dimensions directly, others must be calculated
- Require student to **draw and label** the diagram first (Part a)
- Break into sub-parts: draw → find missing dimension → calculate
- Use Pythagorean theorem or algebra to find hidden dimensions
- Final part asks for volume, surface area, or total surface area

**Structure Template**:
```markdown
**a)** Draw a labeled diagram showing all given dimensions. [1 mark]
**b)** Calculate [missing dimension using given relationships]. [1 mark]
**c)** Find [another derived measurement]. [1 mark]
**d)** Calculate the [total volume/TSA/area]. [2 marks]
```

**Example**:
```markdown
Original: A cylinder has radius 4 cm and height 10 cm. Calculate its volume.

Variation:
## The Rocket Model

A model rocket consists of a cylindrical body with a conical nose on top. The cylinder has a radius of 3 cm and a height that is unknown. The cone has the same radius as the cylinder and a slant height of 5 cm. The total height of the entire rocket is 22 cm.

**a)** Draw a labeled diagram of the rocket showing all given dimensions. [1 mark]

**b)** Calculate the perpendicular height of the cone. [1 mark]

**c)** Find the height of the cylindrical body. [1 mark]

**d)** Calculate the total volume of the rocket model. [2 marks]
```

**Common Composite Shape Scenarios**:
- Rocket/Missile: Cylinder + Cone
- Silo/Barn: Cylinder + Hemisphere
- House/Shed: Rectangular prism + Triangular prism (roof)
- Ice cream cone: Cone + Hemisphere
- Capsule/Pill: Cylinder + 2 Hemispheres
- Trophy/Cup: Cone (inverted) + Cylinder
- Storage tank: Cylinder + 2 Cones (ends)

**Diagram rule**: **NO diagram provided** - student must draw it themselves. Answer key should include the correct labeled diagram.

**Mark allocation guideline**:
- Drawing diagram: 1 mark
- Each intermediate calculation: 1 mark
- Final volume/TSA calculation: 2 marks (method + answer)

---

## Real-Life Context Layer

### What It Is

**Real-Life Context is NOT a variation type** - it is a **presentation layer** that wraps any Type 1-5 variation in a real-world scenario.

**Key Difference:**
- **Variation Types (1-5)**: Change the mathematical structure or approach
- **Real-Life Context Layer**: Changes how numbers/information are presented (embedded in scenario vs. given directly)

### Purpose

When Real-Life Context is applied:
- Numbers are **NOT given directly** in the question
- Student must **read and comprehend** the scenario first
- Student must **extract relevant information** from context
- Tests **comprehension + mathematical skill** together

### Two-Step Process

```
Original Question
      ↓
Step 1: Apply Variation Type (1-5)
      ↓
Step 2: Apply Real-Life Context Layer (if applicable)
      ↓
Final Question
```

**Example Flow:**
```
Original: "A circle has radius 10 cm. A chord is 6 cm from centre. Find chord length."

Step 1 - Apply Type 1 (Different Numbers):
"A circle has radius 12 cm. A chord is 5 cm from centre. Find chord length."

Step 2 - Apply Real-Life Context:
"A circular swimming pool has a radius of 12 metres. A lane rope is
stretched across the pool as a straight chord, positioned 5 metres
from the centre of the pool. Find the length of the lane rope."
```

### Application Rules

| Section | Real-Life Context | Reason |
|---------|-------------------|--------|
| **First 2-3 questions** | ❌ **0%** - Keep abstract | Test basic concepts directly |
| **Remaining questions** | ✅ **~80%** apply | Test comprehension + math |
| **Priority** | Diagram questions > Text questions | Visual scenarios more impactful |

### When to Apply (Decision Tree)

```
Is this in the first 2-3 questions of a section?
  → YES: Do NOT apply Real-Life Context (keep abstract)
  → NO: Continue...

Does this question have a diagram?
  → YES: HIGH priority for Real-Life Context
  → NO: MEDIUM priority for Real-Life Context

Random selection (aim for ~80% of remaining questions)
  → APPLY: Wrap in real-world scenario
  → SKIP: Keep abstract/direct
```

### Real-Life Context Examples by Topic

| Topic | Abstract Version | Real-Life Context Version |
|-------|------------------|---------------------------|
| **Chord theorem** | "A circle has radius r, chord is d from centre..." | "A circular swimming pool... lane rope stretched across..." |
| **Circle angles** | "Points A, B, C, D lie on a circle. ∠AOB = 124°..." | "A circular stadium has spectators at positions A, B, C, D on the boundary..." |
| **Tangent-secant** | "PT is tangent to circle at T. Line from P intersects at Q, R..." | "A footpath touches a circular pond at point T (tangent)..." |
| **Trigonometry** | "A rope of length 18m makes angle 42° with vertical..." | "A rescue helicopter hovers above. Its rope, extended at 42° to vertical..." |
| **Sine/Cosine rule** | "In triangle ABC, angle A = 42°, angle B = 73°, BC = 15m..." | "A surveyor measures a triangular paddock. From corner A..." |
| **Surface area** | "A cylinder has radius 5m and height 12m..." | "A farmer needs to paint a cylindrical grain silo..." |
| **Volume** | "A square pyramid has base 8m and slant height 10m..." | "A shopping centre has a pyramid-shaped glass skylight..." |
| **Sine graphs** | "Use the graph to find θ when sin θ = 0.5..." | "A Ferris wheel's height varies with rotation. Use the graph..." |

### Diagram Handling with Real-Life Context

When Real-Life Context is applied to a diagram question:
1. **Create NEW diagram** that matches the real-world scenario
2. Include visual elements (water for pool, grass for park, etc.)
3. Label with context-appropriate terms (lane rope, footpath, etc.)
4. Keep mathematical elements clear and measurable

### What Real-Life Context Does NOT Change

- The mathematical concept being tested
- The difficulty level
- The numerical values (unless also applying Type 1)
- The solution method
- The mark allocation

---

## Selecting Variation Type

### Decision Framework

**For each question, choose ONE type based on**:

1. **Question complexity**:
   - Simple calculations → Type 1
   - Multi-step problems → Type 1 or 2
   - Conceptual questions → Type 3 or 4

2. **Learning goal**:
   - Procedural practice → Type 1 or 2
   - Conceptual understanding → Type 3 or 4
   - Problem-solving skills → Type 2 or 3

3. **Student readiness**:
   - Building confidence → Type 1
   - Testing mastery → Type 2-4
   - Challenging thinking → Type 3 or 4

### Distribution Guideline

**Across all questions in a workbook, aim for approximately**:

- **~35% Type 1** (different numbers) - Build confidence and mechanical practice
- **~25% Type 2** (modified challenge) - Extend thinking slightly
- **~15% Type 3** (reverse pattern) - Test deep understanding
- **~10% Type 4** (conceptual) - Apply to new contexts
- **~15% Type 5** (construct & calculate) - Visualization and multi-step reasoning

**Note**: These are guidelines, not strict rules. Adjust based on:
- Student's current level
- Difficulty of original questions
- Time since concept was taught
- Student's confidence with topic
- **Type 5 works best for geometry/measurement topics**

---

## CRITICAL: Diagram Handling (Inline Creation)

### Diagram Creation Strategy by Variation Type

| Type | When to Create | Strategy | Example |
|------|----------------|----------|---------|
| **Type 1** | Never | Reuse original diagram | Square 14cm → Square 20cm (same diagram reused) |
| **Type 2** | **ALWAYS** | **CREATE NEW inline** | Square → Rectangle (new diagram created during question generation) |
| **Type 3** | Never | Reuse original diagram | Circle segment (backwards question, same diagram) |
| **Type 4** | **ALWAYS** | **CREATE NEW inline** | Circle → Ellipse (new diagram created during question generation) |
| **Type 5** | **ANSWER ONLY** | **NO diagram in question, CREATE for answer key** | Text description → Student draws → Answer key shows correct diagram |

### Implementation Details

**When**: During variation generation in question-answer-agent (Step 2)

**How**:
1. Generate variation question using this skill (question-variation-types)
2. **IF Type 2 or Type 4 AND original had diagram**:
   - Extract parameters from variation question text
   - Call diagram_utils.py to create new PNG file
   - Update markdown reference to new file: `images/diagram_q3_var_square20cm.png`
3. **ELSE (Type 1 or Type 3)**:
   - Keep original diagram reference unchanged: `images/diagram_page02_geometry.png`

**Result**: PRACTICE.md and ANSWERS.md have correct diagram references from the start (no post-processing needed)

---

## Domain-Specific Guidelines

### For Statistics/Data Questions

**Type 1**: Change data values, keep set size
**Type 2**: Add quartiles, IQR, standard deviation to basic questions
**Type 3**: Given mean and median, find possible data set
**Type 4**: Compare two data sets, which is more variable?

### For Probability Questions

**Type 1**: Different objects/scenarios, same probability structure
**Type 2**: Add "and then" or conditional probability
**Type 3**: Given probability, what's the sample space?
**Type 4**: Real-world scenarios (games, weather, sports)

### For Algebra Questions

**Type 1**: Different coefficients, same equation structure
**Type 2**: Add verification step or check answer
**Type 3**: Given solution, find the equation
**Type 4**: Word problems with real-world context

### For Geometry Questions

**Type 1**: Different measurements, same shape
**Type 2**: Add perimeter/area when only one was asked
**Type 3**: Given area, find dimensions
**Type 4**: Compare shapes, which has larger area/perimeter?
**Type 5**: Composite shapes described in text only - student draws, finds missing dimensions, calculates volume/TSA

**Type 5 Geometry Scenarios**:
| Real-World Context | Shapes Combined | Hidden Dimension |
|--------------------|-----------------|------------------|
| Rocket/Missile | Cylinder + Cone | Cone height (use Pythagorean with slant height) |
| Grain Silo | Cylinder + Hemisphere | Total height minus radius = cylinder height |
| House/Barn | Rectangular prism + Triangular prism | Roof height from total height |
| Ice Cream | Cone + Hemisphere | Hemisphere radius = cone radius |
| Pill/Capsule | Cylinder + 2 Hemispheres | Cylinder length = total - 2×radius |
| Water Tank | Cylinder + 2 Cones | Cone heights from slant height |
| Pencil | Cylinder + Cone (tip) | Cone height from slant height |
| Trophy Cup | Inverted cone + Cylinder base | Various from total height |

---

## Adding New Variation Types

**To add Type 5, 6, etc.:**

1. Define clear "When to use" criteria
2. Describe the approach clearly
3. Provide concrete examples
4. Specify diagram handling rules
5. Update "Distribution Guideline" percentages
6. Test with real questions first

**Template for new types**:

```markdown
### Type X: [Name of Approach]

**When to use**:
- [Situation 1]
- [Situation 2]

**Approach**:
- [Step 1]
- [Step 2]

**Example**:
```
Original: [example]
Variation: [example]
```

**Diagram rule**: [how diagrams are handled]
```

---

## Version History

**v1.2** (2026-01-12)
- Added **Real-Life Context Layer** documentation
- Clarified that Real-Life Context is a PRESENTATION LAYER, not a variation type
- Added two-step process: (1) Apply Type 1-5, then (2) Apply Real-Life Context
- Added application rules: First 2-3 questions = 0%, remaining = ~80%
- Added priority rule: Diagram questions > Text questions
- Added Real-Life Context examples table by topic
- Added decision tree for when to apply

**v1.1** (2026-01-11)
- Added Type 5: Construct & Calculate (No Diagram Given)
- Student must draw diagram from text description
- Ideal for composite 3D shapes (rockets, silos, capsules, etc.)
- Updated distribution guidelines to include Type 5 (~15%)
- Added Type 5 geometry scenarios table

**v1.0** (2025-12-29)
- Initial library with 4 variation types
- Type 1: Different Numbers
- Type 2: Modified Challenge
- Type 3: Reverse Pattern
- Type 4: Conceptual Application

**Future updates**: Add new types here as you develop better strategies!

---

## Related Resources

- **question-answer-agent** - Uses this skill to generate PRACTICE.md files
- **math-workbook-ocr** - OCR and LaTeX knowledge for mathematical content
