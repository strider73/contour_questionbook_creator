# Question Format Pattern Library

A reusable knowledge base for creating tests across ANY subject. Patterns are accumulated from analyzing real tests.

---

## Format Categories Quick Reference

| Category | Description | Cognitive Level | Sub-categories |
|----------|-------------|-----------------|----------------|
| **1. Direct Recall** | State/identify value from given info | Recall | 2 |
| **2. Calculation** | Apply formula/procedure | Application | 14 |
| **3. Show/Prove** | Demonstrate something is true | Application | 1 |
| **4. Solve Equation** | Find unknown value(s) | Application | 1 |
| **5. Graph Sketch** | Draw graph/diagram with features | Application/Analysis | 3 |
| **6. Graph Reading** | Extract info from given graph/diagram | Analysis | 4 |
| **7. Context Translation** | Word problem to math | Analysis | 5 |
| **8. Multi-Part Analysis** | Connected extended response | Analysis/Synthesis | 4 |
| **9. Business/Real-World Model** | Revenue, profit, modeling | Synthesis | 1 |

**Total: 9 Categories, 35 Sub-categories, 49 Patterns**

---

# Patterns by Category

---

# 1. DIRECT RECALL (2 patterns)

## 1.1 Identify Feature
*State a specific feature (intercepts, degree, zeros) from given form*

### Pattern: Identify Feature from Factored Form

**Source:** AOS 8 Mock CAT 1, Q1
**Topic:** Algebra
**Cognitive Level:** Recall

#### Pattern Structure
Given a function in factored form, state a specific feature (intercepts, zeros, degree).

#### Example from Source
> State the x-intercepts of the graph of the function y = (x - 2)(x - 3).

#### How to Create Variations
- Change the factors: (x + 1)(x - 4), (x - 5)(x + 2)
- Ask for different features: y-intercept, zeros, roots
- Use higher degree: (x - 1)(x + 2)(x - 3)
- Reverse: give intercepts, ask for equation

#### Visual Element
- Type: None
- Graph may be shown but is not required

---

## 1.2 Count/Enumerate
*Count distinct items (solutions, roots, factors)*

### Pattern: Count Distinct Solutions

**Source:** AOS 8 Mock CAT 1, Q2
**Topic:** Algebra
**Cognitive Level:** Recall

#### Pattern Structure
Given factored equation with repeated factors, count DISTINCT solutions.

#### Example from Source
> How many different solutions does (x - 3)(x + 5)(x - 2)(x + 5) = 0 have?

#### How to Create Variations
- Vary number of factors and repetitions
- Ask about multiplicity of specific root
- Mix repeated and unique factors
- Reverse: "Write equation with 2 distinct solutions, one with multiplicity 3"

#### Visual Element
- Type: None

---

# 2. CALCULATION (24 patterns)

## 2.1 Theorem Application
*Apply named theorem (Remainder, Factor)*

### Pattern: Remainder Theorem Application

**Source:** AOS 8 Mock CAT 1, Q6
**Topic:** Algebra
**Cognitive Level:** Application

#### Pattern Structure
Use remainder theorem to find remainder when polynomial is divided by linear factor.

#### Example from Source
> Use the remainder theorem to find the remainder when P(x) = 2x³ - 4x² + x - 5 is divided by (x + 1).

#### How to Create Variations
- Change polynomial coefficients
- Change divisor: (x - 2), (x + 3), (2x - 1)
- Ask follow-up: "Is this a factor?"
- Combine: find k such that remainder is zero

#### Visual Element
- Type: None

---

## 2.2 Degree/Structure Analysis
*Analyze polynomial structure*

### Pattern: Polynomial Degree Analysis

**Source:** AOS 8 Mock CAT 1, Q9
**Topic:** Algebra
**Cognitive Level:** Application

#### Pattern Structure
Given polynomials in different forms, determine degrees and degree of product.

#### Example from Source
> Let A(x) = 7x³ - 2x + 9 and B(x) = x(x - 4)²(x + 2).
> a. State the degree of x for A(x) and for B(x).
> b. Give the degree of the product A(x)B(x).

#### How to Create Variations
- Mix standard and factored forms
- Ask about sum (max of degrees) or quotient (difference)
- Include composition of polynomials
- Vary complexity of factored form

#### Visual Element
- Type: None

---

## 2.3 Measures of Center
*Mean, median, mode*

### Pattern: Calculate Mean and Median

**Source:** AOS 6 Mock CAT 2, Q3
**Topic:** Statistics
**Cognitive Level:** Application

#### Pattern Structure
Find both measures of center from a dataset.

#### Example from Source
> Find the mean and the median of the following data: 12, 9, 6, 15, 18

#### How to Create Variations
- Use odd number of values (clear median)
- Use even number (median is average of middle two)
- Include repeated values
- Make mean different from median to show skewness

#### Visual Element
- Type: None

---

## 2.4 Measures of Spread
*Range, IQR, variance, SD*

### Pattern: Calculate Range

**Source:** AOS 6 Mock CAT 2, Q1
**Topic:** Statistics
**Cognitive Level:** Application

#### Pattern Structure
Calculate a single measure of spread from a dataset.

#### Example from Source
> Calculate the range of the data set: {5, 1, 9, 12, 3, 8}

#### How to Create Variations
- Change dataset values (keep 5-10 values)
- Ask for different measures: IQR, standard deviation
- Provide ordered vs unordered data
- Include negative numbers or decimals

#### Visual Element
- Type: None

---

### Pattern: Variance and Standard Deviation

**Source:** AOS 6 Mock CAT 2, Q13
**Topic:** Statistics
**Cognitive Level:** Application

#### Pattern Structure
Calculate variance (sum of squared deviations / n), then SD.

#### Example from Source
> Data: {2, 3, 4, 7, 9}, mean = 5
> a. Calculate population variance.
> b. Find population standard deviation.

#### How to Create Variations
- Give mean vs. require calculation
- Population (÷n) vs sample (÷n-1)
- Ask for exact form vs decimal places
- Compare SDs of two datasets

#### Visual Element
- Type: None

---

## 2.5 Five-Figure Summary
*Min, Q1, Median, Q3, Max and outliers*

### Pattern: Five-Figure Summary

**Source:** AOS 6 Mock CAT 2, Q4
**Topic:** Statistics
**Cognitive Level:** Application

#### Pattern Structure
Find Min, Q₁, Median, Q₃, Max from ordered dataset.

#### Example from Source
> For the data set {10, 12, 13, 15, 17, 18, 20}, find the five-figure summary.

#### How to Create Variations
- Use 7, 9, or 11 values for clear quartiles
- Include outliers to test understanding
- Provide unordered data (must order first)
- Follow up with box plot construction

#### Visual Element
- Type: None (but often leads to box plot)

---

### Pattern: Outlier Detection Using Fences

**Source:** AOS 6 Mock CAT 2, Q10
**Topic:** Statistics
**Cognitive Level:** Analysis

#### Pattern Structure
Calculate IQR, find fences, identify values outside fence range.

#### Example from Source
> The goals scored: 3, 0, 1, 4, 2, 3, 1, 2, 5, 2
> An outlier lies outside [Q₁ - 1.5×IQR, Q₃ + 1.5×IQR]. Identify any outliers.

#### How to Create Variations
- Design with outliers (test detection)
- Design without outliers (answer: "none")
- Single outlier vs multiple
- Different contexts: test scores, temperatures, times

#### Visual Element
- Type: None

---

## 2.6 Basic Probability
*Single event, favorable/total*

### Pattern: Basic Probability

**Source:** AOS 6 Mock CAT 2, Q2
**Topic:** Probability
**Cognitive Level:** Application

#### Pattern Structure
Find probability using favorable/total outcomes.

#### Example from Source
> A die is rolled. What is the probability of rolling a number greater than 4?

#### How to Create Variations
- Different sample spaces: dice, coins, cards, spinners, balls
- Different conditions: less than, equal to, even, prime
- Express as fraction, decimal, or percentage
- Multiple events: "at least one", "both"

#### Visual Element
- Type: None (or spinner/die diagram)

---

## 2.7 Probability Rules
*Addition, multiplication, independence*

### Pattern: Addition Rule (Find Missing Probability)

**Source:** AOS 6 Mock CAT 2, Q7
**Topic:** Probability
**Cognitive Level:** Application

#### Pattern Structure
Given three of P(A), P(B), P(A∪B), P(A∩B), find the fourth.

#### Example from Source
> If P(A) = 0.6, P(B) = 0.5 and P(A ∪ B) = 0.8, find P(A ∩ B).

#### How to Create Variations
- Give different three, ask for different fourth
- Use decimals or fractions
- Include context: "sports club membership"
- Extend: find P(A only) or P(neither)

#### Visual Element
- Type: None (or Venn diagram)

---

### Pattern: Independence Test

**Source:** AOS 6 Mock CAT 2, Q8
**Topic:** Probability
**Cognitive Level:** Analysis

#### Pattern Structure
Test if P(A∩B) = P(A) × P(B) to determine independence.

#### Example from Source
> P(A) = 1/3, P(B) = 1/4, P(A ∩ B) = 1/10. Are A and B independent? Justify.

#### How to Create Variations
- Design independent events (P(A∩B) = P(A)×P(B))
- Design dependent events (P(A∩B) ≠ P(A)×P(B))
- Use fractions or decimals
- Require calculation AND written justification

#### Visual Element
- Type: None

---

### Pattern: Sequential Probability (Multiple Paths)

**Source:** AOS 6 Mock CAT 2, Q14
**Topic:** Probability
**Cognitive Level:** Analysis

#### Pattern Structure
Calculate probability requiring sum of multiple paths (order matters).

#### Example from Source
> Bag has 5 red, 3 blue marbles. Two drawn without replacement.
> What is probability of one red and one blue? (Consider both orders)

#### How to Create Variations
- With replacement vs without replacement
- "Exactly one of each" vs "at least one"
- Different objects: cards, balls, students
- Different numbers of draws

#### Visual Element
- Type: None (or tree diagram)

---

## 2.8 Line of Best Fit
*Equation from points, prediction*

### Pattern: Line of Best Fit Equation

**Source:** AOS 6 Mock CAT 2, Q12
**Topic:** Statistics
**Cognitive Level:** Application

#### Pattern Structure
Find equation of line through two given points, use for prediction.

#### Example from Source
> Line of best fit passes through (2, 60) and (6, 95).
> a. Find the equation of this line.
> b. Predict score for 3 hours study.

#### How to Create Variations
- Different point pairs
- Ask for exact and rounded forms
- Interpolation vs extrapolation prediction
- Discuss limitations of prediction

#### Visual Element
- Type: None (or scatter plot for context)

---

## 2.9 Surface Area
*SA of 3D shapes*

### Pattern: Surface Area of Basic 3D Shape

**Source:** AOS 7 Mock CAT 1, Q5
**Topic:** Geometry
**Cognitive Level:** Application

#### Pattern Structure
Apply surface area formula for basic 3D solid.

#### Example from Source
> Find the surface area of a cube with a side length of 5 cm.

#### How to Create Variations
- Different shapes: cube, rectangular prism, sphere, cylinder
- Reverse: give surface area, find dimension
- Ask for both SA and volume
- Include units in mixed form (cm and mm)

#### Visual Element
- Type: None (or 3D diagram)

---

### Pattern: Cone Surface Area (with Slant Height)

**Source:** AOS 7 Mock CAT 1, Q7
**Topic:** Geometry
**Cognitive Level:** Application

#### Pattern Structure
Calculate total or curved surface area of cone given radius and slant height.

#### Example from Source
> A cone has radius 5 cm and slant height 13 cm. Find total surface area in terms of π.

#### How to Create Variations
- Ask for curved surface only (exclude base)
- Give radius and perpendicular height (need Pythagoras first)
- Reverse: give SA and radius, find slant height
- Numerical answer vs "in terms of π"

#### Visual Element
- Type: None (or cone diagram)

---

## 2.10 Volume
*Volume of 3D shapes*

### Pattern: Hollow Cylinder Volume and Surface Area

**Source:** AOS 7 Mock CAT 1, Q13
**Topic:** Geometry
**Cognitive Level:** Analysis

#### Pattern Structure
Calculate volume and/or surface area of hollow cylinder (pipe).

#### Example from Source
> A pipe has outer diameter 8 cm, inner diameter 6 cm, length 50 cm.
> a. Find volume of metal.
> b. Find total surface area.

#### How to Create Variations
- Give radii instead of diameters
- Ask for mass given density
- Give wall thickness instead of inner diameter
- Reverse: give volume, find dimension

#### Visual Element
- Type: 3D Diagram (showing hollow structure)
- Essential: Cross-section visible, inner/outer clearly shown
- Variable: Dimensions, orientation

---

### Pattern: Prism Volume (Non-rectangular Base)

**Source:** AOS 7 Mock CAT 1, Q16
**Topic:** Geometry
**Cognitive Level:** Analysis

#### Pattern Structure
Find height/area of cross-section, then calculate prism volume.

#### Example from Source
> Triangular prism with equilateral triangle base (side 6 cm), length 10 cm.
> a. Find height of triangle.
> b. Find area of cross-section.
> c. Find volume.

#### How to Create Variations
- Different cross-sections: right triangle, isosceles, trapezoid
- Give height directly (skip Pythagoras step)
- Ask for surface area instead/also
- Reverse: give volume, find dimension

#### Visual Element
- Type: 3D Diagram
- Essential: Cross-section visible, dimensions labeled
- Variable: Cross-section shape, values

---

## 2.11 Similarity Ratios
*k, k², k³ relationships*

### Pattern: Volume Ratio to Linear Ratio

**Source:** AOS 7 Mock CAT 1, Q4
**Topic:** Geometry
**Cognitive Level:** Application

#### Pattern Structure
Convert between volume ratio and linear scale factor using k³ relationship.

#### Example from Source
> Two similar pyramids have volumes 8 cm³ and 27 cm³. Find ratio of heights.

#### How to Create Variations
- Different 3D shapes: cones, spheres, prisms
- Reverse: give linear ratio, find volume ratio
- Give surface area ratio, find linear ratio (k²)
- Use non-perfect-cube volumes (requires calculation)

#### Visual Element
- Type: None (or two similar shapes for comparison)

---

### Pattern: Similar Shapes Surface Area Ratio

**Source:** AOS 7 Mock CAT 1, Q10
**Topic:** Geometry
**Cognitive Level:** Application

#### Pattern Structure
Use linear ratio to find surface area ratio (k² relationship).

#### Example from Source
> Two cylinders have heights 6 cm and 9 cm. If smaller SA = 80 cm², find larger SA.

#### How to Create Variations
- Give areas, find linear ratio
- Different 3D shapes
- Multi-step: find linear ratio from volume, then find SA

#### Visual Element
- Type: Diagram (two similar shapes)
- Essential: Both shapes shown, at least one linear dimension on each
- Variable: Shape type, orientation, values

---

## 2.12 Circle Calculations
*Segment, sector, annulus*

### Pattern: Segment Area (Sector minus Triangle)

**Source:** AOS 7 Mock CAT 1, Q8
**Topic:** Geometry
**Cognitive Level:** Analysis

#### Pattern Structure
Calculate segment area by subtracting triangle from sector.

#### Example from Source
> Circle with radius 6 cm. Find area of shaded minor segment.

#### How to Create Variations
- Different central angles: 60°, 90°, 120°
- Major segment instead of minor
- Give chord length, require angle calculation
- Ask for perimeter of segment

#### Visual Element
- Type: Circle Diagram
- Essential: Circle, chord, shaded segment region
- Variable: Angle, radius, major/minor

---

### Pattern: Annulus Area (Concentric Circles)

**Source:** AOS 7 Mock CAT 1, Q11
**Topic:** Geometry
**Cognitive Level:** Application

#### Pattern Structure
Calculate area between two concentric circles.

#### Example from Source
> Pool has radius 5m with 1m wide path around it. Find path area.

#### How to Create Variations
- Give outer radius instead of path width
- Ask for perimeter (inner + outer)
- Ask for cost given price per m²
- Different shapes: square within square

#### Visual Element
- Type: Diagram (concentric circles)
- Essential: Two circles, ring between them clearly shown
- Variable: Radii values, context (pool, track, etc.)

---

## 2.13 Composite Area
*Subtraction of shapes*

### Pattern: Composite Area (Subtraction)

**Source:** AOS 7 Mock CAT 1, Q6
**Topic:** Geometry
**Cognitive Level:** Application

#### Pattern Structure
Find shaded area by subtracting one shape from another.

#### Example from Source
> Square (side 14 cm) with inscribed circle. Find shaded corner area in terms of π.

#### How to Create Variations
- Reverse: circle with inscribed square
- Different shapes: rectangle + semicircles, triangle + circle
- Ask for percentage/fraction shaded
- Change which region is shaded

#### Visual Element
- Type: 2D Diagram
- Essential: Two shapes (one inside other), clear shading
- Variable: Shape types, which is inner/outer, shading location

---

## 2.14 Pythagoras Application
*Find missing length using Pythagoras*

### Pattern: Find Slant Height of Cone

**Source:** AOS 7 Mock CAT 1, Q14a
**Topic:** Geometry
**Cognitive Level:** Application

#### Pattern Structure
Use Pythagoras to find slant height from radius and perpendicular height.

#### Example from Source
> Cone with radius 10 cm and height 24 cm. Find slant height.

#### How to Create Variations
- Give slant height, find perpendicular height
- Give slant height and height, find radius
- Apply result to CSA or total SA
- Use in context (birthday hat, ice cream cone)

#### Visual Element
- Type: 3D Diagram (cone) or 2D cross-section
- Essential: Radius, height, slant height relationship visible
- Variable: Values, context

---

### Pattern: Height of Equilateral/Isosceles Triangle

**Source:** AOS 7 Mock CAT 1, Q15a, Q16a
**Topic:** Geometry
**Cognitive Level:** Application

#### Pattern Structure
Use Pythagoras to find height of triangle (height bisects base in isosceles).

#### Example from Source
> A-frame triangle with QR = 5m (side), PR = 6m (base). Find height QS.

#### How to Create Variations
- Equilateral triangle (special case)
- Right triangle (height is a side)
- Give height, find side length
- Apply to prism volume or similar triangles

#### Visual Element
- Type: 2D Diagram (triangle)
- Essential: Triangle with height shown, base and side labeled
- Variable: Triangle type, values

---

# 3. SHOW/PROVE (1 pattern)

## 3.1 Theorem Verification
*Show factor/remainder theorem applies*

### Pattern: Factor Theorem Verification

**Source:** AOS 8 Mock CAT 1, Q3
**Topic:** Algebra
**Cognitive Level:** Application

#### Pattern Structure
Show that a given linear expression IS or IS NOT a factor of a polynomial.

#### Example from Source
> Show that (x - 2) is a factor of P(x) = x³ - 7x + 6.

#### How to Create Variations
- Use different polynomials and potential factors
- Ask to show something is NOT a factor
- Reverse: find k such that (x - a) is a factor
- Ask for complete factorization

#### Visual Element
- Type: None

---

# 4. SOLVE EQUATION (1 pattern)

## 4.1 Null Factor Law
*Solve factored equation = 0*

### Pattern: Solve Factored Polynomial Equation

**Source:** AOS 8 Mock CAT 1, Q4
**Topic:** Algebra
**Cognitive Level:** Application

#### Pattern Structure
Solve polynomial equation already in factored form using null factor law.

#### Example from Source
> Solve the equation (3x - 1)(x + 5)(x - 2) = 0.

#### How to Create Variations
- Vary number of factors (2, 3, 4+)
- Include fractional solutions: (2x + 3), (5x - 2)
- Mix simple (x - a) with complex (ax + b) factors
- Extend: inequalities like (x - 1)(x + 3) > 0

#### Visual Element
- Type: None

---

# 5. GRAPH SKETCH (6 patterns)

## 5.1 Polynomial Graph
*Sketch from factored form*

### Pattern: Sketch Polynomial from Factored Form

**Source:** AOS 8 Mock CAT 1, Q5
**Topic:** Algebra
**Cognitive Level:** Application/Analysis

#### Pattern Structure
Sketch graph of polynomial in factored form, label all intercepts.

#### Example from Source
> Sketch the graph of y = (x + 1)(x - 2)(x - 4), clearly labelling all axis intercepts.

#### How to Create Variations
- Different factors: change x-intercept positions
- Include repeated factor: (x - 1)²(x + 2) for touching behavior
- Negative leading coefficient: flip orientation
- Different degrees: quadratic, quartic

#### Visual Element
- Type: Graph (student-drawn)
- Essential: Correct shape, all intercepts labeled with coordinates
- Variable: Scale, exact curve aesthetics

---

### Pattern: Real-World Polynomial Sketch

**Source:** AOS 8 Mock CAT 1, Q12
**Topic:** Algebra
**Cognitive Level:** Application/Analysis

#### Pattern Structure
Given polynomial in real-world context, find intercepts AND sketch graph.

#### Example from Source
> The vertical displacement of a roller-coaster car is modelled by y = -2(x - 1)(x + 3)(x - 5).
> a. Find the axis intercepts.
> b. Sketch a rough graph showing the intercepts.

#### How to Create Variations
- Different contexts: bridge, tunnel, hill, wave
- Positive vs negative leading coefficient
- Different number of intercepts
- Add constraints: "valid for x ≥ 0"

#### Visual Element
- Type: Graph (student-drawn)
- Essential: Shape matching context, intercepts labeled
- Variable: Context, scale, orientation

---

## 5.2 Statistical Display
*Box plot, scatter plot*

### Pattern: Construct Box Plot

**Source:** AOS 6 Mock CAT 2, Q9
**Topic:** Statistics
**Cognitive Level:** Application

#### Pattern Structure
Given five-figure summary, draw box plot on number line.

#### Example from Source
> Draw a box plot for: Min=5, Q₁=10, Median=15, Q₃=25, Max=30.

#### How to Create Variations
- Single box plot vs parallel box plots
- Provide raw data (must find summary first)
- Include outliers (shown as separate points)
- Different scales and ranges

#### Visual Element
- Type: Box Plot (student-drawn)
- Essential: Box from Q₁ to Q₃, median line, whiskers to min/max
- Variable: Scale, position, values

---

### Pattern: Construct Parallel Box Plots

**Source:** AOS 6 Mock CAT 2, Q16b
**Topic:** Statistics
**Cognitive Level:** Application

#### Pattern Structure
Draw two box plots on same axes for comparison.

#### Example from Source
> On the axes below, draw parallel box plots to compare Class 10A and 10B.

#### How to Create Variations
- Provide five-figure summaries vs raw data
- Different contexts: test scores, heights, times
- More than two groups
- Include interpretation question

#### Visual Element
- Type: Parallel Box Plots (student-drawn)
- Essential: Two aligned box plots, same scale, labels
- Variable: Number of groups, values, scale

---

### Pattern: Construct Scatter Plot

**Source:** AOS 6 Mock CAT 2, Q15a
**Topic:** Statistics
**Cognitive Level:** Application

#### Pattern Structure
Plot bivariate data points on coordinate grid.

#### Example from Source
> | Temperature | 22 | 25 | 28 | 30 | 32 | 35 | 20 | 26 |
> | Ice Creams  | 40 | 55 | 70 | 80 | 95 | 110| 30 | 60 |
> Construct a scatterplot of the data.

#### How to Create Variations
- Different contexts: study hours/scores, age/height
- Positive, negative, or no correlation
- Different number of points (6-12)
- Include line of best fit

#### Visual Element
- Type: Scatter Plot (student-drawn)
- Essential: Labeled axes, accurate point placement
- Variable: Context, scale, number of points

---

## 5.3 Probability Display
*Tree diagram*

### Pattern: Construct Tree Diagram

**Source:** AOS 6 Mock CAT 2, Q11
**Topic:** Probability
**Cognitive Level:** Application

#### Pattern Structure
Draw tree diagram showing all outcomes with probabilities on branches.

#### Example from Source
> Bag has 6 red, 4 blue balls. Pick one, don't replace, pick second.
> Draw tree diagram showing all outcomes with probabilities.

#### How to Create Variations
- With replacement (probabilities stay same)
- Without replacement (probabilities change)
- Two stages vs three stages
- Different numbers of outcomes per stage

#### Visual Element
- Type: Tree Diagram (student-drawn)
- Essential: Branches, labels, probabilities on each branch
- Variable: Number of stages, outcomes per stage, context

---

# 6. GRAPH READING (5 patterns)

## 6.1 Extract Coefficients
*Find unknowns from graph points*

### Pattern: Find Coefficients from Graph Points

**Source:** AOS 8 Mock CAT 1, Q10
**Topic:** Algebra
**Cognitive Level:** Analysis

#### Pattern Structure
Given polynomial with unknowns and points from graph, find coefficient values.

#### Example from Source
> The cubic P(x) = -x³ + ax² + bx + c passes through (-1, -2), (0, -4), and (2, 4).
> Find the values of a, b, and c.

#### How to Create Variations
- Different degrees: quadratic (2 unknowns), quartic (4 unknowns)
- Different point combinations (include/exclude y-intercept)
- Give x-intercepts instead of general points
- Combine with other info: "has turning point at..."

#### Visual Element
- Type: Graph (given)
- Essential: Curve with clearly labeled points
- Variable: Degree, point locations, coefficient sign

---

## 6.2 Venn/Table Reading
*Read probability from diagram*

### Pattern: Venn Diagram Probability

**Source:** AOS 6 Mock CAT 2, Q6
**Topic:** Probability
**Cognitive Level:** Application

#### Pattern Structure
Read regions from Venn diagram, calculate probability.

#### Example from Source
> [Venn diagram with regions: A only=12, Both=5, B only=15, Neither=8]
> Find P(A ∪ B).

#### How to Create Variations
- Ask for: P(A∪B), P(A∩B), P(A'), P(A∩B'), P(A|B)
- Two-circle or three-circle diagrams
- Use context labels: "Cat owners", "Dog owners"
- Provide some regions, ask to find missing one

#### Visual Element
- Type: Venn Diagram (given)
- Essential: Circles with clear regions, numbers in each region
- Variable: Number values, set labels, number of circles

---

### Pattern: Two-Way Table Probability

**Source:** AOS 6 Mock CAT 2, Q5
**Topic:** Probability
**Cognitive Level:** Application

#### Pattern Structure
Read value from table and calculate probability.

#### Example from Source
> |  | Basketball | Soccer | Total |
> | Boys | 18 | 12 | 30 |
> | Girls | 15 | 10 | 25 |
> | Total | 33 | 22 | 55 |
> a. How many girls prefer basketball?
> b. What is probability student is a girl who prefers soccer?

#### How to Create Variations
- Different categories: subjects, foods, activities
- Ask for joint, marginal, or conditional probability
- Provide incomplete table (find missing value)
- Compare probabilities between groups

#### Visual Element
- Type: Table (given)
- Essential: Row/column headers, cell values, totals
- Variable: Categories, numbers, table size (2×2, 2×3, 3×3)

---

## 6.3 Statistical Display Reading
*Extract data from plot*

### Pattern: Read Stem-and-Leaf Plot

**Source:** AOS 6 Mock CAT 2, Q16
**Topic:** Statistics
**Cognitive Level:** Analysis

#### Pattern Structure
Extract data from stem-and-leaf, calculate statistics, compare datasets.

#### Example from Source
> [Back-to-back stem-and-leaf for Class 10A and 10B]
> a. Find five-figure summary for both classes.
> c. Calculate mean and range for Class 10B.
> d. Compare the two classes.

#### How to Create Variations
- Single stem-and-leaf vs back-to-back
- Different contexts: heights, times, scores
- Ask for different statistics
- Require comparative statement

#### Visual Element
- Type: Stem-and-Leaf Plot (given)
- Essential: Stem column, leaves in order, key
- Variable: Data values, number of stems, context

---

## 6.4 Circle Diagram Reading
*Apply circle theorems from diagram*

### Pattern: Power of a Point (Tangent-Secant)

**Source:** AOS 7 Mock CAT 1, Q9
**Topic:** Geometry
**Cognitive Level:** Analysis

#### Pattern Structure
Apply power of point theorem: tangent² = near × far segment.

#### Example from Source
> [Diagram: external point P, tangent PA = x, secant through P with PD = 2, DC = 6]
> Find x.

#### How to Create Variations
- Two secants instead (PA × PB = PC × PD)
- Tangent-tangent (equal lengths)
- Reverse: give tangent, find secant segment
- Change which segment is unknown

#### Visual Element
- Type: Circle Diagram (given)
- Essential: Circle, external point, lines from point to/through circle
- Variable: Tangent vs secant, segment labels, unknown position

---

# 7. CONTEXT TRANSLATION (5 patterns)

## 7.1 Geometric to Algebraic
*Shape description → expression*

### Pattern: Geometric to Polynomial Expression

**Source:** AOS 8 Mock CAT 1, Q13
**Topic:** Algebra
**Cognitive Level:** Analysis

#### Pattern Structure
Translate geometric description to polynomial, then evaluate.

#### Example from Source
> A rectangular garden has length 4m longer than width x.
> a. Write expression for area A(x).
> b. Pond depth is (x - 1)m. Write expression for volume V(x).
> c. Find volume if width is 3m.

#### How to Create Variations
- Different shapes: box, cylinder, prism
- Different relationships: "twice the height", "5 less than length"
- Different quantities: perimeter, surface area
- Optimization: "find dimensions for volume = 100"

#### Visual Element
- Type: None (or optional diagram)

---

## 7.2 Data Comparison
*Compare distributions in words*

### Pattern: Compare Two Distributions

**Source:** AOS 6 Mock CAT 2, Q16d
**Topic:** Statistics
**Cognitive Level:** Analysis

#### Pattern Structure
Write comparative statement using measures of center AND spread.

#### Example from Source
> Class 10A: mean ≈ 32.7, SD ≈ 8.4
> Class 10B: [calculated values]
> Write a brief statement comparing performance. Reference at least one measure of centre and one measure of spread.

#### How to Create Variations
- Give all statistics vs require calculation
- Require specific measures to reference
- Open-ended vs structured comparison
- Different contexts: two teams, two years, two groups

#### Visual Element
- Type: None (statistics provided or calculated)

---

## 7.3 Similar Figures
*Real-world similarity (shadows)*

### Pattern: Similar Triangles (Shadow Problems)

**Source:** AOS 7 Mock CAT 1, Q15b
**Topic:** Geometry
**Cognitive Level:** Analysis

#### Pattern Structure
Use proportional reasoning with similar triangles from shadow scenario.

#### Example from Source
> Beam (height h₁) casts 8m shadow. Pole (height h₂) casts 10m shadow at same time.
> If h₁ = 4m, find h₂.

#### How to Create Variations
- Different objects: flagpole, building, tree
- Reverse: give heights, find shadow ratio
- Three objects (more complex ratios)
- Include sun angle calculation

#### Visual Element
- Type: Diagram (objects with shadows)
- Essential: Two vertical objects, shadow lengths shown
- Variable: Object types, values, number of objects

---

## 7.4 Unit Conversion
*Convert units in context*

### Pattern: Unit Conversion in Context

**Source:** AOS 7 Mock CAT 1, Q17c
**Topic:** Geometry
**Cognitive Level:** Application

#### Pattern Structure
Convert between units (m³ to litres, cm to m, etc.) in practical problem.

#### Example from Source
> Pool volume is 500 m³. How many litres to fill it?

#### How to Create Variations
- Different conversions: cm³ to ml, m² to cm²
- Include in multi-step problem
- Practical contexts: filling tank, material needed
- Time-based: rate of filling/emptying

#### Visual Element
- Type: None (or context diagram)

---

## 7.5 Practical Calculation
*Real-world with wastage/extra*

### Pattern: Tiling with Wastage

**Source:** AOS 7 Mock CAT 1, Q17e
**Topic:** Geometry
**Cognitive Level:** Synthesis

#### Pattern Structure
Calculate number of tiles needed, including percentage for wastage.

#### Example from Source
> Walls need tiling: SA = X m². Tiles are 25cm × 25cm. Allow 10% wastage. How many tiles?

#### How to Create Variations
- Different tile sizes/shapes
- Different wastage percentages (5%, 15%)
- Include grout calculation
- Calculate cost given price per tile

#### Visual Element
- Type: None (or wall/floor diagram)

---

# 8. MULTI-PART ANALYSIS (4 patterns)

## 8.1 Polynomial Model
*Multiple angles on one polynomial*

### Pattern: Extended Polynomial Model Analysis

**Source:** AOS 8 Mock CAT 1, Q14
**Topic:** Algebra
**Cognitive Level:** Analysis/Synthesis

#### Pattern Structure
Multi-part question analyzing polynomial model from multiple angles.

#### Example from Source
> Cross-section of hill: H(x) = -¼x(x - 8)(x - 12)
> a. Find height at x = 4. (evaluate)
> b. At what distances is height = 0? (find zeros)
> c. Expand to standard form. (algebra)
> d. How many intersection points with line y = 2x? (reasoning)
> e. Sketch the graph. (visual)

#### How to Create Variations
- Different contexts: valley, wave, trajectory
- Different sub-questions: max height, domain where H > 0
- Different polynomial degrees
- Include comparison with another function

#### Visual Element
- Type: Graph (student-drawn for part e)
- Essential: Shape, intercepts, correct orientation
- Variable: All values based on equation

---

## 8.2 Bivariate Analysis
*Plot → correlation → equation → predict*

### Pattern: Complete Bivariate Analysis

**Source:** AOS 6 Mock CAT 2, Q15
**Topic:** Statistics
**Cognitive Level:** Synthesis

#### Pattern Structure
Full analysis: plot data, describe correlation, find equation, make predictions.

#### Example from Source
> Temperature vs Ice Cream Sales data
> a. Construct scatterplot
> b. Describe correlation
> c. Find line equation
> d-e. Make predictions

#### How to Create Variations
- Different contexts: exercise/heart rate, practice/performance
- Positive vs negative correlation
- Interpolation AND extrapolation questions
- Discuss reliability of predictions

#### Visual Element
- Type: Scatter Plot (student-drawn + given grid)
- Essential: Axes, points, line of best fit
- Variable: Context, scale, correlation direction

---

## 8.3 Composite Solid
*Multiple 3D shapes combined*

### Pattern: Composite 3D Solid (Multiple Parts)

**Source:** AOS 7 Mock CAT 1, Q18
**Topic:** Geometry
**Cognitive Level:** Synthesis

#### Pattern Structure
Calculate volume and/or surface area of solid made from multiple 3D shapes.

#### Example from Source
> Rocket: cylinder (r=4, h=20) + cone (r=4, h=3) + frustum (h=2, R=6, r=4)
> a. Volume of cylinder + cone
> b. Volume of frustum (using similarity)
> c. Total volume
> d. Total external surface area

#### How to Create Variations
- Different components: hemisphere, pyramid, prism
- Fewer or more parts
- Ask only volume or only surface area
- Practical applications: weight, cost of materials

#### Visual Element
- Type: 3D Diagram
- Essential: All components visible, boundaries clear, all dimensions labeled
- Variable: Component types, arrangement, orientation

---

## 8.4 Prism Application
*Area → volume → conversion → practical*

### Pattern: Extended Prism Application

**Source:** AOS 7 Mock CAT 1, Q17
**Topic:** Geometry
**Cognitive Level:** Synthesis

#### Pattern Structure
Complete analysis of prism: cross-section area, volume, conversions, surface area, practical calculations.

#### Example from Source
> Swimming pool (trapezoidal prism): parallel sides 1.2m and 2.8m, length 25m, width 10m.
> a. Area of cross-section
> b. Volume
> c. Litres of water
> d. Wall area to tile
> e. Number of tiles (with wastage)

#### How to Create Variations
- Different cross-section shapes
- Different practical applications (tank, container, room)
- Add cost calculations
- Include time to fill/empty

#### Visual Element
- Type: 3D Diagram
- Essential: Cross-section visible, all dimensions labeled
- Variable: Cross-section shape, context

---

# 9. BUSINESS/REAL-WORLD MODEL (1 pattern)

## 9.1 Revenue-Cost-Profit
*Build expressions, find break-even*

### Pattern: Revenue-Cost-Profit Analysis

**Source:** AOS 8 Mock CAT 1, Q15
**Topic:** Algebra
**Cognitive Level:** Synthesis

#### Pattern Structure
Build revenue/profit expressions, factor, find break-even points.

#### Example from Source
> Boxes sold: x, Price: p(x) = 24 - x, Cost: C(x) = -x³ + 8x² + 4x + 12
> a. Write revenue R(x). (multiply)
> b. Write profit P(x). (subtract)
> c. Factor P(x) completely. (algebra)
> d. Find break-even points. (solve)
> e. Calculate revenue and cost at break-even. (evaluate)

#### How to Create Variations
- Different contexts: tickets, products, services
- Different pricing models: linear, quadratic
- Different cost structures
- Additional questions: maximum profit, profit margin

#### Visual Element
- Type: None (or optional graph)

---

# Pattern Statistics

## By Category

| Category | Sub-categories | Patterns |
|----------|----------------|----------|
| 1. Direct Recall | 2 | 2 |
| 2. Calculation | 14 | 24 |
| 3. Show/Prove | 1 | 1 |
| 4. Solve Equation | 1 | 1 |
| 5. Graph Sketch | 3 | 6 |
| 6. Graph Reading | 4 | 5 |
| 7. Context Translation | 5 | 5 |
| 8. Multi-Part Analysis | 4 | 4 |
| 9. Business/Real-World Model | 1 | 1 |
| **TOTAL** | **35** | **49** |

## By Topic

| Topic | Patterns |
|-------|----------|
| Algebra | 14 |
| Statistics | 12 |
| Probability | 7 |
| Geometry | 16 |
| **TOTAL** | **49** |

---

# Sub-category Index

## 1. Direct Recall
- 1.1 Identify Feature
- 1.2 Count/Enumerate

## 2. Calculation
- 2.1 Theorem Application
- 2.2 Degree/Structure Analysis
- 2.3 Measures of Center
- 2.4 Measures of Spread
- 2.5 Five-Figure Summary
- 2.6 Basic Probability
- 2.7 Probability Rules
- 2.8 Line of Best Fit
- 2.9 Surface Area
- 2.10 Volume
- 2.11 Similarity Ratios
- 2.12 Circle Calculations
- 2.13 Composite Area
- 2.14 Pythagoras Application

## 3. Show/Prove
- 3.1 Theorem Verification

## 4. Solve Equation
- 4.1 Null Factor Law

## 5. Graph Sketch
- 5.1 Polynomial Graph
- 5.2 Statistical Display
- 5.3 Probability Display

## 6. Graph Reading
- 6.1 Extract Coefficients
- 6.2 Venn/Table Reading
- 6.3 Statistical Display Reading
- 6.4 Circle Diagram Reading

## 7. Context Translation
- 7.1 Geometric to Algebraic
- 7.2 Data Comparison
- 7.3 Similar Figures
- 7.4 Unit Conversion
- 7.5 Practical Calculation

## 8. Multi-Part Analysis
- 8.1 Polynomial Model
- 8.2 Bivariate Analysis
- 8.3 Composite Solid
- 8.4 Prism Application

## 9. Business/Real-World Model
- 9.1 Revenue-Cost-Profit

---

# How to Use This Library

## Creating a New Test

1. **Choose topic from curriculum_context.md**
2. **Select appropriate format patterns** based on:
   - Cognitive levels needed (mix of recall → synthesis)
   - Visual elements desired (diagrams, graphs)
   - Real-world context requirements
3. **Browse by Sub-category** to find specific pattern types
4. **Filter by Topic** if needed (Algebra, Statistics, Probability, Geometry)
5. **Apply pattern with new values** from curriculum
6. **Check difficulty against curriculum benchmarks**

## Adding New Patterns

When processing new tests, append new patterns following the template:
- Check if similar pattern exists first
- Assign to ONE of the 9 categories
- Place under appropriate sub-category (or create new sub-category)
- Include Topic tag for filtering
- Include source reference
- Document variations

---

*Last updated: 2026-01-08*
*Sources: AOS 8 Mock CAT 1 (Polynomials), AOS 6 Mock CAT 2 (Statistics & Probability), AOS 7 Mock CAT 1 (Geometry & Measurement)*
