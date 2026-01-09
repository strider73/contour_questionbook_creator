# Year 10 Mathematics - Complete Curriculum Reference

A comprehensive reference combining all Areas of Study (AOS 6-9) from Contour Education workbooks plus Linear Equations content.

**Contents:**
- [AOS 6: Statistics and Probability [10.1]](#curriculum-context-year-10-mathematics-aos-6-revision-101-workbook)
- [AOS 7: Circle Geometry and Measurement [10.2]](#curriculum-context-year-10-mathematics-aos-7-revision-102-workbook)
- [AOS 8: Polynomials [10.3]](#curriculum-context-year-10-mathematics-aos-8-revision-103-workbook)
- [AOS 9: Functions and Transformations [10.4]](#curriculum-context-year-10-mathematics-aos-9-revision-104)

---

## Quick Reference by AOS

| AOS | Code | Topic Area | Main Focus | Pages |
|-----|------|------------|------------|-------|
| **AOS 6** | [10.1] | Statistics & Probability | Data analysis, probability rules, distributions | 1200+ lines |
| **AOS 7** | [10.2] | Circle Geometry & Measurement | Circle theorems, surface area, volume | 1100+ lines |
| **AOS 8** | [10.3] | Polynomials | Division, factor theorem, graphing polynomials | 1180 lines |
| **AOS 9** | [10.4] | Functions & Graphs | Domain/range, transformations, special functions | 960 lines |

---

# Curriculum Context: Year 10 Mathematics AOS 6 Revision [10.1]

## Metadata
- **Source**: Year 10 Mathematics AOS 6 Revision [10.1] Workbook.pdf
- **Publisher**: Contour Education
- **Subject**: Mathematics (Statistics and Probability)
- **Year/Grade Level**: Year 10
- **Topic Area**: Area of Study 6 - Statistics and Probability
- **Analysis Date**: 2026-01-08
- **Total Pages**: 31

---

## 1. Topics Covered

### Topic 1: Two-Step Experiments and Venn Diagrams
- **Definition**: Analysis of probability scenarios involving multiple stages or combined events
- **Key Concepts**:
  - Sample spaces
  - Equally likely outcomes
  - Tree diagrams for sequential events
  - Set notation (union, intersection)
  - Venn diagrams for visualizing combined events
  - Two-way tables for organizing categorical data
- **Subtopics**:
  - Probability Fundamentals
  - Multi-Stage Experiments
  - Venn Diagram and Combining Events
  - Apply the Addition Rule to Find Unknown Probabilities
  - Two-Way Table
- **Pages**: 3-11

### Topic 2: Conditional Probability and Independent Events
- **Definition**: Calculating probabilities when conditions are known, and understanding when events affect each other
- **Key Concepts**:
  - Conditional probability (likelihood given a condition)
  - Independent vs dependent events
  - Multiplication rule for probabilities
  - With/without replacement scenarios
- **Subtopics**:
  - Conditional Probability
  - Independent Events
  - Combining Addition Rule and Independent Event Rule
- **Pages**: 12-17

### Topic 3: Measure of Centre and Spread, Standard Deviation
- **Definition**: Statistical measures to describe the center, spread, and variability of datasets
- **Key Concepts**:
  - Measures of center (mean, median, mode)
  - Measures of spread (range, IQR)
  - Five-figure summary
  - Box-and-whisker plots
  - Outlier detection using fences
  - Standard deviation as a measure of variability
  - Z-scores for standardizing data
  - Normal distribution (68-95-99.7% rule)
- **Subtopics**:
  - Understanding Data
  - Measure of Spread
  - Standard Deviation
  - Z (standardised) Score
- **Pages**: 18-27

### Topic 4: Bivariate Data and Scatter Plots
- **Definition**: Analysis of relationships between two numerical variables
- **Key Concepts**:
  - Independent vs dependent variables
  - Scatter plots
  - Types of correlation (positive, negative, none)
  - Line of best fit by eye
  - Linear equation (y = mx + c)
  - Making predictions using trend lines
- **Subtopics**:
  - Bivariate Data
  - Line of Best Fit by Eye
- **Pages**: 28-31

---

## 2. Formulas and Theorems

### Basic Probability Formula
- **Statement**: For equally likely outcomes, probability equals favorable outcomes divided by total outcomes
- **Formula**: $\text{Pr}(\text{success}) = \frac{\text{Number of successful outcomes}}{\text{Number of total outcomes}}$
- **Variables**:
  - Pr = Probability
  - success = the event of interest
- **When to Use**: When all outcomes in the sample space are equally likely
- **Example from Workbook**: Selecting an orange from a basket with 6 oranges and 4 apples: Pr(orange) = 6/10 = 3/5

### Addition Rule for Probability
- **Statement**: The probability of event A or B occurring equals the sum of their individual probabilities minus the probability of both occurring
- **Formula**: $\text{Pr}(A \cup B) = \text{Pr}(A) + \text{Pr}(B) - \text{Pr}(A \cap B)$
- **Variables**:
  - A, B = events
  - $A \cup B$ = union (A or B)
  - $A \cap B$ = intersection (A and B)
- **When to Use**: Finding probability of at least one of two events occurring
- **Example from Workbook**: Given Pr(A) = 0.4, Pr(B) = 0.7, Pr(A ∩ B) = 0.3, find Pr(A ∪ B) = 0.4 + 0.7 - 0.3 = 0.8

### Addition Rule for Mutually Exclusive Events
- **Statement**: If events cannot occur simultaneously, intersection is zero
- **Formula**: $\text{Pr}(A \cup B) = \text{Pr}(A) + \text{Pr}(B)$ when $\text{Pr}(A \cap B) = 0$
- **When to Use**: When events A and B are mutually exclusive (cannot happen together)
- **Example from Workbook**: If Pr(X) = 0.6 and Pr(X ∪ Y) = 0.9 and they're mutually exclusive, then Pr(Y) = 0.3

### Conditional Probability Formula
- **Statement**: The likelihood of event A occurring given that event B has already occurred
- **Formula**: $\text{Pr}(A|B) = \frac{\text{Pr}(A \cap B)}{\text{Pr}(B)}$
- **Variables**:
  - Pr(A|B) = probability of A given B
  - Pr(A ∩ B) = probability of both A and B
  - Pr(B) = probability of B
- **When to Use**: When calculating probability with a known condition
- **Example from Workbook**: Pizza/burger preference - Pr(Burgers|Pizza) = Pr(Burgers AND Pizza) / Pr(Pizza) = 20/35 = 4/7

### Multiplication Rule for Conditional Probability
- **Statement**: The probability of both events occurring equals the probability of the first times the conditional probability of the second given the first
- **Formula**: $\text{Pr}(A \cap B) = \text{Pr}(A) \times \text{Pr}(B|A)$
- **When to Use**: Finding probability of sequential events or joint events
- **Example from Workbook**: Selecting marbles with replacement - probabilities multiply along tree branches

### Independent Events Rule
- **Statement**: Two events are independent when the occurrence of one does not affect the probability of the other
- **Formula**: $\text{Pr}(A \cap B) = \text{Pr}(A) \times \text{Pr}(B)$
- **Test for Independence**: Events A and B are independent if Pr(A ∩ B) = Pr(A) × Pr(B)
- **When to Use**:
  - Multi-stage experiments with replacement
  - Events that don't influence each other
- **Example from Workbook**: Testing if Pr(A) = 3/4, Pr(B) = 1/2, Pr(A ∩ B) = 3/8 are independent: (3/4) × (1/2) = 3/8 ✓ Independent

### Combined Addition and Independent Events Rule
- **Statement**: For independent events, the addition rule simplifies
- **Formula**: $\text{Pr}(A \cup B) = \text{Pr}(A) + \text{Pr}(B) - \text{Pr}(A) \times \text{Pr}(B)$
- **When to Use**: Finding probability of A or B when events are independent
- **Derivation**: Substitutes Pr(A ∩ B) = Pr(A) × Pr(B) into the addition rule

### Mean (Average)
- **Statement**: The sum of all values divided by the number of values
- **Formula**: $\bar{x} = \frac{\Sigma x}{n}$
- **Variables**:
  - $\bar{x}$ = mean
  - $\Sigma x$ = sum of all observations
  - $n$ = number of observations
- **When to Use**: Finding the central tendency of numerical data
- **Example from Workbook**: Finding missing frequencies when mean is given (Question 15)

### Median
- **Statement**: The middle value when data is ordered
- **Formula**:
  - Odd number of values: middle value
  - Even number of values: average of two middle values
- **When to Use**: Finding the central value, especially when outliers are present
- **Example from Workbook**: For {2, 4, 5, 8, 9}, median = 5; For {3, 5, 7, 11, 13, 15}, median = (7+11)/2 = 9

### Range
- **Statement**: The difference between maximum and minimum values
- **Formula**: $\text{Range} = \text{max} - \text{min}$
- **When to Use**: Quick measure of data spread
- **Example from Workbook**: Visualized on box plots showing distance from min to max

### Interquartile Range (IQR)
- **Statement**: The range of the middle 50% of ordered data
- **Formula**: $\text{IQR} = Q_3 - Q_1$
- **Variables**:
  - $Q_1$ = lower quartile (25th percentile)
  - $Q_3$ = upper quartile (75th percentile)
- **When to Use**: Robust measure of spread, not affected by outliers
- **Example from Workbook**: For data set with Q1=2 and Q3=15, IQR = 15-2 = 13

### Upper and Lower Fences (Outlier Detection)
- **Statement**: Boundaries to identify outliers in a dataset
- **Formulas**:
  - $\text{Upper Fence} = Q_3 + 1.5 \times \text{IQR}$
  - $\text{Lower Fence} = Q_1 - 1.5 \times \text{IQR}$
- **When to Use**: Detecting outliers in box plot analysis
- **Example from Workbook**: Question 16 - finding outliers in dataset using fence calculations

### Standard Deviation
- **Statement**: Measure of variability showing average distance of data points from the mean
- **Formula**: $s = \sqrt{\frac{\Sigma(x_i - \bar{x})^2}{n-1}}$
- **Variables**:
  - $s$ = sample standard deviation
  - $x_i$ = individual observation
  - $\bar{x}$ = mean
  - $n$ = number of observations
  - $\Sigma$ = sum of
- **When to Use**: Measuring data spread, especially for normal distributions
- **Example from Workbook**: Question 17 - calculating standard deviation for plant heights: {12, 15, 11, 14, 13, 17}

### Z-Score (Standardised Score)
- **Statement**: Number of standard deviations a data point is from the mean
- **Formula**: $Z = \frac{x - \bar{x}}{s}$
- **Variables**:
  - $Z$ = z-score
  - $x$ = score/observation
  - $\bar{x}$ = mean
  - $s$ = standard deviation
- **When to Use**:
  - Standardizing data for comparison
  - Identifying how unusual a value is
  - Working with normal distributions
- **Example from Workbook**: Baby weighing 2.9 kg when mean is 3.5 kg and SD is 0.5 kg: Z = (2.9-3.5)/0.5 = -1.2

### Line of Best Fit
- **Statement**: Linear equation representing the trend in bivariate data
- **Formula**: $y = mx + c$
- **Variables**:
  - $y$ = dependent variable
  - $x$ = independent variable
  - $m$ = slope (gradient)
  - $c$ = y-intercept
- **Slope Formula**: $m = \frac{y_2 - y_1}{x_2 - x_1}$
- **When to Use**: Modeling linear relationships, making predictions
- **Example from Workbook**: Ice cream sales vs temperature - using two points (19, 45) and (24, 70) to find equation y = 5x - 50

---

## 3. Worked Examples Analysis

### Example 1: Tree Diagram with Replacement (Question 3 Walkthrough)
- **Location**: Page 5
- **Topic**: Multi-Stage Experiments
- **Problem Type**: Probability with replacement using tree diagram
- **Given Information**:
  - Bag contains 2 red (R) marbles and 1 blue (B) marble
  - Marble selected, color noted, then replaced
  - Process done twice
- **Required**:
  - a) Draw tree diagram showing all outcomes
  - b) Find Pr(R, B) - probability of red then blue
  - c) Find Pr(R, R) - probability of two reds
- **Solution Method**:
  1. Draw first stage with probabilities: Pr(R) = 2/3, Pr(B) = 1/3
  2. From each outcome, draw second stage with same probabilities (replacement)
  3. List all outcomes: RR, RB, BR, BB
  4. For part b: Multiply along R then B branch: (2/3) × (1/3) = 2/9
  5. For part c: Multiply along R then R branch: (2/3) × (2/3) = 4/9
- **Key Formula Used**: $\text{Pr}(\text{sequence}) = \text{Pr}(\text{first}) \times \text{Pr}(\text{second})$
- **Final Answer**:
  - b) Pr(R, B) = 2/9
  - c) Pr(R, R) = 4/9
- **Answer Format**: Simplified fractions
- **Difficulty Level**: Intermediate

### Example 2: Multi-Stage Without Replacement (Question 4)
- **Location**: Page 6
- **Topic**: Multi-Stage Experiments without replacement
- **Problem Type**: Probability of sequential selections
- **Given Information**:
  - Class has 10 students: 6 boys and 4 girls
  - Select teacher's assistant, then class representative
  - Different students (without replacement)
- **Required**:
  - a) Draw tree diagram showing boy/girl outcomes
  - b) Find Pr(girl first, then boy)
  - c) Find Pr(two girls selected)
- **Solution Method**:
  1. First selection: Pr(Boy) = 6/10, Pr(Girl) = 4/10
  2. Second selection depends on first (no replacement):
     - If Boy first: Pr(Boy) = 5/9, Pr(Girl) = 4/9
     - If Girl first: Pr(Boy) = 6/9, Pr(Girl) = 3/9
  3. For part b: (4/10) × (6/9) = 24/90 = 4/15
  4. For part c: (4/10) × (3/9) = 12/90 = 2/15
- **Key Formula Used**: Conditional probability via tree diagram
- **Final Answer**:
  - b) Pr(G, B) = 4/15
  - c) Pr(G, G) = 2/15
- **Answer Format**: Simplified fractions
- **Difficulty Level**: Intermediate

### Example 3: Venn Diagram and Probability (Question 5)
- **Location**: Page 8
- **Topic**: Venn Diagrams and set operations
- **Problem Type**: Using Venn diagrams to calculate probabilities
- **Given Information**:
  - Survey of 50 households
  - 25 have a cat
  - 20 have a dog
  - 8 have both cat and dog
- **Required**:
  - a) Draw Venn diagram
  - b) Find Pr(cat but not dog)
  - c) Find Pr(neither cat nor dog)
- **Solution Method**:
  1. Fill Venn diagram: Intersection = 8
  2. Cat only = 25 - 8 = 17
  3. Dog only = 20 - 8 = 12
  4. Neither = 50 - (17 + 8 + 12) = 50 - 37 = 13
  5. For part b: Pr(C ∩ D') = 17/50
  6. For part c: Pr((C ∪ D)') = 13/50
- **Key Formula Used**: Set operations and basic probability
- **Final Answer**:
  - b) 17/50
  - c) 13/50
- **Answer Format**: Fractions over 50
- **Difficulty Level**: Basic to Intermediate

### Example 4: Conditional Probability from Two-Way Table (Question 9 Walkthrough)
- **Location**: Page 13
- **Topic**: Conditional Probability
- **Problem Type**: Calculate conditional probabilities from two-way table
- **Given Information**:
  - 50 people surveyed about pizza and burger preferences
  - Two-way table showing:
    - 20 prefer both
    - 10 prefer burgers but not pizza
    - 15 prefer pizza but not burgers
    - 5 prefer neither
- **Required**:
  - a) Find Pr(prefers burgers | prefers pizza)
  - b) Find Pr(does not prefer pizza | does not prefer burgers)
- **Solution Method**:
  1. Identify totals: Prefers Pizza = 35, Does not prefer burgers = 20
  2. For part a: Use conditional probability formula
     - Pr(B|P) = Pr(B ∩ P) / Pr(P) = (20/50) / (35/50) = 20/35 = 4/7
  3. For part b: Find Pr(P'|B')
     - Not completed in walkthrough, student should find answer
- **Key Formula Used**: $\text{Pr}(A|B) = \frac{\text{Pr}(A \cap B)}{\text{Pr}(B)}$
- **Final Answer**:
  - a) 4/7
- **Answer Format**: Simplified fractions
- **Difficulty Level**: Intermediate

### Example 5: Testing for Independence (Question 12 Walkthrough)
- **Location**: Page 16
- **Topic**: Independent Events
- **Problem Type**: Determine if events are independent
- **Given Information**:
  - Pr(A) = 3/4
  - Pr(B) = 1/2
  - Pr(A ∩ B) = 3/8
- **Required**: Determine if events A and B are independent
- **Solution Method**:
  1. Calculate Pr(A) × Pr(B) = (3/4) × (1/2) = 3/8
  2. Compare with Pr(A ∩ B) = 3/8
  3. Since Pr(A ∩ B) = Pr(A) × Pr(B), events are independent
- **Key Formula Used**: Independence test: $\text{Pr}(A \cap B) = \text{Pr}(A) \times \text{Pr}(B)$
- **Final Answer**: Independent
- **Answer Format**: Statement
- **Difficulty Level**: Intermediate

### Example 6: Finding Outliers (Question 16 Tech Active)
- **Location**: Page 23
- **Topic**: Outlier detection using fences
- **Problem Type**: Identify outliers in a dataset
- **Given Information**: Dataset {1, 5, 8, 12, 14, 16, 18, 20, 22, 24, 25, 26, 28, 30, 32, 35, 38, 40, 42, 45, 50, 100}
- **Required**: Find outlier(s) if any
- **Solution Method**:
  1. Find five-figure summary: min=1, Q1=16, median=25.5, Q3=38, max=100
  2. Calculate IQR = Q3 - Q1 = 38 - 16 = 22
  3. Calculate Upper Fence = Q3 + 1.5×IQR = 38 + 1.5×22 = 38 + 33 = 71
  4. Calculate Lower Fence = Q1 - 1.5×IQR = 16 - 33 = -17 (no lower outliers)
  5. Values above 71: only 100 is an outlier
- **Key Formula Used**: Upper Fence = Q3 + 1.5 × IQR
- **Final Answer**: 100 is an outlier
- **Answer Format**: Statement identifying the value
- **Difficulty Level**: Intermediate

### Example 7: Calculating Z-Score (Question 18 Walkthrough)
- **Location**: Page 27
- **Topic**: Z-score calculation
- **Problem Type**: Find standardized score for a data value
- **Given Information**:
  - Average weight of newborn babies = 3.5 kg
  - Standard deviation = 0.5 kg
  - Baby weighs 2.9 kg
- **Required**: What is the z-score for this baby?
- **Solution Method**:
  1. Identify values: x = 2.9, mean = 3.5, s = 0.5
  2. Apply formula: Z = (x - mean) / s
  3. Z = (2.9 - 3.5) / 0.5 = -0.6 / 0.5 = -1.2
- **Key Formula Used**: $Z = \frac{x - \bar{x}}{s}$
- **Final Answer**: Z = -1.2
- **Answer Format**: Decimal to 1 decimal place
- **Difficulty Level**: Basic to Intermediate

### Example 8: Line of Best Fit and Prediction (Question 25 Tech Active)
- **Location**: Page 31
- **Topic**: Bivariate data, scatter plot, line of best fit
- **Problem Type**: Construct scatter plot, find equation, make predictions
- **Given Information**:
  - Temperature (°C): 18, 20, 22, 25, 27, 28, 30
  - Cones sold: 40, 55, 60, 75, 80, 85, 95
- **Required**:
  - a) Construct scatter plot
  - b) Draw line of best fit and find equation
  - c) Estimate cones sold at 24°C and 19°C
- **Solution Method**:
  1. Plot points on scatter plot (temperature on x-axis, cones on y-axis)
  2. Draw line through middle of points passing near (19, 45) and (24, 70)
  3. Calculate slope: m = (70-45)/(24-19) = 25/5 = 5
  4. Find y-intercept: using y = mx + c with point (22, 60)
     - 60 = 5(22) + c → 60 = 110 + c → c = -50
  5. Equation: y = 5x - 50
  6. For 24°C: y = 5(24) - 50 = 120 - 50 = 70 cones
  7. For 19°C: y = 5(19) - 50 = 95 - 50 = 45 cones
- **Key Formula Used**:
  - Slope: $m = \frac{y_2 - y_1}{x_2 - x_1}$
  - Line: y = mx + c
- **Final Answer**:
  - Equation: y = 5x - 50
  - At 24°C: 70 cones
  - At 19°C: 45 cones
- **Answer Format**: Equation in y = mx + c form, predictions as whole numbers
- **Difficulty Level**: Intermediate to Advanced

---

## 4. Difficulty Benchmarks

### Basic Level
- **Characteristics**:
  - Direct application of single formula
  - Simple sample spaces
  - One or two-step calculations
  - Clear, straightforward setups
- **Typical Number Ranges**:
  - Small integers (1-20)
  - Simple fractions with denominators ≤ 10
  - Small datasets (n < 10)
- **Steps Required**: 1-2 steps
- **Formulas Used**: Single formula, direct substitution
- **Reference Examples**:
  - Question 1 (writing sample spaces)
  - Question 2 Additional (basic probability with oranges/apples)
  - Basic mean calculation
  - Simple z-score calculation (Question 19)
  - Identifying correlation type from scatter plot (Question 21)

### Intermediate Level
- **Characteristics**:
  - Multiple-step problems
  - Tree diagrams with 2 stages
  - Venn diagrams with 2 sets
  - Two-way tables
  - Conditional probability from tables
  - Standard deviation calculation
  - Line of best fit by eye
- **Typical Number Ranges**:
  - Integers up to 100
  - Fractions requiring simplification
  - Decimals to 1-2 decimal places
  - Datasets with n = 5-20
- **Steps Required**: 3-5 steps
- **Formulas Used**: May combine 2-3 formulas or concepts
- **Reference Examples**:
  - Question 3 (tree diagram with replacement)
  - Question 4 (tree diagram without replacement)
  - Question 5 (Venn diagram calculation)
  - Question 6 (addition rule application)
  - Question 8 (two-way table)
  - Question 9 (conditional probability)
  - Question 13 (finding missing probability for independent events)
  - Question 15 (finding missing frequencies given mean)
  - Question 16 (finding outliers)
  - Question 17 (standard deviation calculation)
  - Question 25 (scatter plot and line of best fit)

### Advanced Level
- **Characteristics**:
  - Multi-step reasoning required
  - Combining multiple concepts
  - Working backwards from given information
  - Extension questions
  - Requires deeper understanding of relationships
- **Typical Number Ranges**:
  - Various number types
  - May involve algebraic manipulation
  - Larger datasets
- **Steps Required**: 5+ steps, may require setup and verification
- **Formulas Used**: Multiple formulas, may need to derive or rearrange
- **Reference Examples**:
  - Question 7 (finding Pr(X) when given Pr(Y), Pr(X ∪ Y), and mutually exclusive)
  - Question 11 Extension (conditional probability with products and defects)
  - Question 14 Extension (testing independence with conditional probability)
  - Question 20 Extension (finding mean from z-score and other information)
  - Combining independent event rule with addition rule

---

## 5. Solution Strategies Taught

### Strategy 1: Tree Diagram Method for Multi-Stage Experiments
- **When Used**: Sequential or multi-stage probability problems
- **Steps**:
  1. Draw first stage branches with all possible outcomes
  2. Label each branch with its probability
  3. From each outcome, draw second stage branches
  4. Label second stage probabilities (adjust for with/without replacement)
  5. To find probability of a path: multiply probabilities along branches
  6. To find probability of multiple paths: add the path probabilities
- **Example Problem Types**:
  - Coin tosses (multiple)
  - Drawing marbles with/without replacement
  - Selecting students in sequence
- **Common Mistakes to Avoid**:
  - Forgetting to adjust probabilities for without replacement
  - Not listing all possible outcomes
  - Adding instead of multiplying along branches

### Strategy 2: Venn Diagram Method for Combined Events
- **When Used**: Problems involving union, intersection, or complement of sets
- **Steps**:
  1. Draw two overlapping circles representing the sets
  2. Start with the intersection (both A and B)
  3. Calculate "A only" = Total A - Intersection
  4. Calculate "B only" = Total B - Intersection
  5. Calculate "Neither" = Total - (A only + Both + B only)
  6. Use counts to find required probabilities
- **Example Problem Types**:
  - Survey data (preferences, ownership)
  - Categorization problems
  - Finding probabilities of combined or complementary events
- **Common Mistakes to Avoid**:
  - Double-counting the intersection
  - Forgetting to account for "neither" category
  - Confusing "A or B" with "A and B"

### Strategy 3: Two-Way Table Method for Conditional Probability
- **When Used**: Problems with two categorical variables
- **Steps**:
  1. Set up table with one variable in rows, other in columns
  2. Fill in given information
  3. Calculate row/column totals
  4. For Pr(A|B): focus on the B row/column, find A within it
  5. Apply formula: Pr(A|B) = (count of A and B) / (count of B)
- **Example Problem Types**:
  - Preference surveys
  - Attendance data
  - Classification problems
- **Common Mistakes to Avoid**:
  - Using wrong total (must use the conditional total, not overall)
  - Confusing Pr(A|B) with Pr(B|A)

### Strategy 4: Testing for Independence
- **When Used**: Determining if two events are independent
- **Steps**:
  1. Calculate Pr(A) × Pr(B)
  2. Compare with Pr(A ∩ B)
  3. If equal, events are independent
  4. If not equal, events are dependent
- **Example Problem Types**: Given probabilities, determine relationship
- **Common Mistakes to Avoid**:
  - Assuming independence without testing
  - Arithmetic errors in multiplication

### Strategy 5: Five-Figure Summary and Box Plot
- **When Used**: Analyzing spread and distribution of numerical data
- **Steps**:
  1. Order data from smallest to largest
  2. Identify minimum and maximum
  3. Find median (middle value)
  4. Find Q1 (median of lower half)
  5. Find Q3 (median of upper half)
  6. Draw box plot with these five values
  7. Calculate IQR = Q3 - Q1
  8. Check for outliers using fences if needed
- **Example Problem Types**:
  - Describing data distribution
  - Comparing datasets
  - Identifying outliers
- **Common Mistakes to Avoid**:
  - Not ordering data first
  - Including median in quartile calculations for even-sized halves

### Strategy 6: Outlier Detection Using Fences
- **When Used**: Identifying unusual values in a dataset
- **Steps**:
  1. Find Q1 and Q3
  2. Calculate IQR = Q3 - Q1
  3. Calculate Upper Fence = Q3 + 1.5 × IQR
  4. Calculate Lower Fence = Q1 - 1.5 × IQR
  5. Any value above upper fence or below lower fence is an outlier
- **Example Problem Types**: Identifying extreme values
- **Common Mistakes to Avoid**:
  - Using wrong multiplier (must be 1.5)
  - Calculation errors in fence formulas

### Strategy 7: Standard Deviation Calculation
- **When Used**: Measuring variability in a dataset
- **Steps**:
  1. Calculate mean of dataset
  2. For each value, find (value - mean)
  3. Square each difference
  4. Sum all squared differences
  5. Divide by (n - 1)
  6. Take square root
- **Example Problem Types**: Measuring spread, comparing variability
- **Common Mistakes to Avoid**:
  - Dividing by n instead of (n-1)
  - Forgetting to take square root
  - Sign errors in differences

### Strategy 8: Z-Score Calculation and Interpretation
- **When Used**: Standardizing scores, comparing values from different distributions
- **Steps**:
  1. Identify x (the value), mean, and standard deviation
  2. Calculate Z = (x - mean) / standard deviation
  3. Interpret:
     - Positive Z means above average
     - Negative Z means below average
     - |Z| tells how many standard deviations from mean
- **Example Problem Types**:
  - Comparing test scores
  - Identifying unusual observations
  - Working with normal distributions
- **Common Mistakes to Avoid**:
  - Wrong order in subtraction (must be x - mean)
  - Not considering the sign of z-score
  - Confusing z-score with the original value

### Strategy 9: Line of Best Fit by Eye
- **When Used**: Modeling linear relationships in bivariate data
- **Steps**:
  1. Plot all data points on scatter plot (x = independent, y = dependent)
  2. Draw line through middle of points (roughly equal points above/below)
  3. Select two points on the line (not necessarily data points)
  4. Calculate slope: m = (y2 - y1) / (x2 - x1)
  5. Substitute one point into y = mx + c to find c
  6. Write equation: y = mx + c
  7. Use equation to make predictions
- **Example Problem Types**:
  - Temperature vs sales
  - Height vs weight
  - Time vs distance
- **Common Mistakes to Avoid**:
  - Drawing line through outliers
  - Calculation errors in slope
  - Extrapolating too far beyond data range

---

## 6. Common Patterns

### Number Patterns Used

**Integers**:
- Small datasets: 1-20 (for basic probability, simple data analysis)
- Medium datasets: 20-100 (for surveys, two-way tables)
- Occasional larger values for outlier detection (e.g., 100 in a dataset of values <50)

**Decimals**:
- Probabilities: expressed as fractions or decimals (0.0 to 1.0)
- Standard deviations: typically 0.5 to 10, given to 1 decimal place
- Z-scores: typically -3 to +3, calculated to 1-2 decimal places
- Means: match data context

**Fractions**:
- Very common for probabilities
- Denominators: typically 2, 3, 4, 5, 6, 8, 9, 10, or multiples
- Expected in simplified form
- Common fractions: 1/2, 1/3, 2/3, 1/4, 3/4, 1/5, 2/5, 3/5, etc.

**Measurements**:
- Temperatures: 18-30°C
- Weights: 2.5-4.0 kg for baby weights
- Heights: 11-17 cm for plants
- Counts: 1-100 for surveys

### Question Formats

**Format 1**: "Find the probability of..."
- Direct probability calculation
- May involve sample spaces, tree diagrams, formulas
- Expected answer: fraction or decimal

**Format 2**: "Draw a [tree diagram / Venn diagram / scatter plot]..."
- Visual representation required
- Often followed by calculation questions
- Tests understanding of organization and structure

**Format 3**: "Determine whether..." (independence, correlation type)
- Classification or decision question
- Requires calculation to support answer
- Expected answer: statement with justification

**Format 4**: "Complete the table with missing values"
- Working backwards from given information
- Tests understanding of relationships
- Expected answer: specific values that make table consistent

**Format 5**: "Calculate the [mean / standard deviation / z-score]..."
- Direct formula application
- May require intermediate steps
- Expected answer: numerical value with specified precision

**Format 6**: "Find the outlier(s)..."
- Outlier detection
- Requires five-figure summary and fence calculations
- Expected answer: list of outlier values or "no outliers"

**Format 7**: Walkthrough/Tech Active questions
- Guided problems with more context
- Often real-world applications
- May require calculator or multiple steps

**Format 8**: Extension questions
- More challenging variations
- May combine multiple concepts
- Test deeper understanding

### Answer Expectations

**Exact vs Approximate**:
- Probabilities: exact fractions preferred, unless specifically asked for decimal
- Standard deviation: to 2 decimal places
- Z-scores: to 1-2 decimal places
- Predictions from line of best fit: whole numbers (when counting discrete items)

**Units**:
- Always include when relevant (kg, cm, °C, etc.)
- Probabilities are unitless
- Percentages when discussing normal distribution

**Significant Figures**:
- Standard deviation: 2 decimal places is standard
- Means: match precision of data or 1 decimal place
- Z-scores: 1-2 decimal places
- Line slope: whole numbers or simple fractions preferred

**Working Required**:
- Yes for all calculation questions
- Tree diagrams should show all branches and probabilities
- Venn diagrams should show all regions with counts
- Box plots should show five-figure summary
- Standard deviation requires showing steps (or calculator notation acceptable)
- Line of best fit requires showing slope calculation and equation derivation

---

## 7. Visual Diagram Patterns

**CRITICAL**: Diagrams are integral to many probability and statistics questions. Document how each concept appears visually so question generators know what diagram configurations test which concepts.

### 7.1 Diagram Configuration → Concept Mapping

| Concept/Theorem | Diagram Configuration | Key Visual Elements | How to Recognize |
|-----------------|----------------------|---------------------|------------------|
| **Sample Space** | Grid/table or list format | All possible outcomes listed systematically | Organized listing of all combinations (e.g., MAT with digits 2,4 → M2, M4, A2, A4, T2, T4) |
| **Tree Diagram (With Replacement)** | Branching structure with consistent probabilities | Equal probabilities on parallel branches across stages | Each stage has identical branch probabilities regardless of previous outcome |
| **Tree Diagram (Without Replacement)** | Branching structure with changing probabilities | Probabilities change on second stage based on first outcome | Second stage shows reduced total (e.g., 5/9 instead of 6/10) |
| **Venn Diagram (Two Sets)** | Two overlapping circles with four regions | Four distinct regions: A only, B only, Both (intersection), Neither (outside) | Counts in each region sum to total; intersection is where circles overlap |
| **Two-Way Table** | Rectangular grid with row/column headers | Categories on both axes, totals in margins | Last row and column show totals; interior cells show combinations |
| **Box-and-Whisker Plot** | Box with whiskers extending to min/max | Five key points: min, Q1, median, Q3, max | Box spans Q1 to Q3 with line at median; whiskers extend to extremes |
| **Normal Distribution Curve** | Bell-shaped symmetric curve with labeled standard deviations | Center at mean, marks at ±1s, ±2s, ±3s | Percentages labeled: 68% within ±1s, 95% within ±2s, 99.7% within ±3s |
| **Scatter Plot** | Points plotted on Cartesian plane | Independent variable on x-axis, dependent on y-axis | Points show pattern: positive (upward), negative (downward), or none |
| **Line of Best Fit** | Straight line through scatter plot | Line positioned to minimize distance to all points | Roughly equal points above and below line; represents trend |

### 7.2 Visual Elements and Their Meaning

| Visual Element | What It Indicates | Testing Aspect |
|----------------|-------------------|----------------|
| **Branch in tree diagram** | Possible outcome at that stage | Student must label with outcome and probability |
| **Terminal node in tree** | Final outcome of sequence | Student may need to list outcome or find its probability |
| **Overlapping region in Venn** | Intersection of both sets | Represents "and" (A ∩ B); student must calculate count |
| **Outside Venn circles** | Elements in neither set | Represents complement (A' ∩ B'); often forgotten by students |
| **Cell in two-way table** | Count of specific combination | Intersection of row and column categories |
| **Box in box plot** | Middle 50% of data (IQR) | Shows data concentration; narrow box = less spread |
| **Whisker in box plot** | Range to minimum/maximum | Shows full data range; length indicates spread |
| **Outlier mark (×) on box plot** | Value beyond fences | Point beyond whiskers; indicates unusual value |
| **Shaded region under normal curve** | Probability/percentage of data | Area represents proportion within those standard deviations |
| **Point on scatter plot** | Single observation of both variables | (x, y) pair from dataset |
| **Slope of line** | Rate of change of y per unit x | Positive = positive correlation; negative = negative correlation |

### 7.3 Standard Diagram Patterns by Topic

**Two-Step Experiments:**
```
Pattern: Tree Diagram Structure
├── Stage 1: First event
│   ├── Outcome A (with probability)
│   └── Outcome B (with probability)
└── Stage 2: Second event (from each Stage 1 outcome)
    ├── From A → Outcomes with probabilities
    └── From B → Outcomes with probabilities

Variations:
├── With Replacement → Same probabilities in Stage 2
└── Without Replacement → Adjusted probabilities in Stage 2
```

**Venn Diagrams:**
```
Pattern: Two-Circle Configuration
├── Region 1: A only (A - B)
├── Region 2: Intersection (A ∩ B)
├── Region 3: B only (B - A)
└── Region 4: Neither (outside both circles)

Common applications:
├── Survey preferences (cats and dogs, pizza and burgers)
├── Student clubs (chess and debate)
└── Product characteristics (minor and major defects)
```

**Box Plots:**
```
Pattern: Five-Figure Summary Display
A────────┬────┬────┬────────E
         B    C    D

Where: A=min, B=Q1, C=median, D=Q3, E=max

With outliers:
×        A────────┬────┬────┬────────E
                  B    C    D

Note: × marks appear beyond whiskers when fences are exceeded
```

**Distribution Shapes on Box Plots:**
```
Symmetric:      ├────┼────┤
                (box centered, equal whiskers)

Positive skew:  ├──┼────────┤
                (longer right whisker/box portion)

Negative skew:  ├────────┼──┤
                (longer left whisker/box portion)
```

**Scatter Plot Correlations:**
```
Positive correlation:     Negative correlation:      No correlation:
y │    ·  ·                y │  ·  ·                  y │  ·    ·  ·
  │  ·  ·                    │    ·  ·                  │    ·    ·
  │·  ·                      │      ·  ·                │  ·    ·
  └────── x                  └────────── x              └────────── x
```

### 7.4 Diagram Variations in Workbook

| Concept | Variation 1 | Variation 2 | Variation 3 |
|---------|-------------|-------------|-------------|
| **Tree diagrams** | 2 stages, 2 outcomes each (coin tosses) | 2 stages, different outcomes (letters + digits) | 2 stages with/without replacement (marbles) |
| **Venn diagrams** | Equal-sized sets | Different-sized sets | Sets with small intersection |
| **Two-way tables** | 2×2 table (binary choices) | 2×3 table (one variable with 3 categories) | Incomplete table (missing values to find) |
| **Box plots** | Standard (no outliers) | With outliers marked | Comparing multiple datasets side-by-side |
| **Scatter plots** | Strong positive correlation | Weak/no correlation | With line of best fit drawn |

**This diagram variety allows question generators to:**
- Choose DIFFERENT but VALID configurations that test the SAME concept
- Vary difficulty by changing complexity (number of outcomes, table size)
- Test understanding through different visual representations

### 7.5 Key Diagram Features for Question Generation

**For Tree Diagrams:**
- Number of stages (typically 2 in this workbook)
- Number of outcomes per stage (2-4 common)
- With/without replacement (affects probability values)
- Whether to ask for specific path or sum of paths

**For Venn Diagrams:**
- Total sample size (typically 50-100)
- Relative sizes of sets
- Size of intersection
- Whether "neither" category is included
- Questions can ask for any region or combination

**For Two-Way Tables:**
- Dimensions (2×2 most common, but can be 2×3)
- Which cells are given vs. to be found
- Whether totals are provided
- Conditional probability questions based on rows/columns

**For Box Plots:**
- Presence/absence of outliers
- Shape of distribution (symmetric, skewed)
- Whether to provide data or just plot
- Comparison questions (if multiple plots)

**For Scatter Plots:**
- Number of data points (typically 5-10)
- Strength of correlation
- Whether line of best fit is required
- Type of prediction questions (interpolation vs. extrapolation)

---

## 8. Constraints for Question Variations

### MUST DO:

1. **Only use formulas documented in Section 2**
   - All probability formulas (basic, addition rule, conditional, multiplication, independence)
   - All statistics formulas (mean, median, range, IQR, standard deviation, z-score)
   - Line of best fit equation (y = mx + c)

2. **Match difficulty levels defined in Section 4**
   - Basic: 1-2 steps, direct formula application, small numbers
   - Intermediate: 3-5 steps, may combine concepts, moderate numbers
   - Advanced: 5+ steps, working backwards, combining multiple concepts

3. **Follow solution strategies from Section 5**
   - Use tree diagrams for multi-stage experiments
   - Use Venn diagrams for combined events
   - Use two-way tables for conditional probability
   - Test independence using multiplication check
   - Use five-figure summary for box plots
   - Use fences for outlier detection
   - Follow standard deviation calculation steps
   - Use z-score formula correctly
   - Draw line of best fit through middle of scatter plot points

4. **Use number patterns from Section 6**
   - Probabilities as simplified fractions
   - Small integers (1-100) for counts and surveys
   - Standard deviation to 2 decimal places
   - Z-scores to 1-2 decimal places
   - Appropriate units for context

5. **Maintain question formats from Section 6**
   - "Find the probability of..."
   - "Draw a [diagram type]..."
   - "Determine whether..."
   - "Calculate the..."
   - Include walkthrough and extension variations

6. **Use visual diagram patterns from Section 7**
   - Tree diagrams with proper branching structure
   - Venn diagrams with four regions clearly labeled
   - Two-way tables with totals
   - Box plots showing five-figure summary
   - Scatter plots with appropriate correlation patterns

### MUST NOT:

1. **Introduce formulas not taught in this workbook**
   - No permutations/combinations notation (nPr, nCr)
   - No regression formulas beyond line of best fit by eye
   - No correlation coefficient (r)
   - No population standard deviation (σ)
   - No binomial/normal distribution formulas

2. **Exceed the advanced difficulty benchmark**
   - No problems requiring more than 3 combined concepts
   - No algebraic manipulation beyond basic substitution
   - No complex systems of equations
   - No calculus or advanced statistics

3. **Require methods not demonstrated in worked examples**
   - No systematic counting techniques beyond tree diagrams
   - No formal regression analysis
   - No hypothesis testing
   - No confidence intervals

4. **Use number ranges outside documented patterns**
   - Avoid probabilities as percentages (use fractions/decimals)
   - Avoid extremely large or extremely small numbers
   - Avoid excessive decimal precision
   - Avoid irrational numbers (unless in special contexts like π)

5. **Introduce concepts not in the curriculum**
   - No geometric probability
   - No expected value calculations
   - No variance (only standard deviation)
   - No probability distributions beyond basic discrete
   - No weighted means beyond frequency tables

6. **Create ambiguous or poorly defined problems**
   - Always specify with/without replacement
   - Always provide complete information for calculations
   - Always specify required answer format
   - Always ensure diagrams can be drawn with given information

### QUALITY CHECKS:

Before generating a question variation, verify:

1. **Formula alignment**: Does this question use only formulas from Section 2?
2. **Difficulty appropriate**: Does complexity match Basic/Intermediate/Advanced criteria?
3. **Strategy applicable**: Can students solve this using strategies from Section 5?
4. **Numbers reasonable**: Do values match patterns in Section 6?
5. **Format consistent**: Does question format match those in Section 6?
6. **Diagram valid**: If using diagrams, do they follow patterns in Section 7?
7. **Complete information**: Is all necessary information provided?
8. **Unambiguous**: Is there exactly one correct interpretation?
9. **Solvable**: Can this be solved with the taught methods?
10. **Pedagogically sound**: Does this test genuine understanding, not tricks?

---

## Summary Statistics

- **Total Topics**: 4 major sections (A, B, C, D)
- **Total Subtopics**: 15 (Probability Fundamentals, Multi-Stage Experiments, Venn Diagrams, Addition Rule, Two-Way Table, Conditional Probability, Independent Events, Understanding Data, Measure of Spread, Standard Deviation, Z-score, Bivariate Data, Line of Best Fit)
- **Total Formulas/Theorems**: 15 main formulas
- **Worked Examples Analyzed**: 8 detailed walkthroughs
- **Practice Questions**: 25 questions (numbered 1-25)
- **Difficulty Distribution**:
  - Basic: ~25% (simple probability, basic statistics, identification tasks)
  - Intermediate: ~60% (tree diagrams, Venn diagrams, two-way tables, calculations)
  - Advanced: ~15% (extension questions, combining concepts, working backwards)
- **Page Distribution**:
  - Probability topics: Pages 3-17 (48% of workbook)
  - Statistics topics: Pages 18-31 (52% of workbook)
- **Visual Diagrams Used**:
  - Tree diagrams (3 examples)
  - Venn diagrams (3 examples)
  - Two-way tables (2 examples)
  - Box-and-whisker plots (3 examples)
  - Normal distribution curve (2 examples)
  - Scatter plots (2 examples)


---


# Curriculum Context: Year 10 Mathematics AOS 7 Revision [10.2] Workbook

## Metadata
- Source: Year 10 Mathematics AOS 7 Revision [10.2] Workbook.pdf
- Subject: Mathematics
- Year/Grade Level: Year 10 (Australian Curriculum)
- Topic Area: AOS 7 - Circle Geometry and Measurement
- Analysis Date: 2026-01-07

---

## 1. Topics Covered

### Topic 1: Congruence and Similarity
- **Definition**: Congruence means "exactly the same" (same side length and angles). Similarity means "same shape, different size" (same angles).
- **Key Concepts**:
  - Congruence tests for triangles (SSS, SAS, AAS, RHS)
  - Scale factor between similar figures
  - Ratio of corresponding side lengths
- **Subtopics**:
  - Triangle congruence (SSS, SAS, AAS, RHS cases)
  - Similar figures and scale factor
  - Applications to real-world shadow problems
- **Pages**: 3-6

### Topic 2: Chord Theorems
- **Definition**: Theorems relating to chords (straight lines connecting two points on a circle's circumference)
- **Key Concepts**:
  - Equal chords subtend equal angles
  - Equal distance from center implies equal chord length
  - Perpendicular from center bisects chord
  - Intersecting chords theorem
- **Subtopics**:
  - Chord Theorem 1: Equal chords and equal angles at centre
  - Chord Theorem 2: Equidistant chords from centre
  - Chord Theorem 3: Perpendicular bisector properties
  - Chord Theorem 4: Line through centre perpendicular to chord
  - Chord Theorem 5: Intersecting chords (PA × PB = PC × PD)
- **Pages**: 7-10

### Topic 3: Angle Theorems in Circles
- **Definition**: Theorems relating angles subtended by arcs and chords in circles
- **Key Concepts**:
  - Angle at centre is twice angle at circumference
  - Angles in semi-circle equal 90°
  - Angles in same segment are equal
  - Opposite angles in cyclic quadrilateral sum to 180°
- **Subtopics**:
  - Angle Theorem 1: Angle at centre = 2 × angle at circumference
  - Angle Theorem 2: Angles in semi-circle (90°)
  - Angle Theorem 3: Angles in same segment are equal
  - Angle Theorem 4: Cyclic quadrilateral (opposite angles sum to 180°)
- **Pages**: 11-14

### Topic 4: Tangent Theorems
- **Definition**: Theorems relating to tangent lines (lines that touch circle at exactly one point)
- **Key Concepts**:
  - Tangent perpendicular to radius at point of contact
  - Two tangents from external point are equal length
  - Alternate segment theorem
  - Tangent-secant theorem (power of a point)
- **Subtopics**:
  - Tangent Theorem 1: Tangent ⊥ radius (90° angle)
  - Tangent Theorem 2: Alternate segment theorem
  - Tangent Theorem 3: Two tangents from external point (equal lengths)
  - Tangent Theorem 4: Tangent-secant theorem (PT² = PA × PB)
- **Pages**: 15-21

### Topic 5: Perimeter and Composite Area
- **Definition**: Calculating perimeters and areas of composite shapes
- **Key Concepts**:
  - Perimeter as sum of all sides
  - Circumference formulas (C = πd, C = 2πr)
  - Sector perimeter = arc length + 2r
  - Composite area by addition/subtraction
- **Subtopics**:
  - Perimeter of polygons
  - Circumference of circles
  - Perimeter of sectors
  - Composite shapes combining rectangles, circles, semicircles
- **Pages**: 22-23

### Topic 6: Surface Area of 3D Solids
- **Definition**: Total area of all faces of 3D objects
- **Key Concepts**:
  - Prism surface area formulas
  - Pyramid surface area formulas
  - Cylinder surface area: 2πr² + 2πrh
  - Cone surface area: πr(r + l)
  - Sphere surface area: 4πr²
  - Composite solids (cylinder + cone, etc.)
- **Subtopics**:
  - Rectangular and triangular prisms
  - Square-based pyramids
  - Cylinders
  - Cones
  - Spheres
  - Composite 3D shapes
  - Hollow solids (with cylindrical holes)
- **Pages**: 24-34

### Topic 7: Volume of 3D Solids
- **Definition**: Amount of space occupied by 3D objects
- **Key Concepts**:
  - Prism volume: base area × height
  - Pyramid volume: 1/3 × base area × height
  - Cylinder volume: πr²h
  - Cone volume: 1/3 × πr²h
  - Sphere volume: 4/3 × πr³
  - Composite volumes by addition/subtraction
- **Subtopics**:
  - Rectangular and triangular prisms
  - Pyramids (square and other bases)
  - Cylinders
  - Cones
  - Spheres
  - Composite solids
  - Volumes with material removed (hollow shapes)
- **Pages**: 30-34

---

## 2. Formulas and Theorems

### Circle Terminology
- **Chord**: Straight line connecting any two points on circumference
- **Arc**: Smooth curve joining two endpoints on circumference
- **Sector**: Portion of a circle (like a pizza slice)
- **Segment**: Interior region of circle bounded by chord and arc
- **Tangent**: Line that touches circle at exactly one point
- **Secant**: Line that crosses through circle at two points

### Congruence Tests for Triangles
- **SSS (Side-Side-Side)**: All three sides equal
- **SAS (Side-Angle-Side)**: Two sides and included angle equal
- **AAS (Angle-Angle-Side)**: Two angles and corresponding side equal
- **RHS (Right angle-Hypotenuse-Side)**: Right angle, hypotenuse, and one side equal

### Similarity
- **Scale Factor Formula**: $\text{Scale factor} = \frac{\text{Image length}}{\text{Original length}}$
- **Variables**:
  - Image length = length in enlarged/reduced figure
  - Original length = length in original figure
- **When to Use**: When two figures are similar (same shape, different size)
- **Example from Workbook**: Lighthouse shadow problem - using similar triangles to find height

### Chord Theorem 1: Equal Chords → Equal Angles
- **Statement**: Chords of equal length subtend equal angles at the centre of the circle
- **Formula**: If chord AB = chord CD, then ∠AOB = ∠COD (where O is centre)
- **Converse**: If chords subtend equal angles at centre, then chords are equal length
- **When to Use**: When comparing two chords in same circle

### Chord Theorem 2: Equidistant Chords
- **Statement**: Two chords of equal distance from centre are equal in length
- **Formula**: If perpendicular distance from O to chord AB = perpendicular distance from O to chord DC, then chord AB = chord DC
- **Converse**: If chords are equidistant from centre, they have equal length
- **When to Use**: When perpendicular distances from centre to chords are involved

### Chord Theorem 3: Perpendicular Bisector
- **Statement**: The perpendicular from centre to chord bisects the chord and the angle at centre
- **Formula**: If OE ⊥ chord AB, then AE = EB and ∠AOE = ∠BOE
- **Converse**: If radius bisects chord (or angle at centre), then radius is perpendicular to chord
- **When to Use**: When finding half-chord lengths or using Pythagoras theorem

### Chord Theorem 4: Diameter Bisector
- **Statement**: The line that halves the chord runs through the centre
- **Formula**: Perpendicular bisector of any chord passes through circle centre
- **When to Use**: Locating centre of circle from chord

### Chord Theorem 5: Intersecting Chords
- **Statement**: If two chords intersect at point P inside circle, then PA × PB = PC × PD
- **Formula**: $PA \times PB = PC \times PD$
- **Variables**:
  - PA, PB = segments of first chord
  - PC, PD = segments of second chord
  - P = intersection point
- **When to Use**: Finding unknown segment lengths when chords intersect
- **Example from Workbook**: Question 4 - solving for x using intersecting chords

### Angle Theorem 1: Angle at Centre
- **Statement**: Angle at centre is twice the angle at circumference (when subtended by same arc)
- **Formula**: $\angle AOB = 2 \times \angle ACB$ (where O is centre, A, B, C on circumference)
- **When to Use**: Relating central angles to inscribed angles
- **Example from Workbook**: Question 8 - given ∠ADB = 63°, find ∠AOB = 2×63° = 126°

### Angle Theorem 2: Angle in Semi-circle
- **Statement**: If angle is subtended by diameter, then angle at circumference = 90°
- **Formula**: If AB is diameter, then ∠ACB = 90° (C on circumference)
- **When to Use**: When one side of inscribed angle is a diameter
- **Example from Workbook**: Questions 6, 7 - using 180° property and semi-circle property

### Angle Theorem 3: Angles in Same Segment
- **Statement**: If two or more circumference angles are subtended by same endpoints and lie in same segment, then they are equal
- **Formula**: If angles a and b both subtended by arc AB and in same segment, then a = b
- **When to Use**: Finding equal angles on circumference
- **Example from Workbook**: Question 9 Extension - proving ∠CAD = ∠CBD

### Angle Theorem 4: Cyclic Quadrilateral
- **Statement**: Opposite angles of cyclic quadrilateral add to 180°
- **Formula**:
  - $a + c = 180°$
  - $b + d = 180°$
- **When to Use**: When quadrilateral has all vertices on circle
- **Example from Workbook**: Questions 6, 7 - finding unknown angles using cyclic quadrilateral property

### Tangent Theorem 1: Tangent Perpendicular to Radius
- **Statement**: Angle between tangent and radius at point of contact = 90°
- **Formula**: If line touches circle at P, and O is centre, then tangent ⊥ OP
- **When to Use**: Creating right triangles with tangent, radius, and external line
- **Example from Workbook**: Question 10 - isosceles triangle with tangent

### Tangent Theorem 2: Alternate Segment Theorem
- **Statement**: Angle between tangent and chord = angle on opposite corner (in alternate segment)
- **Formula**: For internal triangle made of chords, angle between tangent and chord = angle on opposite side of triangle
- **When to Use**: When tangent and chord meet at point on circle
- **Example from Workbook**: Question 10 - finding angles using alternate segment theorem

### Tangent Theorem 3: Two Tangents from External Point
- **Statement**: From single point outside circle, only two tangents exist, and distance from point to each tangent point is equal
- **Formula**: If tangents from P touch circle at A and B, then PA = PB
- **When to Use**: Finding equal lengths when two tangents drawn from external point
- **Example from Workbook**: Question 15 - two tangents PQ and PR with PQ = 30 cm, PO = 34 cm

### Tangent Theorem 4: Tangent-Secant (Power of Point)
- **Statement**: For tangent and secant starting at same external point, tangent squared = product of secant segments
- **Formula**: $PT^2 = PA \times PB$
- **Variables**:
  - PT = tangent length from P to circle
  - PA = distance from P to near intersection of secant
  - PB = distance from P to far intersection of secant
- **When to Use**: Finding unknown lengths with tangent-secant configuration
- **Example from Workbook**: Questions 13, 14 - using PT² = PA×PB to solve for unknowns

### Perimeter Formulas

**Polygon Perimeter**:
- **Formula**: $P = a + b + c + d + ...$
- Sum of all side lengths

**Circle Circumference**:
- **Formula**: $C = \pi d$ or $C = 2\pi r$
- **Variables**:
  - d = diameter
  - r = radius
- **Note**: π ≈ 3.14159265... (use π button on calculator)

**Sector Perimeter**:
- **Formula**: $P = \frac{\theta}{360} \times 2\pi r + 2r$
- **Variables**:
  - θ = interior angle in degrees
  - r = radius
- **When to Use**: Finding perimeter of sector (arc length + two radii)
- **Example from Workbook**: Question 17 - composite shape with sector

### Area Formulas (2D)

**Square**: $A = l^2$

**Rectangle**: $A = l \times w$

**Parallelogram**: $A = b \times h$

**Triangle**: $A = \frac{1}{2} \times b \times h$

**Trapezium**: $A = \frac{h(a+b)}{2}$

**Kite/Rhombus**: $A = \frac{1}{2}(x \times y)$ where x, y are diagonals

**Circle**: $A = \pi r^2$

**Sector**:
- **Formula**: $A = \frac{\theta}{360} \times \pi r^2$
- **Variables**:
  - θ = interior angle in degrees
  - r = radius

### Surface Area Formulas (3D)

**Rectangular Prism**:
- **Formula**: $SA = 2lw + 2lh + 2hw$
- **Variables**: l = length, w = width, h = height

**Triangular Prism**:
- **Formula**: $SA = bh + a(b + c + base)$ where a = area of triangular face

**Square-based Pyramid**:
- **Formula**: $SA = b^2 + 4 \times \frac{1}{2}bl$ where b = base side, l = slant height
- Simplified: $SA = b^2 + 2bl$

**Cylinder**:
- **Formula**: $SA = 2\pi r^2 + 2\pi rh$
- **Variables**: r = radius, h = height
- **Components**: Two circular ends + curved surface

**Sphere**:
- **Formula**: $SA = 4\pi r^2$
- **Variables**: r = radius

**Cone**:
- **Formula**: $SA = \pi r(r + l)$
- **Variables**:
  - r = base radius
  - l = slant height
- **Components**: Circular base + curved surface

### Volume Formulas (3D)

**Rectangular Prism**:
- **Formula**: $V = l \times w \times h$

**Oblique Rectangular Prism**:
- **Formula**: $V = A \times h$ (base area × perpendicular height)

**Triangular Prism**:
- **Formula**: $V = \frac{1}{2} \times a \times b \times h$ where a,b are triangle base and height

**Cylinder**:
- **Formula**: $V = \pi r^2h$
- **Variables**: r = radius, h = height

**Square Pyramid**:
- **Formula**: $V = \frac{1}{3} \times b^2 \times h$
- **Variables**: b = base side length, h = perpendicular height

**Right Cone**:
- **Formula**: $V = \frac{1}{3} \times \pi r^2 h$
- **Variables**: r = radius, h = perpendicular height

**Sphere**:
- **Formula**: $V = \frac{4}{3}\pi r^3$
- **Variables**: r = radius

---

## 3. Worked Examples Analysis

### Example 1: Shadow Problem (Similarity)
- **Location**: Page 6, Question 3
- **Topic**: Similar triangles in real-world context
- **Problem Type**: Find height using similar triangle ratios
- **Given Information**:
  - Lighthouse casts shadow 32.0 m long
  - Park sign 1.8 m tall casts shadow 1.5 m long
- **Required**: Height of lighthouse
- **Solution Method**:
  1. Identify that both create similar triangles (same sun angle)
  2. Set up proportion: $\frac{\text{lighthouse height}}{32} = \frac{1.8}{1.5}$
  3. Cross-multiply: lighthouse height × 1.5 = 1.8 × 32
  4. Solve: lighthouse height = (1.8 × 32) ÷ 1.5 = 38.4 m
- **Key Formula Used**: Scale factor = $\frac{1.8}{1.5}$
- **Final Answer**: 38.4 m
- **Answer Format**: Decimal to 1 decimal place
- **Difficulty Level**: Intermediate

### Example 2: Congruence Test Identification
- **Location**: Page 4, Question 1
- **Topic**: Identifying congruence postulates
- **Problem Type**: State which congruence test applies
- **Given Information**: Pairs of triangles with marked equal sides/angles
- **Required**: Name the congruence test (SSS, SAS, AAS, RHS)
- **Solution Method**:
  1. Count number of marked equal sides (S)
  2. Count number of marked equal angles (A)
  3. Check if right angle present (R)
  4. Determine pattern and name test
- **Example a**: Three equal sides marked → SSS
- **Example b**: Two angles and included side → AAS
- **Difficulty Level**: Basic

### Example 3: Intersecting Chords
- **Location**: Page 11, Question 4
- **Topic**: Chord Theorem 5 application
- **Problem Type**: Find value of x using intersecting chords
- **Given Information**: Two chords AB and CD intersecting at P, segments labeled with expressions containing x
- **Required**: Value of x
- **Solution Method**:
  1. Identify intersection point P
  2. Label segments: PA, PB, PC, PD
  3. Apply formula: PA × PB = PC × PD
  4. Substitute given expressions: 2 × 4 = x × (x+7)
  5. Expand: 8 = x² + 7x
  6. Rearrange to quadratic: x² + 7x - 8 = 0
  7. Factor: (x+8)(x-1) = 0
  8. Solve: x = -8 or x = 1 (reject negative as length must be positive)
- **Key Formula Used**: $PA \times PB = PC \times PD$
- **Final Answer**: x = 1
- **Answer Format**: Exact integer
- **Difficulty Level**: Intermediate

### Example 4: Tangent-Secant Theorem
- **Location**: Page 19, Question 14
- **Topic**: Tangent Theorem 4 (Power of Point)
- **Problem Type**: Find unknown lengths using tangent-secant relationship
- **Given Information**: AP = x cm, PC = 0.5 cm, PD = 2 cm, PB = y cm, TD = 5 cm, AT = 8 cm
- **Required**: Find x and y
- **Solution Method**:
  1. Identify tangent (AT or TD) and secant lines
  2. Apply PT² = PA × PB formula
  3. For tangent TD: (5)² = PC × PD → Need to find full secant length
  4. Set up equations using given values
  5. Solve system of equations
- **Key Formula Used**: $PT^2 = PA \times PB$
- **Final Answer**: Multiple values for x and y
- **Answer Format**: Decimal to 2 decimal places
- **Difficulty Level**: Advanced

### Example 5: Angle at Centre Theorem
- **Location**: Page 14, Question 8
- **Topic**: Angle Theorem 1 application
- **Problem Type**: Calculate angles using centre-circumference relationship
- **Given Information**: ∠ADB = 63°, ∠BCD = 112°, points on circle with centre O
- **Required**:
  - a. Calculate ∠AOB
  - b. Calculate ∠BAD
- **Solution Method**:
  1. For part a: Use angle at centre = 2 × angle at circumference
     - ∠AOB = 2 × 63° = 126°
  2. For part b: Use angles in same segment or cyclic quadrilateral
     - ∠BAD = 180° - 112° = 68° (opposite angles in cyclic quad)
- **Key Formula Used**: Central angle = 2 × inscribed angle
- **Final Answer**: a) 126°, b) 68°
- **Answer Format**: Degrees (exact)
- **Difficulty Level**: Intermediate

### Example 6: Composite Area Calculation
- **Location**: Page 26, Question 18a
- **Topic**: Composite area with circles and rectangles
- **Problem Type**: Calculate area of composite shape
- **Given Information**: Shape with two semicircles (diameter 10 cm each) connected by rectangle (10 cm × 10 cm implied)
- **Required**: Area correct to 1 decimal place
- **Solution Method**:
  1. Identify components: rectangle + two semicircles (= full circle)
  2. Calculate rectangle area: 10 × 10 = 100 cm²
  3. Calculate circle area: π × 5² = 25π cm²
  4. Add areas: 100 + 25π ≈ 100 + 78.54 = 178.5 cm²
  5. Alternative approach shown: 3 × (semicircle area) + rectangle
- **Key Formula Used**: Circle area = πr², Rectangle area = l×w
- **Final Answer**: 275.30 cm² (or approximately 278.5 cm² depending on interpretation)
- **Answer Format**: Decimal to 1 decimal place
- **Difficulty Level**: Intermediate

### Example 7: Sector Perimeter
- **Location**: Page 23, Question 17
- **Topic**: Composite perimeter with sector
- **Problem Type**: Calculate perimeter of composite shape (rectangle with quarter-circle)
- **Given Information**: AC = 10 m, AB = 8 m
- **Required**: Perimeter correct to 2 decimal places
- **Solution Method**:
  1. Identify shape: Rectangle ABCD + quarter circle with radius 6 m
  2. Calculate arc length: (90°/360°) × 2πr = (1/4) × 2π(6) = 3π m
  3. Sum visible edges: 8 + 10 + arc + other sides
  4. Perimeter = 8 + (straight edges) + 3π ≈ 32.42 m
- **Key Formula Used**: Arc length = (θ/360) × 2πr
- **Final Answer**: 37.26 m (approximately)
- **Answer Format**: Decimal to 2 decimal places
- **Difficulty Level**: Intermediate to Advanced

### Example 8: Composite 3D Surface Area
- **Location**: Page 28, Question 19
- **Topic**: Surface area of composite solid (rectangular prism + triangular pyramid)
- **Problem Type**: Calculate total surface area
- **Given Information**:
  - Rectangular base: 6 cm × 6 cm
  - Height of prism: 10 cm
  - Triangular pyramid on top with equal faces, edge 7 cm
- **Required**: Surface area
- **Solution Method**:
  1. Calculate rectangular prism faces (excluding top): 4(6×10) + (6×6) = 240 + 36 = 276 cm²
  2. Calculate triangular faces: 4 × (1/2 × 6 × 7) = 4 × 21 = 84 cm²
  3. Total: 276 + 84 = 360 cm²
  4. Note: Top face of prism not counted as it's inside
- **Key Formula Used**: Triangle area = (1/2)bh, Rectangle area = lw
- **Final Answer**: 360 cm²
- **Answer Format**: Exact (integer)
- **Difficulty Level**: Advanced

### Example 9: Composite Volume Subtraction
- **Location**: Page 32, Question 23
- **Topic**: Volume of solid with conical hole
- **Problem Type**: Cylinder volume minus cone volume
- **Given Information**:
  - Cylinder: height 30 cm, diameter 10 cm
  - Conical hole: same base and height as cylinder
- **Required**: Volume of remaining wood, correct to 1 decimal place
- **Solution Method**:
  1. Calculate cylinder volume: V = πr²h = π(5)²(30) = 750π cm³
  2. Calculate cone volume: V = (1/3)πr²h = (1/3)π(5)²(30) = 250π cm³
  3. Subtract: 750π - 250π = 500π ≈ 1570.8 cm³
- **Key Formula Used**: Vcylinder = πr²h, Vcone = (1/3)πr²h
- **Final Answer**: 1570.8 cm³
- **Answer Format**: Decimal to 1 decimal place
- **Difficulty Level**: Intermediate

### Example 10: Frustum Surface Area
- **Location**: Page 33, Question 24
- **Topic**: Surface area of frustum (truncated cone)
- **Problem Type**: Calculate surface area of frustum with given dimensions
- **Given Information**:
  - Top circular rim diameter: 45 cm
  - Base circular diameter: 25 cm
  - Vertical depth: 24 cm
- **Required**: Total surface area (nearest integer)
- **Solution Method**:
  1. Identify as frustum of cone
  2. Calculate top circle area: π(22.5)²
  3. Calculate bottom circle area: π(12.5)²
  4. Calculate slant height using Pythagoras: l² = 24² + (22.5-12.5)²
  5. Calculate curved surface area of frustum
  6. Sum all areas
- **Key Formula Used**: Frustum curved surface = π(r₁+r₂)l
- **Final Answer**: Integer value
- **Answer Format**: Nearest integer
- **Difficulty Level**: Advanced

---

## 4. Difficulty Benchmarks

### Basic Level
- **Characteristics**:
  - Direct application of single formula
  - Clearly stated which theorem to use
  - All needed values explicitly given
  - 1-2 step problems
  - Recognition tasks (identify congruence test)
- **Typical Number Ranges**:
  - Integers: 1-20
  - Simple decimals: 1 decimal place
  - Nice angles: 30°, 45°, 60°, 90°, 180°
- **Steps Required**: 1-2 steps
- **Formulas Used**: Single formula, direct substitution
- **Reference Examples**:
  - Question 1 (identify congruence tests - SSS, AAS)
  - Question 8a (angle at centre = 2 × 63° = 126°)
  - Simple perimeter calculations with given dimensions

### Intermediate Level
- **Characteristics**:
  - Multiple steps required
  - Need to identify which theorem applies
  - Some values must be calculated before main calculation
  - May require Pythagoras or algebra
  - 3-4 step problems
  - Composite shapes with 2 components
- **Typical Number Ranges**:
  - Integers: up to 100
  - Decimals: 1-2 decimal places
  - Angles: any value 0°-360°
  - May involve π (leave in terms of π or use calculator)
- **Steps Required**: 3-4 steps
- **Formulas Used**: May combine 2 formulas or use theorem + calculation
- **Reference Examples**:
  - Question 3 (shadow problem with similar triangles)
  - Question 4 (intersecting chords with algebra)
  - Question 17 (sector perimeter)
  - Question 18 (composite area calculations)
  - Question 19 (composite surface area)
  - Question 23 (volume subtraction)

### Advanced Level
- **Characteristics**:
  - Multi-step problems (5+ steps)
  - Must determine strategy independently
  - Combines multiple theorems
  - Requires algebraic manipulation (quadratics, simultaneous equations)
  - Proof or "show that" questions
  - Complex composite shapes (3+ components)
  - Indirect reasoning required
- **Typical Number Ranges**:
  - Larger integers: up to 1000
  - Decimals: 2-3 decimal places precision
  - Algebraic expressions (x, x+1, 2x+10, etc.)
  - Exact values with surds (√2, √3) possible
- **Steps Required**: 5+ steps, may have multiple parts
- **Formulas Used**: Multiple formulas, may need to derive relationships
- **Reference Examples**:
  - Question 5 (intersecting chords with similarity reasoning)
  - Question 9 Extension (prove angles equal using multiple theorems)
  - Question 14 (tangent-secant with multiple unknowns)
  - Question 20 Extension (composite solid with cylindrical hole)
  - Question 24 (frustum surface area calculation)

---

## 5. Solution Strategies Taught

### Strategy 1: Identifying Similar Triangles
- **When Used**: Real-world problems with shadows, scaling, proportions
- **Steps**:
  1. Identify the two triangles in the scenario
  2. Confirm they are similar (same angles - often due to parallel lines or same sun angle)
  3. Label corresponding sides on both triangles
  4. Set up proportion: $\frac{\text{side 1 of triangle A}}{\text{corresponding side 1 of triangle B}} = \frac{\text{side 2 of triangle A}}{\text{corresponding side 2 of triangle B}}$
  5. Cross-multiply and solve for unknown
- **Example Problem Types**:
  - Shadow problems
  - Scale model problems
  - Map distance problems
- **Common Mistakes to Avoid**:
  - Matching non-corresponding sides
  - Forgetting to check triangles are actually similar

### Strategy 2: Circle Theorem Selection
- **When Used**: Any circle geometry problem
- **Steps**:
  1. Draw or examine the diagram carefully
  2. Identify key features: centre, radii, chords, tangents, arcs
  3. Look for these configurations:
     - Angle at centre and angle at circumference from same arc → use 2:1 ratio
     - Diameter present → check for 90° angle
     - Two angles in same segment → they're equal
     - Quadrilateral in circle → opposite angles sum to 180°
     - Tangent meeting radius → 90° angle
     - Two tangents from external point → equal lengths
     - Tangent and secant from same point → use PT² = PA×PB
     - Two chords intersecting → use PA×PB = PC×PD
  4. Apply the identified theorem
  5. Use algebra if variables present
- **Example Problem Types**:
  - Finding unknown angles
  - Finding unknown lengths
  - Proving angle relationships
- **Common Mistakes to Avoid**:
  - Confusing angle at centre with angle at circumference
  - Forgetting which angles are equal in same segment

### Strategy 3: Composite Area/Volume by Components
- **When Used**: Shapes made from multiple basic shapes
- **Steps**:
  1. Identify all component shapes (rectangles, triangles, circles, sectors, etc.)
  2. Determine whether to ADD or SUBTRACT:
     - If shapes don't overlap → ADD all areas
     - If one shape cut out of another → SUBTRACT
     - If shaded region between shapes → Large - Small
  3. Calculate area/volume of each component separately
  4. Combine using addition/subtraction as determined
  5. Apply units correctly (cm², m³, etc.)
- **Example Problem Types**:
  - Rectangle with semicircular ends
  - Circle with square removed
  - Cylinder with conical hole
  - Prism topped with pyramid
- **Common Mistakes to Avoid**:
  - Counting overlapping regions twice
  - Wrong operation (adding when should subtract)
  - Forgetting to account for hidden faces in 3D

### Strategy 4: Two-Step Right Triangle (Pythagoras + Application)
- **When Used**: Finding slant heights, missing dimensions in 3D shapes
- **Steps**:
  1. Identify where right triangle exists (often hidden in 3D diagram)
  2. Label the three sides: hypotenuse, opposite, adjacent
  3. Apply Pythagoras: a² + b² = c²
  4. Solve for unknown side
  5. Use this calculated value in main formula (surface area, volume, etc.)
- **Example Problem Types**:
  - Finding slant height of cone
  - Finding diagonal in rectangular prism
  - Finding perpendicular distance from centre to chord
- **Common Mistakes to Avoid**:
  - Using wrong sides in Pythagoras
  - Confusing perpendicular height with slant height

### Strategy 5: Algebraic Setup for Circle Theorems
- **When Used**: Circle problems with expressions containing variables
- **Steps**:
  1. Identify which circle theorem applies
  2. Write the theorem relationship (equation)
  3. Substitute given expressions (e.g., x, x+7, 2x+10)
  4. Expand and simplify
  5. Rearrange to standard form (often quadratic: ax² + bx + c = 0)
  6. Solve using factoring, quadratic formula, or other method
  7. Check solutions make sense (reject negative lengths, angles > 180°, etc.)
- **Example Problem Types**:
  - Intersecting chords with variable segments
  - Tangent-secant with expressions
  - Angles expressed algebraically in cyclic quadrilaterals
- **Common Mistakes to Avoid**:
  - Algebraic errors in expansion
  - Accepting impossible solutions (negative lengths)
  - Not checking answer in original context

### Strategy 6: Working Backwards from Required Answer
- **When Used**: Complex multi-step problems, especially "show that" questions
- **Steps**:
  1. Read what needs to be proved or found
  2. Identify what formula will give that result
  3. List what values are needed for that formula
  4. Work backwards: what do I need to find first? second?
  5. Create a solution pathway from given → intermediate → final
  6. Execute the plan forward
- **Example Problem Types**:
  - Prove two angles are equal
  - Show that a value equals specific number
  - Extension questions
- **Common Mistakes to Avoid**:
  - Assuming what needs to be proved
  - Circular reasoning

---

## 6. Common Patterns

### Number Patterns Used
- **Integers**:
  - Small: 1-20 (basic problems, congruence)
  - Medium: 20-100 (intermediate calculations, angles)
  - Large: 100-1000 (surface area, volume)
- **Decimals**:
  - 1 decimal place: 1.5, 1.8, 32.0 (measurement contexts)
  - 2 decimal places: 0.5, 2.25, 38.54 (precise calculations, answers)
  - 3+ decimal places: rare, only when using π (3.14159...)
- **Fractions**:
  - Halves: 1/2 (triangle area, trapezium)
  - Thirds: 1/3 (pyramid/cone volume)
  - Unit fractions: 1/2, 1/3, 1/4 in formulas
- **Special Values**:
  - π (use calculator π button, or 3.14)
  - Common angles: 30°, 45°, 60°, 90°, 180°, 360°
  - Right angles marked with square symbol
- **Measurements**:
  - Lengths: 1-50 cm typical, up to 100 m for real-world
  - Areas: 10-500 cm²
  - Volumes: 100-2000 cm³
  - Angles: 0°-360°

### Question Formats
- **Format 1**: "Calculate/Find the [measurement] of..."
  - Diagram provided with labeled dimensions
  - May have some dimensions unlabeled (to find)
  - Answer requires calculation

- **Format 2**: "State the postulate/theorem that can be used to conclude..."
  - Diagram with marked equal sides/angles
  - Tests knowledge of congruence tests or circle theorems
  - Answer is name of theorem (SSS, Tangent Theorem 1, etc.)

- **Format 3**: "Work out the size of each angle marked with a letter. Give reasons."
  - Circle diagram with multiple angles to find
  - Requires stating which theorem used for each
  - Tests understanding of relationships

- **Format 4**: "Show that..." or "Prove that..." (Extension)
  - Requires logical reasoning
  - Must justify each step
  - Higher difficulty

- **Format 5**: "Find the value of x"
  - Diagram with algebraic expressions
  - Requires setting up equation
  - Solve for variable

- **Format 6**: "Calculate [measurement], giving your answer correct to [precision]"
  - Specifies required precision (1 d.p., 2 d.p., nearest integer)
  - Often involves π or square roots
  - Must round appropriately

### Answer Expectations
- **Exact vs Approximate**:
  - Exact when possible for angles (e.g., 126°, not 126.0°)
  - Exact for integer lengths when no π involved
  - Approximate (decimal) when π involved or specified precision
  - May leave in terms of π for some area/perimeter questions

- **Units**:
  - Always required for measurements
  - Length: cm, m (given in question)
  - Area: cm², m² (squared units)
  - Volume: cm³, m³ (cubed units)
  - Angles: ° (degrees symbol)
  - Missing units → incorrect answer

- **Significant Figures/Decimal Places**:
  - Follow question instructions ("correct to 1 decimal place")
  - If not specified, match precision of given data or use 2 d.p.
  - Angles: usually exact (no decimals unless calculated)
  - Measurements with π: 1-2 decimal places standard

- **Working Required**:
  - Yes - show all steps for complex calculations
  - Must show formula before substitution
  - Must show intermediate steps
  - "Give reasons" means state theorem names
  - Extension questions require full justification

---

## 7. Visual Diagram Patterns

### 7.1 Diagram Configuration → Concept Mapping

| Concept/Theorem | Diagram Configuration | Key Visual Elements | How to Recognize |
|-----------------|----------------------|---------------------|------------------|
| SSS Congruence | Two triangles side by side | All three sides marked equal (tick marks) | Three pairs of equal marks |
| SAS Congruence | Two triangles | Two sides + included angle marked equal | Side-Angle-Side pattern |
| AAS Congruence | Two triangles | Two angles + one side marked equal | Angle-Angle-Side pattern |
| RHS Congruence | Two right triangles | Right angle + hypotenuse + one side equal | Square corner + equal marks |
| Similar Triangles | Two triangles, different sizes | Same angles, proportional sides | Same shape, different size, may be rotated |
| Chord Theorem 1 | Circle with two chords from centre | Equal chord lengths marked | Two chords, tick marks showing equality |
| Chord Theorem 2 | Circle with perpendiculars from centre to chords | Perpendicular marks, equal distances | Right angle marks, equal perpendicular distances |
| Chord Theorem 3 | Circle with perpendicular from centre to chord | Perpendicular bisector | Right angle mark at chord midpoint |
| Chord Theorem 5 (Intersecting) | Circle with two chords crossing inside | X-pattern inside circle | Two chords intersect at point P inside |
| Angle at Centre | Circle with angle at centre and circumference | Two angles subtended by same arc | Centre labeled O, both angles from same arc |
| Angle in Semi-circle | Circle with diameter | Angle on circumference, one side is diameter | Diameter shown, angle on opposite side |
| Angles in Same Segment | Circle with multiple angles in one segment | Multiple angles between same two endpoints | All angles touch same two points on circle |
| Cyclic Quadrilateral | Quadrilateral inscribed in circle | Four vertices on circle | All four corners touch circle |
| Tangent ⊥ Radius | Circle with tangent line | Right angle mark where tangent meets radius | Line touches at one point, 90° mark |
| Alternate Segment | Circle with tangent and chord | Triangle formed with tangent | Tangent meets chord at circle point |
| Two Tangents Equal | Circle with external point P | Two tangent lines from same point | Point outside, two lines touching circle |
| Tangent-Secant | Circle with tangent and secant from same point | One line touches, one crosses | External point with tangent + secant |
| Composite Area (subtraction) | Two shapes, one inside other | Shaded region between shapes | Inner shape different color/shading |
| Sector | Circle with two radii | Pie-slice shape, angle marked | Two radii, arc, shaded sector |
| Annulus | Two concentric circles | Ring shape | Two circles, same centre, different radii |

### 7.2 Visual Elements and Their Meaning

| Visual Element | What It Indicates | Testing Aspect |
|----------------|-------------------|----------------|
| **Shaded region** | "Calculate this area/volume" | Student must identify what to compute |
| **Variable label (x, ?)** | "Find this value" | This is the unknown to solve for |
| **Right angle mark (□)** | Perpendicular lines, 90° | Pythagoras or right triangle properties apply |
| **Equal marks (tick marks)** | Equal lengths | These sides/segments are the same length |
| **Equal angle arcs** | Equal angles | These angles have the same measure |
| **Dimension arrows** | Given measurements | These values are provided for calculation |
| **Dashed lines** | Construction lines / auxiliary lines | May indicate radius, perpendicular, or hidden edges |
| **Centre point (O, •)** | Circle centre | Radius relationships, central angles apply |
| **Letters at vertices** | Points for reference | Use in naming angles, segments, theorems |
| **Parallel marks (>> or ǁ)** | Parallel lines | Corresponding angles, similar triangles may apply |

### 7.3 Standard Diagram Patterns by Topic

#### Circle Theorems - Chords:
```
Pattern: Circle + Chords
├── Two chords from centre → Equal chords = equal angles (Theorem 1)
├── Two chords with perpendiculars → Equidistant = equal length (Theorem 2)
├── One chord with perpendicular from centre → Bisects chord (Theorem 3)
├── Chord with perpendicular bisector → Passes through centre (Theorem 4)
└── Two chords intersecting inside → PA×PB = PC×PD (Theorem 5)
```

#### Circle Theorems - Angles:
```
Pattern: Circle + Angles
├── Centre angle + circumference angle from same arc → Centre = 2×Circum (Theorem 1)
├── Angle with diameter as one side → Angle = 90° (Theorem 2)
├── Multiple angles in same segment → All equal (Theorem 3)
└── Quadrilateral with vertices on circle → Opposite angles sum 180° (Theorem 4)
```

#### Circle Theorems - Tangents:
```
Pattern: Circle + Tangent Lines
├── Tangent + radius to contact point → 90° angle (Theorem 1)
├── Tangent + chord at contact → Alternate segment (Theorem 2)
├── Two tangents from external point → Equal lengths (Theorem 3)
└── Tangent + secant from same point → PT² = PA×PB (Theorem 4)
```

#### Composite 2D Shapes:
```
Pattern: Multiple shapes combined
├── Rectangle + semicircles on ends → Oblong with rounded ends
├── Square + circle inside → Shaded corners
├── Circle + square inside → Shaded curved regions
├── Rectangle + quarter circles → Rounded corners
└── Sector + triangle → Combined area calculation
```

#### Composite 3D Solids:
```
Pattern: Multiple 3D shapes stacked/connected
├── Rectangular prism + pyramid on top → Building/tower shape
├── Cylinder + cone on top → Silo, rocket, lighthouse
├── Cylinder + hemisphere → Tank, dome, capsule
├── Cylinder with cylindrical hole → Hollow pipe
└── Prism + frustum → Complex composite
```

### 7.4 Diagram Variations in Workbook

Document how the workbook varies diagrams for the same concept:

| Concept | Variation 1 | Variation 2 | Variation 3 |
|---------|-------------|-------------|-------------|
| Congruent triangles | Side by side, same orientation | One rotated 180° | One reflected |
| Similar triangles | Vertical alignment (shadow) | Side by side comparison | Nested (one inside other) |
| Intersecting chords | Perpendicular intersection | Oblique intersection | One horizontal, one diagonal |
| Angle at centre | Full circle shown | Partial circle (arc visible) | With quadrilateral formed |
| Tangent problems | Single tangent horizontal | Two tangents from external point | Tangent with secant |
| Composite area | Rectangle + semicircles (horizontal) | Rectangle + quarter circles (corners) | Circle + inscribed square |
| Composite 3D | Prism + pyramid (aligned) | Cylinder + cone | Solid with hole removed |
| Cyclic quadrilateral | Square-ish in circle | Kite-like in circle | Irregular quad in circle |

#### Important Visual Recognition Notes:

1. **Shading indicates calculation target**: If region is shaded, calculate THAT area/volume
2. **Tick marks mean equality**: Same number of ticks = same length
3. **Arc marks on angles mean equality**: Same arc marks = same angle measure
4. **Dashed vs solid lines**: Dashed often means hidden/construction, solid means actual edge
5. **Centre marked with O or dot**: Identifies circle centre for radius/central angle theorems
6. **Right angle marks are critical**: Always indicates 90°, enables Pythagoras
7. **Letters establish relationships**: ∠AOB means "angle at O between points A and B"

This section ensures the question generator understands that **diagrams ARE the question** - the visual configuration indicates which theorem/formula to apply, and variations test whether students recognize the same concept in different orientations or configurations.

---

## 8. Constraints for Question Variations

### MUST DO:
1. **Only use formulas documented in Section 2**
   - All circle theorems listed (Chord 1-5, Angle 1-4, Tangent 1-4)
   - All area formulas (square, rectangle, parallelogram, triangle, trapezium, kite, circle, sector)
   - All surface area formulas (prisms, pyramids, cylinder, cone, sphere)
   - All volume formulas (prisms, pyramids, cylinder, cone, sphere)
   - Perimeter and circumference formulas
   - Similarity and congruence concepts

2. **Match difficulty levels defined in Section 4**
   - Basic: 1-2 steps, direct application, integers 1-20, simple decimals
   - Intermediate: 3-4 steps, identify theorem, integers up to 100, may use algebra
   - Advanced: 5+ steps, multiple theorems, algebraic expressions, proofs

3. **Follow solution strategies from Section 5**
   - Identifying similar triangles (proportions)
   - Circle theorem selection (match diagram to theorem)
   - Composite area/volume by components (add/subtract)
   - Two-step right triangle (Pythagoras + application)
   - Algebraic setup for circle theorems
   - Working backwards from required answer

4. **Use number patterns from Section 6**
   - Integers: 1-20 (basic), 20-100 (intermediate), 100-1000 (advanced)
   - Decimals: 1 d.p. for measurements, 2 d.p. for calculated answers
   - Use π correctly (calculator value, not 3.14 unless specified)
   - Common angles: 30°, 45°, 60°, 90°, 180°, 360°
   - Realistic measurements (cm, m for length; cm², m² for area; cm³, m³ for volume)

5. **Maintain question formats from Section 6**
   - "Calculate/Find..." with diagram
   - "State the theorem/postulate..." for identification
   - "Work out the size of each angle... Give reasons"
   - "Show that..." for extension/proof
   - "Find the value of x" for algebra
   - Specify precision: "correct to 1 decimal place"

6. **Follow answer expectation patterns from Section 6**
   - Include units (cm, m, °, cm², m², cm³, m³)
   - Specify precision requirements
   - Expect working shown for multi-step problems
   - Require theorem names when "give reasons" asked

7. **Use diagram patterns from Section 7**
   - Match visual configuration to theorem being tested
   - Use standard visual elements (shading, tick marks, right angle symbols, dashed lines)
   - Vary orientation/configuration while testing same concept

### MUST NOT:
1. **Introduce formulas not taught in this workbook**
   - No trigonometry beyond right triangles (sin, cos, tan NOT in this workbook)
   - No radians (only degrees for angles)
   - No calculus concepts
   - No vectors or coordinate geometry
   - No complex numbers or surds (√2, √3) except incidentally in answers

2. **Exceed the advanced difficulty benchmark**
   - Maximum 7-8 steps
   - No university-level mathematics
   - No proofs requiring formal symbolic logic
   - Keep algebra at Year 10 level (quadratics, simultaneous equations max)

3. **Require methods not demonstrated in worked examples**
   - Don't require trigonometric ratios (sin/cos/tan)
   - Don't require logarithms or exponentials
   - Don't require matrix operations
   - Don't require calculus (derivatives, integrals)
   - Stick to methods shown: Pythagoras, algebra, circle theorems, area/volume formulas

4. **Use number ranges outside documented patterns**
   - Avoid very large numbers (>10,000) or very small decimals (<0.01)
   - Avoid irrational answers unless approximate decimal requested
   - Keep angles in range 0°-360°
   - Avoid negative lengths or angles (physically impossible)

5. **Mix incompatible units**
   - Don't mix cm and m without conversion
   - Don't use imperial units (inches, feet) - stick to metric
   - Don't mix degrees and radians

6. **Create impossible geometric configurations**
   - Triangle inequality must hold (sum of two sides > third side)
   - Angles in triangle must sum to 180°
   - Angles in quadrilateral must sum to 360°
   - Circle configurations must be geometrically valid

7. **Omit necessary information**
   - Always provide enough information to solve
   - Don't create under-determined problems
   - Label diagrams clearly
   - Specify precision requirements

8. **Violate realistic measurement constraints**
   - Areas should match reasonable calculation from given lengths
   - Volumes should match reasonable calculation from given dimensions
   - Scale factors should be positive and reasonable (not 0.001 or 1000)

---

## 9. Topic-Specific Constraints

### Congruence and Similarity
- Use only SSS, SAS, AAS, RHS congruence tests
- Similarity problems should have clear context (shadows, scale models)
- Scale factors between 0.1 and 10 (typically 0.5 to 5)
- Corresponding sides clearly identifiable

### Circle Theorems - Chords
- Chord lengths realistic for circle size (not longer than diameter)
- Intersecting chord problems: ensure PA×PB = PC×PD yields solvable values
- When using perpendiculars, ensure they create valid right triangles

### Circle Theorems - Angles
- Central angles 0°-360°
- Circumference angles 0°-180° (max semi-circle)
- Cyclic quadrilateral opposite angles must sum to 180°
- Ensure angle relationships are geometrically valid

### Circle Theorems - Tangents
- Tangent point always on circle
- External point always outside circle
- For PT² = PA×PB, ensure values create positive, real solutions
- Tangent lengths reasonable compared to circle radius

### Perimeter and Area
- Composite shapes: max 3 component shapes for intermediate, 4-5 for advanced
- Sector angles: multiples of 30° or 45° preferred (easier to work with)
- When using π, specify whether to leave in terms of π or calculate decimal

### Surface Area and Volume
- 3D composite shapes: max 2 shapes combined (intermediate), 3 shapes (advanced)
- Ensure all dimensions provided or calculable
- Hollow shapes: hole smaller than outer shape
- Frustum problems: ensure top diameter < bottom diameter

---

## Summary Statistics

- **Total Topics**: 7 major topics
  1. Congruence and Similarity
  2. Chord Theorems
  3. Angle Theorems
  4. Tangent Theorems
  5. Perimeter and Composite Area
  6. Surface Area of 3D Solids
  7. Volume of 3D Solids

- **Total Formulas/Theorems**: 40+
  - 4 Congruence tests
  - 5 Chord theorems
  - 4 Angle theorems
  - 4 Tangent theorems
  - 6 Area formulas (2D shapes)
  - 6 Surface area formulas (3D shapes)
  - 7 Volume formulas (3D shapes)
  - Perimeter/circumference formulas

- **Worked Examples Analyzed**: 10 detailed examples covering all difficulty levels

- **Difficulty Distribution**:
  - ~30% Basic (recognition, 1-2 steps, direct application)
  - ~50% Intermediate (3-4 steps, some reasoning, multiple components)
  - ~20% Advanced (5+ steps, proofs, complex algebra, multi-part)

- **Question Types**:
  - Calculation questions: ~60%
  - "Find the value of x" (algebra): ~20%
  - "Give reasons" (theorem identification): ~10%
  - Extension/"Show that": ~10%

- **Key Mathematical Skills Required**:
  - Circle geometry theorem application
  - Algebraic manipulation (linear and quadratic equations)
  - Pythagoras theorem
  - Similarity and proportion
  - Composite area and volume calculation
  - Formula substitution
  - Geometric reasoning

- **Units Used**:
  - Length: cm, m
  - Area: cm², m²
  - Volume: cm³, m³
  - Angle: degrees (°)

- **Precision Expectations**:
  - Exact for angles (when possible)
  - 1-2 decimal places for measurements
  - Nearest integer for some composite calculations
  - May leave in terms of π when appropriate

---

## Notes for Question Generation

1. **Diagram Quality is Essential**: Every geometry question REQUIRES a clear, accurate diagram. The visual representation IS the question in many cases.

2. **Progressive Difficulty**: Start with recognition/identification (basic), move to calculation with guidance (intermediate), end with independent problem-solving (advanced).

3. **Realistic Contexts**: When using real-world scenarios (shadows, buildings, containers), ensure measurements are realistic and relatable.

4. **Algebraic Progression**:
   - Basic: no algebra, direct substitution
   - Intermediate: simple linear equations, one variable
   - Advanced: quadratic equations, multiple variables, proof

5. **Answer Precision Matters**: Always specify required precision. Don't accept "approximately 38" when "38.4 m" or "38.45 m to 2 d.p." is expected.

6. **Theorem Naming Convention**: Use consistent naming (Chord Theorem 1, Angle Theorem 2, etc.) as shown in workbook.

7. **Multi-Part Questions**: Extension questions often have parts a, b, c building on each other. Part a establishes value needed for part b.

8. **"Give Reasons" Philosophy**: Students must justify angle calculations by naming the theorem used. This tests understanding, not just calculation.

9. **Composite Shape Strategy**: Always possible to break into basic shapes. The challenge is identifying which shapes and whether to add or subtract.

10. **Common Student Errors to Avoid in Answer Key**:
    - Using diameter instead of radius (or vice versa)
    - Forgetting to square radius in circle formulas
    - Confusing surface area with volume
    - Accepting negative solutions for lengths
    - Arithmetic errors with π (using 3.14 vs calculator π button)


---


# Curriculum Context: Year 10 Mathematics AOS 8 Revision [10.3] Workbook

## Metadata
- Source: Year 10 Mathematics AOS 8 Revision [10.3] Workbook.pdf
- Subject: Mathematics
- Year/Grade Level: Year 10 (Australian Curriculum)
- Topic Area: AOS 8 - Polynomials and Polynomial Graphs
- Analysis Date: 2026-01-08
- Total Pages: 25

---

## 1. Topics Covered

### Topic 1: Polynomial Fundamentals
- **Definition**: Functions of the form $f(x) = a_nx^n + a_{n-1}x^{n-1} + a_{n-2}x^{n-2} + ... + a_1x + a_0$ where all powers are positive integers (whole numbers)
- **Key Concepts**:
  - Polynomial notation and terminology
  - Degree of polynomial
  - Coefficients
  - Leading term
- **Subtopics**: Expanding and simplifying polynomials
- **Pages**: 3

### Topic 2: Long Division of Polynomials
- **Definition**: Algorithm for dividing polynomial by another polynomial to find quotient and remainder
- **Key Concepts**:
  - Divisor, dividend, quotient, remainder
  - Division algorithm formula
  - Systematic column method
- **Subtopics**: Multi-step polynomial division
- **Pages**: 4

### Topic 3: Short Division (Synthetic Division)
- **Definition**: Simplified method for dividing polynomial by linear factor $(x-a)$
- **Key Concepts**:
  - Abbreviated notation using coefficients only
  - Visual layout with boxes
  - Identifying quotient coefficients and remainder
- **Subtopics**: Division by $(x-c)$ where c is a constant
- **Pages**: 6

### Topic 4: Remainder Theorem
- **Definition**: Method to find remainder without full division by substituting x-value
- **Key Concepts**:
  - Direct substitution to find remainder
  - Division by $(x-a)$: remainder is $f(a)$
  - Division by $(ax-b)$: remainder is $f(\frac{b}{a})$
  - Solving for unknown coefficients using remainder conditions
- **Subtopics**:
  - Finding remainder when dividing by linear factors
  - Using remainder theorem to determine unknown values
  - Extension: high powers like $x^{101}$
- **Pages**: 7-8

### Topic 5: Factor Theorem
- **Definition**: If $f(a) = 0$, then $(x-a)$ is a factor of $f(x)$
- **Key Concepts**:
  - Relationship between roots and factors
  - Testing if linear expression is a factor
  - Finding unknown coefficients using factor conditions
  - Distinction between factor (result is 0) and non-factor (result is not 0)
- **Subtopics**:
  - Determining if $(x-a)$ is a factor
  - Finding values that make expressions factors
  - "Not a factor" determination
- **Pages**: 9

### Topic 6: Solving Polynomial Equations
- **Definition**: Finding all values of x where polynomial equals zero (roots/x-intercepts)
- **Key Concepts**:
  - Null Factor Law: if $a \times b \times c = 0$, then at least one factor equals zero
  - Factorised form to find roots
  - Repeated roots (multiplicity)
  - Using given roots to construct polynomials
- **Subtopics**:
  - Finding roots from factorised form
  - Constructing polynomial from given roots
  - Multi-part problems involving roots and point conditions
- **Pages**: 10-11

### Topic 7: Sketching Cubic Graphs in Point of Inflection (POI) Form
- **Definition**: Graphs of form $y = a(x-h)^n + k$ where n is odd positive integer (typically 3)
- **Key Concepts**:
  - All cubics with odd power look like "cubic" shape
  - Point of inflection $(h,k)$ - where curve changes concavity
  - Positive $a$: goes up to right; Negative $a$: goes down to right
  - Finding intercepts: x-intercept (set $y=0$), y-intercept (set $x=0$)
  - Labeling turning point and intercepts
- **Subtopics**:
  - Identifying point of inflection from equation
  - Finding x and y intercepts
  - Sketching shape based on sign of coefficient
  - Extension: determining coefficients from graph
- **Pages**: 12-15

### Topic 8: Sketching Quartic Graphs in Turning Point Form
- **Definition**: Graphs of form $y = a(x-h)^n + k$ where n is even positive integer (typically 4)
- **Key Concepts**:
  - All quartics with even power look like "quadratic" shape (U or upside-down U)
  - Turning point $(h,k)$ - minimum or maximum
  - Positive $a$ ($a > 0$): opens upward (smiley face)
  - Negative $a$ ($a < 0$): opens downward (sad face)
  - Finding vertex and intercepts
- **Subtopics**:
  - Identifying turning point from equation
  - Determining if graph opens up or down
  - Finding intercepts
  - Extension: negative coefficients
- **Pages**: 16-18

### Topic 9: Graphs of Factorised Cubics
- **Definition**: Cubic polynomials in fully factorised form showing all linear factors
- **Key Concepts**:
  - All distinct linear factors correspond to x-intercepts
  - Repeated linear factors correspond to turning point AND x-intercept
  - Example: $f(x) = (x-a)(x-b)(x-c)$ has x-intercepts at $x=a, b, c$
  - Example: $f(x) = (x-a)^2(x-b)$ has turning point at $x=a$ and x-intercept at $x=b$
  - Positive vs negative leading coefficient determines end behavior
- **Subtopics**:
  - Identifying x-intercepts from factors
  - Recognizing repeated roots as turning points
  - Positive cubic: goes up first vs Negative cubic: goes down first
  - Sketching complete graphs with all features labeled
- **Pages**: 19-20

### Topic 10: Application of Polynomials
- **Definition**: Real-world problems modeled by polynomial functions
- **Key Concepts**:
  - Height/distance functions
  - Finding where functions meet specific conditions (e.g., ground level)
  - Finding maximum/minimum values (turning points)
  - Comparing multiple polynomial models
  - Domain restrictions based on context
- **Subtopics**:
  - Structure height problems
  - Finding intersection points of two curves
  - Optimization (tallest point, same height)
  - Extension: inscribed rectangles and parabolas
- **Pages**: 24-25

---

## 2. Formulas and Theorems

### Division Algorithm
- **Statement**: When dividing polynomials, the relationship between dividend, divisor, quotient, and remainder
- **Formula**: $\frac{\text{Dividend}}{\text{Divisor}} = \text{Quotient} + \frac{\text{Remainder}}{\text{Divisor}}$
- **Variables**:
  - Dividend = polynomial being divided
  - Divisor = polynomial dividing into dividend
  - Quotient = result of division (polynomial)
  - Remainder = what's left over (polynomial of lower degree than divisor)
- **When to Use**: Any polynomial division problem to express final answer
- **Example from Workbook**: $\frac{100}{7} = 14 + \frac{2}{7}$ (Page 4)

### Remainder Theorem (Form 1)
- **Statement**: When polynomial $f(x)$ is divided by $(x-a)$, the remainder is $f(a)$
- **Formula**: Remainder $= f(a)$ when dividing by $(x-a)$
- **Variables**:
  - $f(x)$ = polynomial function
  - $a$ = the value that makes divisor equal to zero (from $x-a=0$, so $x=a$)
- **When to Use**: Finding remainder without performing full division; divisor is of form $(x-a)$
- **Example from Workbook**: Finding remainder when $f(x) = -3x^3 + 4x^2 - 5x + 12$ is divided by $2x-3$, substitute $x = \frac{3}{2}$ (Page 7)

### Remainder Theorem (Form 2)
- **Statement**: When polynomial $f(x)$ is divided by $(ax-b)$, the remainder is $f(\frac{b}{a})$
- **Formula**: Remainder $= f(\frac{b}{a})$ when dividing by $(ax-b)$
- **Variables**:
  - $f(x)$ = polynomial function
  - $a$ = coefficient of x in divisor
  - $b$ = constant term in divisor
  - Solve $ax-b=0$ to get $x = \frac{b}{a}$
- **When to Use**: Finding remainder when divisor has coefficient other than 1 on x
- **Example from Workbook**: For divisor $2x-3$, set $2x-3=0$, so $x = \frac{3}{2}$ (Page 7)

### Factor Theorem
- **Statement**: For any x-intercept (root) $x=a$, there is a corresponding factor $(x-a)$
- **Formula**: If $f(a) = 0$, then $(x-a)$ is a factor of $f(x)$
- **Variables**:
  - $f(x)$ = polynomial function
  - $a$ = root/zero of the polynomial
  - $(x-a)$ = corresponding linear factor
- **When to Use**:
  - Testing if a given expression is a factor
  - Finding unknown coefficients given factor information
  - Converting between roots and factors
- **Example from Workbook**: If $(x-a)$ is a factor of $-5x^4 + 3x^3 + 7ax^2$, then substituting $x=a$ must give 0 (Page 9)

### Null Factor Law
- **Statement**: If a product of factors equals zero, at least one factor must equal zero
- **Formula**: If $a \times b \times c = 0$, then $a=0$ or $b=0$ or $c=0$
- **Variables**:
  - $a, b, c$ = factors (can be expressions like $(x-2)$, $(x+3)$, etc.)
- **When to Use**: Solving polynomial equations in factorised form to find all roots
- **Example from Workbook**: $(2x+\frac{3}{5})^4(x-6)^2(7-x) = 0$ leads to $2x+\frac{3}{5}=0$ or $x-6=0$ or $7-x=0$ (Page 10)

### Polynomial General Form
- **Statement**: Standard form of polynomial with descending powers
- **Formula**: $f(x) = a_nx^n + a_{n-1}x^{n-1} + a_{n-2}x^{n-2} + ... + a_1x + a_0$
- **Variables**:
  - $n$ = degree of polynomial (highest power)
  - $a_n, a_{n-1}, ..., a_1, a_0$ = coefficients
  - $a_n \neq 0$ (leading coefficient is non-zero)
- **When to Use**: Identifying and writing polynomials in standard form
- **Example from Workbook**: General definition on Page 3

### Cubic Point of Inflection Form
- **Statement**: Transformation form of cubic showing point of inflection
- **Formula**: $y = a(x-h)^3 + k$
- **Variables**:
  - $a$ = dilation factor (determines steepness and direction)
  - $(h,k)$ = point of inflection coordinates
  - If $a > 0$: graph rises to the right
  - If $a < 0$: graph falls to the right
- **When to Use**: Sketching cubic graphs, identifying key features
- **Example from Workbook**: $y = (x+1)^3 + 8$ has POI at $(-1, 8)$ (Page 13)

### Quartic Turning Point Form
- **Statement**: Transformation form of quartic showing vertex/turning point
- **Formula**: $y = a(x-h)^4 + k$
- **Variables**:
  - $a$ = dilation factor (determines width and direction)
  - $(h,k)$ = turning point (vertex) coordinates
  - If $a > 0$: parabola opens upward (minimum at vertex)
  - If $a < 0$: parabola opens downward (maximum at vertex)
- **When to Use**: Sketching quartic graphs, finding vertex and intercepts
- **Example from Workbook**: $y = (x-2)^4 - 1$ has vertex at $(2, -1)$ (Page 17)

### X-intercept from Factor
- **Statement**: Each distinct linear factor gives an x-intercept
- **Formula**: Factor $(x-a)$ corresponds to x-intercept at $(a, 0)$
- **Variables**:
  - $a$ = x-coordinate of intercept
- **When to Use**: Finding x-intercepts from factorised polynomials
- **Example from Workbook**: $f(x) = (x-a)(x-b)(x-c)$ has x-intercepts at $(a,0), (b,0), (c,0)$ (Page 19)

### Repeated Factor (Turning Point)
- **Statement**: Repeated linear factors correspond to turning point on x-axis
- **Formula**: Factor $(x-a)^2$ (or higher even power) gives turning point AND x-intercept at $(a, 0)$
- **Variables**:
  - $a$ = x-coordinate where graph touches x-axis
- **When to Use**: Identifying where cubic graph touches (but doesn't cross) x-axis
- **Example from Workbook**: $f(x) = (x-a)^2(x-b)$ has turning point at $(a,0)$ and crosses at $(b,0)$ (Page 19)

---

## 3. Worked Examples Analysis

### Example 1: Long Division of Polynomials
- **Location**: Page 4, Question 2 Walkthrough
- **Topic**: Long Division
- **Problem Type**: Divide polynomial by polynomial to find quotient and remainder
- **Given Information**: $p(x) = 2x^4 - 3x^2 + 8x - 1$, $g(x) = x^2 + 1$
- **Required**: Find quotient $q(x)$ and remainder $r(x)$
- **Solution Method**:
  1. Set up long division with dividend inside, divisor outside
  2. Divide leading term of dividend by leading term of divisor: $2x^4 \div x^2 = 2x^2$
  3. Multiply divisor by this term: $2x^2(x^2+1) = 2x^4 + 2x^2$
  4. Subtract from dividend: $(2x^4 - 3x^2) - (2x^4 + 2x^2) = -5x^2$
  5. Bring down next terms: $-5x^2 + 8x - 1$
  6. Repeat: $-5x^2 \div x^2 = -5$, multiply and subtract
  7. Continue until remainder degree is less than divisor degree
- **Key Formula Used**: Division algorithm
- **Final Answer**: Quotient $= 2x^2 - 5$, Remainder $= 8x + 4$
- **Answer Format**: Polynomial expressions
- **Difficulty Level**: Basic/Intermediate - demonstrates standard algorithm

### Example 2: Short Division (Synthetic Division)
- **Location**: Page 6, Question 4 Walkthrough
- **Topic**: Short Division/Synthetic Division
- **Problem Type**: Simplify polynomial division using abbreviated method
- **Given Information**: $(2x^3 - 3x^2 - 8x + 12) \div (x-3)$
- **Required**: Find quotient (simplified form)
- **Solution Method**:
  1. Identify divisor root: $(x-3)$ means $x=3$
  2. Write coefficients of dividend: 2, -3, -8, 12
  3. Use box/synthetic division layout
  4. Bring down leading coefficient (2)
  5. Multiply by root (3), add to next coefficient: $2 \times 3 = 6$, then $-3 + 6 = 3$
  6. Continue pattern: multiply, add, repeat
  7. Final value is remainder (should be 0 for exact division)
- **Key Formula Used**: Synthetic division algorithm
- **Final Answer**: $2x^2 + 3x + 1$ with remainder 15
- **Answer Format**: Polynomial expression
- **Difficulty Level**: Intermediate - requires understanding of synthetic division layout

### Example 3: Remainder Theorem with Linear Divisor
- **Location**: Page 7, Question 6 Walkthrough
- **Topic**: Remainder Theorem
- **Problem Type**: Find unknown coefficient given equal remainders
- **Given Information**: $p(x) = 3x^3 - 2x^2 + ax + 4$ and $g(x) = x^3 + 5x^2 - 7x + 1$ both divided by $x-2$ give same remainder
- **Required**: Find value of $a$
- **Solution Method**:
  1. Apply remainder theorem: remainder when dividing by $(x-2)$ is $f(2)$
  2. Calculate $p(2) = 3(2)^3 - 2(2)^2 + a(2) + 4 = 24 - 8 + 2a + 4 = 20 + 2a$
  3. Calculate $g(2) = (2)^3 + 5(2)^2 - 7(2) + 1 = 8 + 20 - 14 + 1 = 15$
  4. Set equal: $20 + 2a = 15$
  5. Solve for $a$: $2a = -5$, so $a = -2.5$
- **Key Formula Used**: Remainder Theorem: $f(a)$ gives remainder
- **Final Answer**: $a = -2.5$
- **Answer Format**: Decimal value
- **Difficulty Level**: Intermediate - requires setting up equation and solving

### Example 4: Remainder Theorem with Non-unit Coefficient
- **Location**: Page 7, Question 7
- **Topic**: Remainder Theorem (Form 2)
- **Problem Type**: Find remainder when divisor has coefficient $\neq 1$
- **Given Information**: $f(x) = -3x^3 + 4x^2 - 5x + 12$ divided by $2x-3$
- **Required**: Find remainder
- **Solution Method**:
  1. Identify divisor form: $ax - b = 2x - 3$
  2. Solve for x-value: $2x - 3 = 0$, so $x = \frac{3}{2}$
  3. Substitute into polynomial: $f(\frac{3}{2}) = -3(\frac{3}{2})^3 + 4(\frac{3}{2})^2 - 5(\frac{3}{2}) + 12$
  4. Calculate: $= -3(\frac{27}{8}) + 4(\frac{9}{4}) - \frac{15}{2} + 12$
  5. Simplify to get numerical answer
- **Key Formula Used**: Remainder Theorem: $f(\frac{b}{a})$ for divisor $(ax-b)$
- **Final Answer**: $\frac{27}{2}$ or $13.5$
- **Answer Format**: Fraction or decimal
- **Difficulty Level**: Intermediate - requires careful fraction arithmetic

### Example 5: Factor Theorem - Testing if Expression is Factor
- **Location**: Page 9, Question 10 Walkthrough
- **Topic**: Factor Theorem
- **Problem Type**: Given factor condition, find unknown coefficient
- **Given Information**: $(x-a)$ is a factor of $-5x^4 + 3x^3 + 7ax^2$ where $a \neq 0$
- **Required**: Find value of $a$
- **Solution Method**:
  1. Apply factor theorem: if $(x-a)$ is factor, then $f(a) = 0$
  2. Substitute $x = a$: $-5(a)^4 + 3(a)^3 + 7a(a)^2 = 0$
  3. Simplify: $-5a^4 + 3a^3 + 7a^3 = 0$
  4. Combine like terms: $-5a^4 + 10a^3 = 0$
  5. Factor: $-5a^3(a - 2) = 0$
  6. Since $a \neq 0$, we have $a - 2 = 0$, so $a = 2$
- **Key Formula Used**: Factor Theorem: $f(a) = 0$ if $(x-a)$ is factor
- **Final Answer**: $a = 2$
- **Answer Format**: Integer value
- **Difficulty Level**: Intermediate/Advanced - requires algebraic manipulation

### Example 6: Determining if Expression is NOT a Factor
- **Location**: Page 9, Question 11
- **Topic**: Factor Theorem (negative result)
- **Problem Type**: Test if given expression is a factor
- **Given Information**: $P(x) = x^3 + 4x^2 - 5x - 6$, test if $(x-2)$ is a factor
- **Required**: Determine yes or no
- **Solution Method**:
  1. Apply factor theorem: calculate $P(2)$
  2. Substitute: $P(2) = (2)^3 + 4(2)^2 - 5(2) - 6$
  3. Calculate: $= 8 + 16 - 10 - 6 = 8$
  4. Since $P(2) \neq 0$, $(x-2)$ is NOT a factor
- **Key Formula Used**: Factor Theorem (contrapositive)
- **Final Answer**: NO, not a factor
- **Answer Format**: Yes/No with justification
- **Difficulty Level**: Basic - direct application of theorem

### Example 7: Sketching Cubic in POI Form
- **Location**: Page 13, Question 16 Walkthrough
- **Topic**: Sketching Cubic Graphs in POI Form
- **Problem Type**: Sketch graph with labeled features
- **Given Information**: $y = (x+1)^3 + 8$
- **Required**: Sketch with intercepts and turning point labeled
- **Solution Method**:
  1. Identify POI: $(h,k) = (-1, 8)$ from form $(x-h)^3 + k$
  2. Find y-intercept: set $x=0$, $y = (0+1)^3 + 8 = 1 + 8 = 9$, point $(0,9)$
  3. Find x-intercept: set $y=0$, $0 = (x+1)^3 + 8$
  4. Solve: $(x+1)^3 = -8$, take cube root: $x+1 = -2$, so $x = -3$
  5. X-intercept at $(-3, 0)$
  6. Determine shape: coefficient is positive (1), so curve rises to right
  7. Sketch: mark POI at $(-1,8)$, passes through $(-3,0)$ and $(0,9)$
- **Key Formula Used**: POI form $y = a(x-h)^3 + k$
- **Final Answer**: Graph with POI at $(-1,8)$, x-intercept $(-3,0)$, y-intercept $(0,9)$
- **Answer Format**: Labeled graph sketch
- **Difficulty Level**: Intermediate - requires finding multiple features

### Example 8: Sketching Quartic in Turning Point Form
- **Location**: Page 17, Question 19 Walkthrough
- **Topic**: Sketching Quartic Graphs in Turning Point Form
- **Problem Type**: Sketch parabola-like quartic with vertex
- **Given Information**: $y = (x-2)^4 - 1$
- **Required**: Label vertex and intercepts
- **Solution Method**:
  1. Identify vertex (turning point): $(h,k) = (2,-1)$ from form $(x-h)^4 + k$
  2. Determine direction: coefficient is positive (1), opens upward
  3. Find y-intercept: set $x=0$, $y = (0-2)^4 - 1 = 16 - 1 = 15$, point $(0,15)$
  4. Find x-intercepts: set $y=0$, $0 = (x-2)^4 - 1$
  5. Solve: $(x-2)^4 = 1$, take fourth root: $x-2 = \pm 1$
  6. Solutions: $x = 2+1 = 3$ and $x = 2-1 = 1$
  7. X-intercepts at $(1,0)$ and $(3,0)$
  8. Sketch U-shape with vertex at bottom
- **Key Formula Used**: Turning point form $y = a(x-h)^4 + k$
- **Final Answer**: U-shaped graph, vertex $(2,-1)$, x-intercepts $(1,0)$ and $(3,0)$, y-intercept $(0,15)$
- **Answer Format**: Labeled graph sketch
- **Difficulty Level**: Intermediate - solving fourth power equation

### Example 9: Sketching Negative Quartic
- **Location**: Page 18, Question 20
- **Topic**: Sketching Quartic with Negative Coefficient
- **Problem Type**: Inverted parabola shape
- **Given Information**: $y = -\frac{1}{4}(x+2)^4 - 1$
- **Required**: Sketch with labeled vertex and intercepts
- **Solution Method**:
  1. Identify vertex: $(h,k) = (-2,-1)$
  2. Determine direction: coefficient is negative ($-\frac{1}{4}$), opens downward
  3. Find y-intercept: set $x=0$, $y = -\frac{1}{4}(2)^4 - 1 = -\frac{16}{4} - 1 = -4 - 1 = -5$
  4. Find x-intercepts: set $y=0$, $0 = -\frac{1}{4}(x+2)^4 - 1$
  5. Solve: $(x+2)^4 = -4$ - no real solution (negative under even root)
  6. No x-intercepts
  7. Sketch inverted U-shape (sad face) with maximum at vertex
- **Key Formula Used**: Turning point form with negative coefficient
- **Final Answer**: Inverted parabola, maximum at $(-2,-1)$, y-intercept $(0,-5)$, no x-intercepts
- **Answer Format**: Labeled graph sketch
- **Difficulty Level**: Intermediate - recognizing no real x-intercepts

### Example 10: Sketching Factorised Cubic (Positive)
- **Location**: Page 21, Question 21 Walkthrough
- **Topic**: Graphs of Factorised Cubics
- **Problem Type**: Identify all x-intercepts and sketch
- **Given Information**: $y = (x-2)(3x-1)(4x+1)$
- **Required**: Sketch and label intercepts
- **Solution Method**:
  1. Find x-intercepts from factors: set each factor to zero
  2. $(x-2) = 0$ gives $x = 2$
  3. $(3x-1) = 0$ gives $x = \frac{1}{3}$
  4. $(4x+1) = 0$ gives $x = -\frac{1}{4}$
  5. X-intercepts at $(-\frac{1}{4}, 0)$, $(\frac{1}{3}, 0)$, $(2, 0)$
  6. Find y-intercept: set $x=0$, $y = (-2)(-1)(1) = 2$
  7. Determine shape: expand to check leading coefficient (positive), so cubic rises to right
  8. Sketch: crosses x-axis at three points, passes through $(0,2)$
- **Key Formula Used**: Factor to x-intercept relationship
- **Final Answer**: Cubic crossing at $x = -0.25, \frac{1}{3}, 2$; y-intercept $(0,2)$
- **Answer Format**: Labeled graph with 3 x-intercepts
- **Difficulty Level**: Intermediate - solving linear factors

### Example 11: Sketching Factorised Cubic with Repeated Root
- **Location**: Page 22, Question 22
- **Topic**: Graphs of Factorised Cubics (Turning Point on Axis)
- **Problem Type**: Identify turning point and crossing point
- **Given Information**: $y = (x-2)(x+5)^2$
- **Required**: Sketch and label intercepts
- **Solution Method**:
  1. Identify x-intercepts: $(x-2) = 0$ gives $x=2$, $(x+5) = 0$ gives $x=-5$
  2. Note: $(x+5)^2$ is repeated (even power), so turning point at $x=-5$
  3. Graph touches x-axis at $(-5,0)$ but doesn't cross
  4. Graph crosses x-axis at $(2,0)$
  5. Find y-intercept: $y = (-2)(5)^2 = -2 \times 25 = -50$
  6. Determine shape: leading coefficient positive, cubic rises to right
  7. Sketch: turning point at $(-5,0)$, crosses at $(2,0)$, passes through $(0,-50)$
- **Key Formula Used**: Repeated factor indicates turning point
- **Final Answer**: Turning point $(-5,0)$, crosses at $(2,0)$, y-intercept $(0,-50)$
- **Answer Format**: Labeled graph showing touching vs crossing
- **Difficulty Level**: Advanced - distinguishing repeated vs distinct factors

### Example 12: Application - Polynomial Height Functions
- **Location**: Page 24, Question 24
- **Topic**: Application of Polynomials
- **Problem Type**: Real-world modeling with constraints
- **Given Information**:
  - Curve A: $y = -5x^2 + 45x + 50$, $x \geq 0$ (height in metres)
  - Curve B: $y = x^3 - 6x^2 + 11x - 6$, $x \geq 0$ (height in metres)
- **Required**:
  a) Where does Curve A meet ground?
  b) Where does Curve B meet ground?
  c) At what x is Curve A tallest?
- **Solution Method**:
  - Part a: Set $y = 0$: $-5x^2 + 45x + 50 = 0$
    - Factor: $-5(x^2 - 9x - 10) = 0$
    - Further: $-5(x-10)(x+1) = 0$
    - Solutions: $x = 10$ or $x = -1$
    - Since $x \geq 0$, answer is $x = 10$ metres
  - Part b: Set $y = 0$: $x^3 - 6x^2 + 11x - 6 = 0$
    - Factor by grouping or trial: $x = 1, 2, 3$
    - All valid since all positive
  - Part c: Find maximum of quadratic (complete square or vertex formula)
    - Vertex at $x = -\frac{b}{2a} = -\frac{45}{2(-5)} = \frac{45}{10} = 4.5$
    - Maximum height at $x = 4.5$ metres
- **Key Formula Used**: Quadratic factoring, vertex formula
- **Final Answer**: a) 10m, b) 1m, 2m, 3m, c) 4.5m with height 50m
- **Answer Format**: Distance in metres with context
- **Difficulty Level**: Advanced - multi-part real-world problem

---

## 4. Difficulty Benchmarks

### Basic Level
- **Characteristics**:
  - Direct application of single formula or theorem
  - Simple polynomial expressions (degree 2-3, small integer coefficients)
  - One-step or two-step problems
  - Clear indication of which method to use
- **Typical Number Ranges**:
  - Integer coefficients from -10 to 10
  - Simple roots like 1, 2, 3, -1, -2
  - Y-values up to 50
- **Steps Required**: 1-2 steps
- **Formulas Used**: Single formula, direct substitution
- **Reference Examples**:
  - Q1: Expand and simplify polynomial expression (Page 3)
  - Q11: Test if expression is a factor using factor theorem (Page 9)
  - Q16 Walkthrough: Sketch cubic in POI form with given equation (Page 13)

### Intermediate Level
- **Characteristics**:
  - Combination of multiple concepts
  - Requires choosing appropriate method
  - Polynomial degree 3-4
  - May involve fractions or decimals in answers
  - Multi-step algebraic manipulation
  - Graph sketching with multiple features
- **Typical Number Ranges**:
  - Integer coefficients -20 to 20
  - Fractional roots like $\frac{1}{3}$, $\frac{-5}{2}$
  - Decimal answers to 1-2 decimal places
  - Y-values up to 150
- **Steps Required**: 3-5 steps
- **Formulas Used**: May combine multiple formulas or theorems
- **Reference Examples**:
  - Q3: Long division with cubic dividend (Page 5)
  - Q6 Walkthrough: Find unknown using remainder theorem (Page 7)
  - Q10 Walkthrough: Find value using factor theorem (Page 9)
  - Q13: Find roots of factorised polynomial with fractions (Page 10)
  - Q19 Walkthrough: Sketch quartic with turning point (Page 17)
  - Q21 Walkthrough: Sketch factorised cubic (Page 21)

### Advanced Level
- **Characteristics**:
  - Multi-part problems requiring several concepts
  - Real-world applications with constraints
  - Higher degree polynomials (degree 4+)
  - Requires strategic thinking and problem-solving
  - May involve constructing polynomials from conditions
  - Extension questions with non-standard approaches
  - Negative coefficients or inverted graphs
- **Typical Number Ranges**:
  - Large powers (e.g., $x^{101}$)
  - Complex expressions with multiple unknowns
  - Surds or irrational answers (though not common in this workbook)
  - Y-values exceeding 100
- **Steps Required**: 5+ steps, multi-part questions
- **Formulas Used**: Multiple formulas, strategic selection, derivation needed
- **Reference Examples**:
  - Q8 Extension: Remainder when $x^{101}-1$ divided by $(x-1)$ (Page 8)
  - Q14 Extension: Construct polynomial from given roots and point (Page 11)
  - Q15 Extension: Multi-condition problem with remainder and y-intercept (Page 11)
  - Q18 Extension: Determine coefficients from graph (Page 15)
  - Q23 Extension: Rectangle inscribed in parabola optimization (Page 23)
  - Q24: Application with two polynomial curves, multiple parts (Page 24-25)

---

## 5. Solution Strategies Taught

### Strategy 1: Long Division Algorithm
- **When Used**: Dividing polynomial by polynomial of degree $\geq 2$
- **Steps**:
  1. Set up division: dividend inside, divisor outside in traditional layout
  2. Divide leading term of dividend by leading term of divisor
  3. Write result above division bar
  4. Multiply entire divisor by this result
  5. Subtract from dividend (watch signs carefully)
  6. Bring down next term(s)
  7. Repeat steps 2-6 until remainder degree < divisor degree
  8. Express answer using division algorithm formula
- **Example Problem Types**: Any polynomial division, especially when divisor is degree 2+
- **Common Mistakes to Avoid**:
  - Sign errors when subtracting
  - Forgetting to include zero coefficients for missing powers
  - Stopping too early

### Strategy 2: Synthetic Division (Short Division)
- **When Used**: Dividing polynomial by linear factor $(x-c)$
- **Steps**:
  1. Identify the root $c$ from divisor $(x-c)$
  2. Write down all coefficients of dividend (include 0 for missing terms)
  3. Set up box diagram or synthetic division layout
  4. Bring down first coefficient unchanged
  5. Multiply by root $c$, write result below next coefficient
  6. Add vertically, write sum below
  7. Repeat multiply-add pattern across all coefficients
  8. Final value is remainder, others form quotient polynomial
- **Example Problem Types**: Division by $(x-3)$, $(x+5)$, etc.
- **Common Mistakes to Avoid**:
  - Using wrong value for $c$ (remember $x-3$ means $c=3$, not $c=-3$)
  - Misaligning columns in box method

### Strategy 3: Remainder Theorem Substitution
- **When Used**: Finding remainder without full division; solving for unknowns with remainder conditions
- **Steps**:
  1. Identify divisor form: $(x-a)$ or $(ax-b)$
  2. Solve for x-value: $x=a$ or $x=\frac{b}{a}$
  3. Substitute this value into polynomial $f(x)$
  4. Simplify arithmetic carefully (powers, fractions)
  5. Result is the remainder
  6. If finding unknown, set remainder equal to given value and solve
- **Example Problem Types**: "Find remainder when...", "Two polynomials have same remainder..."
- **Common Mistakes to Avoid**:
  - Incorrect fraction arithmetic
  - Using wrong x-value for divisor $(ax-b)$

### Strategy 4: Factor Theorem Testing
- **When Used**: Determining if linear expression is a factor; finding unknowns given factor conditions
- **Steps**:
  1. Identify potential factor $(x-a)$
  2. Substitute $x=a$ into polynomial $f(x)$
  3. Simplify completely
  4. If result equals zero: IS a factor
  5. If result is non-zero: NOT a factor
  6. For unknown coefficients: set up equation $f(a) = 0$ and solve
- **Example Problem Types**: "Is $(x-2)$ a factor of...", "If $(x-a)$ is a factor, find..."
- **Common Mistakes to Avoid**:
  - Arithmetic errors in substitution
  - Confusing "is a factor" (equals 0) with "has remainder" (non-zero)

### Strategy 5: Null Factor Law for Roots
- **When Used**: Finding all roots/solutions of polynomial equation in factorised form
- **Steps**:
  1. Ensure equation is set equal to zero
  2. Write in fully factorised form if not already
  3. Apply null factor law: set each distinct factor equal to zero
  4. Solve each linear equation separately
  5. List all solutions (roots)
  6. Note multiplicity if factors are repeated
- **Example Problem Types**: "Find roots of $(x-2)(x+3)(x-7)=0$"
- **Common Mistakes to Avoid**:
  - Forgetting to list all roots
  - Not solving fractional factors correctly

### Strategy 6: Sketching Transformed Polynomial Graphs
- **When Used**: Sketching cubics/quartics in transformation form
- **Steps**:
  1. Identify form: $(x-h)^n + k$ where $n$ is degree
  2. Locate key point: POI for odd $n$, turning point for even $n$ at $(h,k)$
  3. Determine direction/shape based on coefficient $a$ and degree $n$
  4. Find y-intercept: substitute $x=0$
  5. Find x-intercepts: set $y=0$ and solve (may have 0, 1, or 2 solutions)
  6. Draw smooth curve through all points with correct shape
  7. Label all key features clearly
- **Example Problem Types**: "Sketch $y = (x+1)^3 + 8$", "Sketch $y = -(x-2)^4 + 1$"
- **Common Mistakes to Avoid**:
  - Confusing turning point vs point of inflection
  - Not checking if x-intercepts exist (negative under even root)
  - Incorrect shape for negative coefficients

### Strategy 7: Sketching Factorised Cubics
- **When Used**: Sketching cubic graphs given in factorised form
- **Steps**:
  1. Identify all linear factors
  2. Set each factor to zero to find x-intercepts
  3. Check for repeated factors (even power = touches axis, odd power = crosses)
  4. Find y-intercept by substituting $x=0$
  5. Determine end behavior: expand leading term or check sign pattern
  6. Sketch curve crossing/touching x-axis at identified points
  7. Ensure curve has correct cubic shape (two turning points max)
- **Example Problem Types**: "Sketch $y = (x-1)(x+2)(x-3)$", "Sketch $y = (x+1)^2(x-2)$"
- **Common Mistakes to Avoid**:
  - Missing repeated roots
  - Incorrect cubic shape (too many wiggles)
  - Wrong end behavior

### Strategy 8: Application Problem Framework
- **When Used**: Real-world polynomial modeling problems
- **Steps**:
  1. Read problem carefully, identify what is given and what is required
  2. Note any domain restrictions (e.g., $x \geq 0$ for physical quantities)
  3. For "meets ground" problems: set $y=0$ and solve
  4. For "maximum/minimum" problems: find turning point
  5. For "intersection" problems: set two functions equal
  6. Check solutions against domain restrictions
  7. Include units in final answer with context
- **Example Problem Types**: Height vs distance, structure problems, optimization
- **Common Mistakes to Avoid**:
  - Including negative solutions when physically impossible
  - Forgetting units
  - Not checking domain restrictions

---

## 6. Common Patterns

### Number Patterns Used

#### Integers
- **Typical Ranges**: -10 to 20 for coefficients
- **Roots/Intercepts**: Often small integers like -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 10
- **Powers**: Degree 2 (quadratic), 3 (cubic), 4 (quartic) most common
- **Extension**: Very large powers like 101 for challenge questions

#### Decimals
- **Precision**: Usually 1 decimal place (e.g., 2.5, 4.5) or 2 decimal places (e.g., 13.5)
- **Context**: Often appear in final answers after division or vertex calculations
- **Negative Decimals**: Yes, especially for y-intercepts or turning points

#### Fractions
- **Common Fractions**: $\frac{1}{2}$, $\frac{1}{3}$, $\frac{1}{4}$, $\frac{2}{3}$, $\frac{3}{5}$, $\frac{-5}{2}$
- **Context**: Roots from factors like $(2x+3)$, $(3x-1)$, $(4x+1)$
- **Working**: Students expected to show fraction arithmetic in steps

#### Special Values
- **Not Prominent**: This workbook does not use $\pi$, $\sqrt{2}$, $\sqrt{3}$, or surds
- **Focus**: Rational numbers and simple radicals only (e.g., $\sqrt{4} = 2$)

#### Measurements
- **Context**: Application problems use metres for distance/height
- **Typical Values**: 0 to 50 metres for heights, 0 to 10 metres for horizontal distances
- **Realistic Scale**: Values chosen to be practical for real structures

### Question Formats

#### Format 1: "Expand and simplify"
- **Structure**: Given polynomial expression in factorised or mixed form
- **Task**: Multiply out and combine like terms
- **Example**: "Expand and simplify $(5y-2)(2y^2+y-3)$"
- **Working Expected**: Show distributive property steps

#### Format 2: "Apply [method] to find..."
- **Structure**: Direct instruction to use specific technique
- **Task**: Perform algorithm (long division, short division, remainder theorem)
- **Example**: "Apply long division to find quotient and remainder..."
- **Working Expected**: Full algorithm shown with clear layout

#### Format 3: "Find the value of [unknown]"
- **Structure**: Polynomial with unknown coefficient, given condition
- **Task**: Set up equation and solve for unknown
- **Example**: "If remainder is 0, find the value of $a$"
- **Working Expected**: Substitution, equation setup, algebraic solution

#### Format 4: "Determine if [expression] is a factor"
- **Structure**: Test factor theorem condition
- **Task**: Substitute and check if result is zero
- **Example**: "Determine if $x-2$ is a factor of $P(x) = x^3 + 4x^2 - 5x - 6$"
- **Working Expected**: Substitution calculation, yes/no conclusion

#### Format 5: "Find the roots/x-intercepts"
- **Structure**: Factorised polynomial set equal to zero
- **Task**: Apply null factor law
- **Example**: "Find the roots of $(2x+\frac{3}{5})^4(x-6)^2(7-x)=0$"
- **Working Expected**: Each factor set to zero, all solutions listed

#### Format 6: "Sketch the graph of [function]"
- **Structure**: Polynomial in transformation or factorised form
- **Task**: Draw accurate sketch with labeled key features
- **Example**: "Sketch the graph of $y = (x+1)^3 + 8$ on the axes below. Label the intercepts and turning point."
- **Working Expected**: Calculations for intercepts, labeled diagram

#### Format 7: "Where does Curve A meet [condition]?"
- **Structure**: Real-world application with polynomial model
- **Task**: Set up appropriate equation and solve
- **Example**: "Where does Curve A meet the ground?" (set y=0)
- **Working Expected**: Equation setup, solution, answer with units

### Answer Expectations

#### Exact vs Approximate
- **General Rule**: Give exact answers unless stated otherwise
- **Exact**: Fractions like $\frac{3}{2}$, $\frac{-5}{2}$
- **Approximate**: "In decimal form" means convert to decimal (e.g., 1.5 instead of $\frac{3}{2}$)
- **Context**: Application problems often ask for decimal form for practicality

#### Units
- **Always Required**: Yes, for application/word problems involving measurements
- **Standard Units**: Metres (m) for distance and height
- **Placement**: After numerical answer (e.g., "10 metres" or "10m")

#### Significant Figures
- **Not Explicitly Stated**: Workbook doesn't specify sig fig requirements
- **Standard Precision**:
  - Exact fractions when possible
  - 1-2 decimal places for decimals
  - Don't over-round intermediate steps
- **Context**: Match precision to problem context

#### Working Required
- **Always**: Yes, working is essential for all problems
- **How Much Detail**:
  - Show formula/theorem being applied
  - Show substitution step
  - Show arithmetic/algebraic manipulation
  - Box or highlight final answer
- **Layout**: Clear, organized, step-by-step progression
- **Walkthroughs**: Model problems show expected level of detail

#### Graph Requirements
- **Axes**: Must be drawn and labeled (x and y)
- **Key Features**: All intercepts, turning points, POI labeled with coordinates
- **Accuracy**: Shape must be correct (cubic/quartic characteristics)
- **Neatness**: Smooth curves, clear labels, readable coordinates

---

## 7. Visual Diagram Patterns

### 7.1 Diagram Configuration → Concept Mapping

| Concept/Theorem | Diagram Configuration | Key Visual Elements | How to Recognize |
|-----------------|----------------------|---------------------|------------------|
| **Cubic in POI Form** | S-shaped curve with inflection point | Single point where concavity changes; curve continuous through point | Smooth S-shape, labeled point $(h,k)$ where curve transitions from concave down to concave up (or vice versa) |
| **Quartic in Turning Point Form (Positive)** | U-shaped parabola with vertex at bottom | Vertex (turning point) at minimum; symmetric shape | Upward-opening U-shape, vertex labeled as lowest point $(h,k)$ |
| **Quartic in Turning Point Form (Negative)** | Inverted U-shape with vertex at top | Vertex (turning point) at maximum; symmetric shape | Downward-opening ∩-shape, vertex labeled as highest point $(h,k)$ |
| **Factorised Cubic (All Distinct Roots)** | Cubic crossing x-axis three times | Three points where curve crosses horizontal axis | Three distinct $(x,0)$ points marked; typical cubic wiggle with two turning points |
| **Factorised Cubic (One Repeated Root)** | Cubic touching x-axis once, crossing once | One point where curve touches but doesn't cross (turning point on axis); one crossing point | Two x-intercepts marked: one shows curve bouncing off axis, one shows crossing |
| **Polynomial Graph Features** | Coordinate plane with labeled axes and grid | X-axis (horizontal), Y-axis (vertical), origin marked as 0 | Standard Cartesian plane, typically showing range -10 to +10 on each axis |

### 7.2 Visual Elements and Their Meaning

| Visual Element | What It Indicates | Testing Aspect |
|----------------|-------------------|----------------|
| **Labeled point $(h,k)$** | Key feature location (POI or turning point) | Student must identify type based on context and calculate coordinates |
| **X-intercept marking** | Where graph crosses x-axis (root/solution) | Student must find by solving equation when $y=0$ |
| **Y-intercept marking** | Where graph crosses y-axis | Student must find by substituting $x=0$ |
| **Arrow directions on axes** | Graph extends infinitely in those directions | Indicates domain/range continuation |
| **Grid lines** | Scale reference for plotting points | Helps determine accuracy of sketch |
| **Smooth curve vs sharp point** | Differentiable vs non-differentiable | All polynomial graphs must be smooth (no sharp corners) |
| **Concavity change** | Point of inflection for cubics | Visual cue for where curve changes from concave to convex |
| **Symmetry** | Even-degree polynomials in vertex form | Quartics should show left-right symmetry around turning point |
| **End behavior arrows** | Direction of graph as $x \to \pm\infty$ | Positive cubic: down-left, up-right; Negative cubic: up-left, down-right |

### 7.3 Standard Diagram Patterns by Topic

#### Cubic Graphs (POI Form):
```
Pattern: S-shaped curve with labeled inflection point

Positive Coefficient (a > 0):
- Starts from bottom-left (third quadrant)
- Curves through point of inflection
- Ends in top-right (first quadrant)
- Point of inflection is where curve "flattens" momentarily

Negative Coefficient (a < 0):
- Starts from top-left (second quadrant)
- Curves through point of inflection
- Ends in bottom-right (fourth quadrant)
- Inverted S-shape

Key Features to Mark:
├── Point of inflection $(h,k)$
├── X-intercept(s) - solve $(x-h)^3 + k = 0$
└── Y-intercept - substitute $x=0$
```

#### Quartic Graphs (Turning Point Form):
```
Pattern: Parabola-like U or ∩ shape with vertex

Positive Coefficient (a > 0):
- U-shaped (concave up)
- Vertex is minimum point
- Opens upward
- Symmetric about vertical line through vertex
- "Smiley face" ☺

Negative Coefficient (a < 0):
- ∩-shaped (concave down)
- Vertex is maximum point
- Opens downward
- Symmetric about vertical line through vertex
- "Sad face" ☹

Key Features to Mark:
├── Vertex/Turning point $(h,k)$
├── X-intercept(s) - solve $(x-h)^4 + k = 0$ (may be 0, 1, or 2)
└── Y-intercept - substitute $x=0$

Note: Flatter than quadratic parabolas due to higher degree
```

#### Factorised Cubic Graphs:
```
Pattern: Cubic with marked x-intercepts

All Distinct Factors: $(x-a)(x-b)(x-c)$
- Three separate x-intercepts
- Graph crosses x-axis at all three points
- Typical cubic shape with two turning points between roots
- No turning points on the x-axis

├── X-intercept at $(a, 0)$ - crosses
├── X-intercept at $(b, 0)$ - crosses
└── X-intercept at $(c, 0)$ - crosses

One Repeated Factor: $(x-a)^2(x-b)$
- Two x-intercepts visually
- Graph TOUCHES (but doesn't cross) at repeated root
- Graph CROSSES at distinct root
- One turning point is ON the x-axis

├── X-intercept at $(a, 0)$ - TOUCHES (turning point)
└── X-intercept at $(b, 0)$ - CROSSES

End Behavior:
- Positive leading coefficient: ↙ to ↗ (down-left to up-right)
- Negative leading coefficient: ↖ to ↘ (up-left to down-right)
```

#### Application Context Diagrams:
```
Pattern: Real-world scenario with polynomial curves

Common Setups:
1. Height vs Horizontal Distance
   - X-axis: horizontal distance (metres)
   - Y-axis: height above ground (metres)
   - Ground level at y = 0
   - Curves show structure profiles

2. Inscribed Shapes in Parabolas
   - Parabola curve with rectangle drawn inside
   - Shaded region shows area of interest
   - Dimensions labeled with variables
   - Axis of symmetry marked

Key Visual Cues:
├── Domain restrictions shown (e.g., $x \geq 0$ only first quadrant)
├── Intersection points marked where curves meet
├── Maximum/minimum points highlighted
└── Measurement labels with units (metres)
```

### 7.4 Diagram Variations in Workbook

| Concept | Variation 1 | Variation 2 | Variation 3 |
|---------|-------------|-------------|-------------|
| **Cubic POI Form** | Positive coefficient, POI in first quadrant | Negative coefficient, POI in second quadrant | Positive coefficient, POI below x-axis |
| **Quartic Turning Point** | Positive coefficient, vertex below x-axis (two x-intercepts) | Negative coefficient, vertex above x-axis (two x-intercepts) | Positive coefficient, vertex above x-axis (no x-intercepts) |
| **Factorised Cubic** | Three distinct positive roots | One repeated root (touches axis) | Mix of positive and negative roots |
| **End Behavior** | Positive cubic (rises right) | Negative cubic (falls right) | Determined by sign of leading coefficient |
| **Intercept Configurations** | Both x and y intercepts in view | Y-intercept off scale (very high/low) | No x-intercepts (quartic entirely above/below axis) |

### 7.5 Critical Visual Recognition Skills

**Students must be able to:**

1. **Distinguish POI from Turning Point**:
   - POI: curve passes THROUGH continuously, changes concavity
   - Turning Point: curve reaches max/min and reverses direction

2. **Recognize Touching vs Crossing**:
   - Touching: even multiplicity, curve bounces off x-axis
   - Crossing: odd multiplicity, curve passes through x-axis

3. **Identify Graph Type from Shape**:
   - One inflection point, no local max/min → Cubic in POI form
   - U or ∩ shape with one turning point → Quartic in vertex form
   - Multiple x-intercepts with wiggles → Factorised cubic

4. **Determine Coefficient Sign from Direction**:
   - Cubic rises to right → positive leading coefficient
   - Cubic falls to right → negative leading coefficient
   - Quartic opens up → positive leading coefficient
   - Quartic opens down → negative leading coefficient

5. **Read Coordinates from Labeled Points**:
   - Key points always labeled with coordinates $(x, y)$
   - Must transfer these to equation form correctly
   - Distinguish between given points and points to be found

### 7.6 Sketch Quality Expectations

**For full marks, graphs must show:**
- ✓ Correctly drawn and labeled axes
- ✓ Appropriate scale (usually -10 to +10 or as shown)
- ✓ ALL key features labeled with exact coordinates:
  - Turning points / Points of inflection
  - X-intercepts (where graph crosses x-axis)
  - Y-intercepts (where graph crosses y-axis)
- ✓ Correct polynomial shape (smooth curve, no corners)
- ✓ Correct end behavior (arrows showing direction)
- ✓ Proper concavity throughout
- ✓ Neat, clear presentation

**Common sketch errors to avoid:**
- ✗ Sharp corners (polynomials are smooth)
- ✗ Wrong concavity
- ✗ Unlabeled key points
- ✗ Incorrect number of turning points
- ✗ Wrong end behavior
- ✗ Not showing graph passing through calculated points

---

## 8. Constraints for Question Variations

### MUST DO:

1. **Use Only Documented Formulas** (Section 2)
   - Division algorithm
   - Remainder theorem (both forms)
   - Factor theorem
   - Null factor law
   - POI form: $y = a(x-h)^3 + k$
   - Turning point form: $y = a(x-h)^4 + k$
   - Factorised form relationships

2. **Match Difficulty Levels** (Section 4)
   - Basic: 1-2 steps, direct application, small integers
   - Intermediate: 3-5 steps, combination of concepts, fractions/decimals possible
   - Advanced: 5+ steps, multi-part, real-world context, strategic thinking

3. **Follow Solution Strategies** (Section 5)
   - Long division for polynomial divisors
   - Synthetic division for linear divisors
   - Remainder theorem for finding remainders
   - Factor theorem for testing factors
   - Null factor law for finding roots
   - Transformation analysis for graph sketching
   - Application framework for word problems

4. **Use Number Patterns** (Section 6)
   - Coefficients: integers -20 to 20
   - Roots: small integers or simple fractions
   - Powers: mainly degree 2, 3, 4 (with extension to higher)
   - Answers: exact fractions preferred, decimals when specified
   - Application measurements: 0-50 metres typical

5. **Maintain Question Formats** (Section 6)
   - Clear instruction verbs: "Expand", "Apply", "Find", "Determine", "Sketch"
   - Specify working requirements explicitly
   - Include domain restrictions for applications
   - Ask for units in measurement problems
   - Provide axes for graph sketching

6. **Use Graph Visual Patterns** (Section 7)
   - Correct polynomial shapes (smooth, no corners)
   - Appropriate end behavior for coefficient signs
   - Distinguish POI (cubic) from turning point (quartic)
   - Show touching vs crossing for repeated roots
   - Label all key features with coordinates

### MUST NOT:

1. **Introduce New Formulas**
   - No trigonometric functions
   - No exponential functions
   - No logarithms
   - No calculus (derivatives/integrals)
   - No complex numbers
   - No matrix methods
   - Stay within polynomial algebra only

2. **Exceed Difficulty Benchmarks**
   - Don't require more than 6-7 steps
   - Avoid excessively large coefficients (> 50)
   - Don't use polynomials of degree > 4 (except extension)
   - Avoid irrational coefficients ($\sqrt{2}$, $\pi$, etc.)
   - Keep fraction arithmetic manageable

3. **Require Undocumented Methods**
   - No completing the square (not taught here)
   - No polynomial long division by quadratics (not shown)
   - No partial fractions
   - No advanced factoring techniques beyond trinomial
   - No graphing calculators required

4. **Use Inappropriate Number Ranges**
   - Avoid coefficients with absolute value > 50
   - Don't use messy fractions (e.g., $\frac{17}{23}$)
   - Avoid decimals with > 2 decimal places
   - Don't use irrational numbers as coefficients
   - Keep answer values reasonable (< 1000 typically)

5. **Create Ambiguous Questions**
   - Always specify what to find
   - Clarify if answer should be exact or decimal
   - State domain restrictions clearly
   - Indicate if working must be shown
   - Provide enough information to solve

6. **Break Visual Conventions**
   - Don't use non-polynomial graphs as examples
   - Maintain standard orientation (y up, x right)
   - Keep scale consistent within a problem
   - Don't omit key features from sketch requirements
   - Follow smooth curve requirement (no sharp points)

### SPECIFIC CONSTRAINTS BY TOPIC:

#### Polynomials (Basic Operations):
- Degree 2-4 typical, extension to higher powers
- Integer coefficients only for multiplication
- Simplified form required as final answer

#### Division (Long/Short):
- Divisor degree should be at least 1 less than dividend
- For long division: divisor typically degree 2
- For synthetic division: divisor must be linear $(x-c)$
- Remainder must be lower degree than divisor

#### Remainder Theorem:
- Divisor must be linear: $(x-a)$ or $(ax-b)$
- Calculations should not require calculator
- Fraction arithmetic must be manageable
- Extension: high powers like $x^{101}$ acceptable

#### Factor Theorem:
- Test factors must be linear
- Roots should be rational numbers
- Unknown coefficients: solve results in integer or simple fraction

#### Solving Equations:
- Must be in factorised form or factorable
- Roots should be rational (integers or simple fractions)
- Maximum 4 distinct roots typical
- Repeated roots acceptable (show multiplicity)

#### Graph Sketching:
- Provide blank axes or specify range
- Must specify which features to label
- Degree 3 (cubic) or 4 (quartic) standard
- All key points should have rational coordinates

#### Applications:
- Real-world context must be realistic
- Domain restrictions required (e.g., $x \geq 0$)
- Units must be specified (metres, etc.)
- Answers should make physical sense
- Multi-part questions acceptable (up to 5 parts)

### PEDAGOGICAL FIDELITY:

**This workbook teaches:**
- Polynomial algebra at Year 10 level (Australian Curriculum)
- Procedural fluency with division algorithms
- Connection between factors and roots
- Graph sketching from equations
- Real-world applications of polynomials

**This workbook does NOT teach:**
- Calculus concepts (derivatives for finding turning points)
- Advanced factoring (sum/difference of cubes)
- Polynomial theorems beyond factor/remainder
- Rational functions (with variables in denominator)
- Parametric or polar representations

**Question variations must:**
- Build on concepts in the order presented
- Reinforce connection between algebraic and graphical representations
- Develop fluency through varied practice
- Include mix of routine and non-routine problems
- Provide appropriate scaffolding for complex tasks

---

## Summary Statistics

- **Total Topics**: 10 major topics
- **Total Formulas/Theorems**: 10 documented formulas/theorems
- **Worked Examples Analyzed**: 12 detailed walkthroughs
- **Practice Problems**: 24 questions total (including extensions)
- **Difficulty Distribution**:
  - Basic: ~25% (6 questions)
  - Intermediate: ~55% (13 questions)
  - Advanced/Extension: ~20% (5 questions)
- **Page Range**: 25 pages total
- **Sections**: 2 major sections (A: Polynomials, B: Graphing)
- **Sub-sections**: 9 sub-sections covering specific skills

---

## Notes for Question Generator

1. **Progressive Difficulty**: Questions should start basic and gradually increase in complexity within each topic

2. **Balanced Coverage**: Ensure all 10 topics receive attention in question generation

3. **Working Space**: Original workbook provides ample space for student working - variations should assume same

4. **Extension Questions**: Marked clearly and reserved for advanced students (approximately 20% of questions)

5. **Real-World Context**: Application problems (Topic 10) should use realistic scenarios with appropriate units and constraints

6. **Graph Paper**: Sketching questions assume graph paper or pre-drawn axes are provided

7. **Calculator Use**: Most questions designed for non-calculator work; calculators acceptable for checking

8. **Walkthrough Style**: Some questions designated as "Walkthrough" with partial solutions shown to model method

9. **Answer Format**: Students expected to show all working, circle/box final answers, include units where applicable

10. **Visual Accuracy**: Graph sketches must show correct polynomial shape characteristics (smooth curves, appropriate end behavior, correct concavity)


---


# Curriculum Context: Year 10 Mathematics AOS 9 Revision [10.4]

## Metadata
- Source: Year 10 Mathematics AOS 9 Revision [10.4] Workbook.pdf
- Subject: Mathematics
- Year/Grade Level: Year 10
- Topic Area: Functions and Transformations, Gallery of Graphs
- Analysis Date: 2026-01-08

---

## 1. Topics Covered

### Topic 1: Functions and Correspondence
- **Definition**: Functions are relations that make one y-value at any given x-value
- **Key Concepts**:
  - Function definition and notation $y = f(x)$
  - Vertical line test
  - Distinguishing functions from relations
- **Subtopics**:
  - Identifying functions from tables of values
  - Identifying functions from graphs
  - Function vs relation determination
- **Pages**: 2-4

### Topic 2: Domain and Range
- **Definition**: Domain is all suitable x-values; Range is all suitable y-values
- **Key Concepts**:
  - Set notation and terminology
  - Set operations (intersection, union, difference)
  - Interval notation (parentheses vs square brackets)
  - Determining domain and range from functions
  - Determining domain and range from graphs
- **Subtopics**:
  - Sets and elements
  - Set operators (AND, OR, except)
  - Interval notation with inclusive/non-inclusive boundaries
  - Domain and range of quadratic functions
  - Domain and range of square root functions
  - Domain and range of hyperbolas
- **Pages**: 5-9

### Topic 3: Square Root Functions
- **Definition**: Functions of the form $y = a\sqrt{b(x-h)} + k$ where transformations are applied to the basic square root function
- **Key Concepts**:
  - General form and transformations
  - Effects of parameters a, b, h, k
  - Domain restrictions (inside square root must be ≥ 0)
  - Graphing square root functions
  - Key points and turning points
- **Subtopics**:
  - Positive vs negative dilation (a parameter)
  - Horizontal vs vertical translation (h and k parameters)
  - Reflection in x-axis (negative a)
  - Reflection in y-axis (negative b)
  - Finding domain and range from equation
  - Sketching and labeling key points
- **Pages**: 10-12

### Topic 4: Hyperbola
- **Definition**: Rational functions of the form $y = \frac{a}{x-h} + k$ with asymptotes
- **Key Concepts**:
  - Asymptotes (lines the graph approaches but never meets)
  - Horizontal and vertical asymptotes
  - Finding asymptotes from equations
  - Transformations and translations
  - Positive vs negative parameter effects
- **Subtopics**:
  - Rectangular hyperbola standard form
  - Finding asymptotes: substitute x = ∞ for horizontal, y = ∞ for vertical
  - Translation notation (h, k)
  - Graphing hyperbolas with intercepts and asymptotes
  - Reflections and transformations of hyperbolas
  - Applications (laser beam paths, drone trajectories)
- **Pages**: 13-17

### Topic 5: Circles
- **Definition**: Circles with center (h, k) and radius r follow the equation $(x-h)^2 + (y-k)^2 = r^2$
- **Key Concepts**:
  - Circle equation in standard form
  - Center and radius identification
  - Completing the square technique
  - Graphing circles with key points
  - Intercepts and intersections
- **Subtopics**:
  - General form to standard form conversion
  - Completing the square: $x^2 + bx + c = (x + \frac{b}{2})^2 - (\frac{b}{2})^2 + c$
  - Finding x-intercepts and y-intercepts
  - Sketching circles with labeled points
  - Exact vs approximate radius values
  - Applications (skate park design, circular structures)
- **Pages**: 21-24

---

## 2. Formulas and Theorems

### Function Notation
- **Statement**: A function relates each x-value to exactly one y-value
- **Formula**: $y = f(x)$
- **Variables**:
  - $x$ = independent variable (input)
  - $y$ = dependent variable (output)
  - $f$ = function name
- **When to Use**: When expressing relationships between variables
- **Example from Workbook**: Questions 1-2 use this to identify functions vs relations

### Vertical Line Test
- **Statement**: Every function only intersects a vertical line once
- **Formula**: Visual test on graphs
- **When to Use**: To determine if a graph represents a function
- **Example from Workbook**: Question 2 requires identifying which graphs are functions

### Set Intersection (AND)
- **Statement**: Intersection finds values in BOTH sets
- **Formula**: $A \cap B$ = What values are in set A AND in set B
- **Variables**:
  - $A$ = first set
  - $B$ = second set
  - $\cap$ = intersection symbol
- **When to Use**: Finding common elements between two sets
- **Example from Workbook**: Question 3 uses $A \cap B$ with perfect squares and multiples of 3

### Set Union (OR)
- **Statement**: Union finds values in EITHER set
- **Formula**: $A \cup B$ = What values are in set A OR in set B
- **Variables**:
  - $A$ = first set
  - $B$ = second set
  - $\cup$ = union symbol
- **When to Use**: Combining all elements from multiple sets
- **Example from Workbook**: Question 3 calculates $A \cup B = \{1, 3, 6, 9, 12, 15, 16, 18, 21, 24, 25, 27\}$

### Set Difference (Except)
- **Statement**: Set difference finds values in first set EXCEPT those also in second set
- **Formula**: $A \setminus B$ = What values are in set A, except those also in set B
- **Variables**:
  - $A$ = first set
  - $B$ = second set
  - $\setminus$ = set difference symbol
- **When to Use**: Removing elements of one set from another
- **Example from Workbook**: Question 3 shows $A \setminus B = \{1, 4, 16, 25\}$ (perfect squares not divisible by 3)

### Interval Notation - Parentheses (Non-Inclusive)
- **Statement**: Parentheses indicate the boundary value is NOT included
- **Formula**: $x \in (a, b) \Rightarrow a < x < b$
- **Variables**:
  - $a$ = lower boundary (not included)
  - $b$ = upper boundary (not included)
  - $x$ = variable
- **When to Use**: When endpoints are excluded from the interval
- **Example from Workbook**: Question 4a shows $(-5, 1) \cup (-2, 4) = (-5, 4)$

### Interval Notation - Square Brackets (Inclusive)
- **Statement**: Square brackets indicate the boundary value IS included
- **Formula**: $x \in [a, b] \Rightarrow a \leq x \leq b$
- **Variables**:
  - $a$ = lower boundary (included)
  - $b$ = upper boundary (included)
  - $x$ = variable
- **When to Use**: When endpoints are included in the interval
- **Example from Workbook**: Question 4b shows $[-3, 2) \cap (-1, 5] = (-1, 2)$

### Square Root Function - General Form
- **Statement**: Square root functions transform the basic square root shape
- **Formula**: $y = a\sqrt{b(x-h)} + k$
- **Variables**:
  - $a$ = vertical dilation (stretch/compression) and reflection
  - $b$ = horizontal dilation and reflection
  - $h$ = horizontal translation (shift right if positive)
  - $k$ = vertical translation (shift up if positive)
- **When to Use**: Expressing transformed square root functions
- **Example from Workbook**: Question 8 shows $y = \sqrt{x-3} - 2$ with domain $[3, \infty)$ and range $[-2, \infty)$

### Square Root Domain Restriction
- **Statement**: The expression inside a square root must be non-negative
- **Formula**: For $y = \sqrt{b(x-h)} + k$, require $b(x-h) \geq 0$
- **When to Use**: Finding the domain of square root functions
- **Example from Workbook**: Question 8 requires $x - 3 \geq 0$, so $x \geq 3$, giving domain $[3, \infty)$

### Rectangular Hyperbola - General Form
- **Statement**: Hyperbolas have the form of a fraction with asymptotes
- **Formula**: $y = \frac{a}{x-h} + k$
- **Variables**:
  - $a$ = determines vertical stretch and positive/negative orientation
  - $h$ = x-translation (vertical asymptote location)
  - $k$ = y-translation (horizontal asymptote location)
- **When to Use**: Expressing hyperbolic relationships
- **Example from Workbook**: Question 9 shows $y = \frac{1}{2x+3} - 1$ with vertical asymptote at $x = -\frac{3}{2}$ and horizontal asymptote at $y = -1$

### Finding Asymptotes
- **Statement**: Asymptotes are found by substituting infinity values
- **Formula**:
  - Horizontal asymptote: Sub $x = \infty$ → $y$ asymptote = $k$
  - Vertical asymptote: Sub $y = \infty$ → $x$ asymptote = $h$
- **When to Use**: Finding asymptotes of hyperbolas
- **Example from Workbook**: Question 9 finds asymptotes at $x = -\frac{3}{2}$ and $y = -1$

### Circle Equation - Standard Form
- **Statement**: A circle with center (h, k) and radius r has a specific equation
- **Formula**: $(x - h)^2 + (y - k)^2 = r^2$
- **Variables**:
  - $h$ = x-coordinate of center
  - $k$ = y-coordinate of center
  - $r$ = radius
- **When to Use**: Expressing circles algebraically, finding center and radius
- **Example from Workbook**: Question 15 shows $(x+5)^2 + (y-3)^2 = 25$ with center $(-5, 3)$ and radius $r = 5$

### Completing the Square
- **Statement**: Converting quadratic expressions to perfect square form
- **Formula**: $x^2 + bx + c = (x + \frac{b}{2})^2 - (\frac{b}{2})^2 + c$
- **Variables**:
  - $b$ = coefficient of x-term
  - $c$ = constant term
- **When to Use**: Converting circle equations from general to standard form, finding vertex of parabolas
- **Example from Workbook**: Question 16 converts $x^2 + y^2 - 14x + 8y + 40 = 0$ to $(x-7)^2 + (y+4)^2 = 25$

### Circle from General Form
- **Statement**: General form circle equations can be converted to standard form
- **Formula**: $x^2 + y^2 + Dx + Ey + F = 0$ converts to $(x - h)^2 + (y - k)^2 = r^2$ by completing the square
- **When to Use**: When given expanded circle equation
- **Example from Workbook**: Question 16 shows complete process of completing square for both x and y terms

---

## 3. Worked Examples Analysis

### Example 1: Set Operations with Defined Sets (Question 3)
- **Location**: Page 6
- **Topic**: Domain and Range - Set Operations
- **Problem Type**: Find set operations (union, intersection, difference)
- **Given Information**:
  - Set $A = \{x: x \text{ is a perfect square less than 30}\} = \{1, 4, 9, 16, 25\}$
  - Set $B = \{x: x \text{ is a positive multiple of 3 less than 30}\} = \{3, 6, 9, 12, 15, 18, 21, 24, 27\}$
- **Required**: Find $A \cup B$, $A \cap B$, $A \setminus B$, $B \setminus A$
- **Solution Method**:
  1. List all elements in set A (perfect squares: 1, 4, 9, 16, 25)
  2. List all elements in set B (multiples of 3: 3, 6, 9, 12, 15, 18, 21, 24, 27)
  3. For $A \cup B$: combine all unique elements from both sets (do not repeat)
  4. For $A \cap B$: find elements that appear in BOTH sets (only 9)
  5. For $A \setminus B$: find elements in A that are NOT in B (1, 4, 16, 25)
  6. For $B \setminus A$: find elements in B that are NOT in A (3, 6, 12, 15, 18, 21, 24, 27)
- **Key Formula Used**: Set notation and operations
- **Final Answer**:
  - $A \cup B = \{1, 3, 6, 9, 12, 15, 16, 18, 21, 24, 25, 27\}$
  - $A \cap B = \{9\}$
  - $A \setminus B = \{1, 4, 16, 25\}$
  - $B \setminus A = \{3, 6, 12, 15, 18, 21, 24, 27\}$
- **Answer Format**: Set notation with braces
- **Difficulty Level**: Basic

### Example 2: Interval Notation Union and Intersection (Question 4)
- **Location**: Page 7
- **Topic**: Domain and Range - Interval Operations
- **Problem Type**: Find union and intersection of intervals
- **Given Information**:
  - Part a: $(-5, 1) \cup (-2, 4)$
  - Part b: $[-3, 2) \cap (-1, 5]$
- **Required**: Simplify interval expressions
- **Solution Method**:
  1. Draw number line showing both intervals
  2. For union: combine all values in either interval (create spanning interval)
  3. For intersection: find only values in BOTH intervals (create overlap interval)
  4. Pay attention to open vs closed endpoints (parentheses vs brackets)
  5. Write final answer in interval notation
- **Key Formula Used**: Interval notation rules
- **Final Answer**:
  - Part a: $(-5, 4)$ (union spans from leftmost to rightmost point)
  - Part b: $(-1, 2)$ (intersection is only the overlap region)
- **Answer Format**: Interval notation with proper brackets
- **Difficulty Level**: Intermediate

### Example 3: Domain and Range from Quadratic Function (Question 6)
- **Location**: Page 8
- **Topic**: Domain and Range - Quadratic Functions
- **Problem Type**: Find domain, range, and equation from quadratic function
- **Given Information**:
  - Function $f: [-4, 1] \to R$
  - Rule: $f(x) = -(x-2)^2 + 5$
- **Required**: Domain, range, and equation of function
- **Solution Method**:
  1. Domain is GIVEN as $[-4, 1]$ (stated in function notation)
  2. Find turning point from equation form: $(h, k) = (2, 5)$
  3. Since domain restricts x-values, turning point is NOT included
  4. Evaluate function at domain boundaries: $f(-4) = -31$ and $f(1) = 4$
  5. Since parabola opens downward (negative coefficient), range goes from minimum value up
  6. Range is $[-31, 4]$ (from lowest boundary value to highest boundary value)
- **Key Formula Used**: Quadratic function in turning point form
- **Final Answer**:
  - Domain: $[-4, 1]$
  - Range: $[-31, 4]$
  - Equation: $f(x) = -(x-2)^2 + 5$
- **Answer Format**: Interval notation with square brackets
- **Difficulty Level**: Intermediate

### Example 4: Square Root Function Domain, Range, and Sketch (Question 8)
- **Location**: Page 12
- **Topic**: Square Root Functions
- **Problem Type**: Identify domain, range, sketch graph, label key points
- **Given Information**: $y = \sqrt{x-3} - 2$
- **Required**: Domain, range, graph sketch with labeled points
- **Solution Method**:
  1. Find domain: inside square root must be ≥ 0, so $x - 3 \geq 0$, thus $x \geq 3$
  2. Domain = $[3, \infty)$
  3. Find starting point: when $x = 3$, $y = \sqrt{0} - 2 = -2$, giving point $(3, -2)$
  4. Square root function increases as x increases, so range starts at -2 and goes up
  5. Range = $[-2, \infty)$
  6. Sketch: starting at $(3, -2)$, curve increases to the right
  7. Verify with another point: when $x = 7$, $y = \sqrt{4} - 2 = 0$, giving $(7, 0)$
- **Key Formula Used**: $y = \sqrt{x-h} + k$ with domain restriction
- **Final Answer**: Domain $[3, \infty)$, Range $[-2, \infty)$, graph labeled with $(3, -2)$
- **Answer Format**: Interval notation, coordinate pairs for key points
- **Difficulty Level**: Intermediate

### Example 5: Hyperbola Graphing with Asymptotes (Question 9)
- **Location**: Page 14
- **Topic**: Hyperbola
- **Problem Type**: Graph hyperbola, label intercepts and asymptotes
- **Given Information**: $y = \frac{1}{2x+3} - 1$
- **Required**: Graph with intercepts and asymptotes labeled
- **Solution Method**:
  1. Find vertical asymptote: set denominator = 0, so $2x + 3 = 0$, thus $x = -\frac{3}{2}$
  2. Find horizontal asymptote: as $x \to \infty$, $y \to -1$
  3. Find y-intercept: set $x = 0$, $y = \frac{1}{3} - 1 = -\frac{2}{3}$, giving $(0, -\frac{2}{3})$
  4. Find x-intercept: set $y = 0$, $0 = \frac{1}{2x+3} - 1$, so $1 = \frac{1}{2x+3}$, $2x+3 = 1$, $x = -1$, giving $(-1, 0)$
  5. Sketch hyperbola approaching asymptotes, passing through intercepts
  6. Label asymptotes with dashed lines and equations
- **Key Formula Used**: $y = \frac{a}{x-h} + k$ with asymptote finding rules
- **Final Answer**: Graph with vertical asymptote $x = -\frac{3}{2}$, horizontal asymptote $y = -1$, intercepts $(-1, 0)$ and $(0, -\frac{2}{3})$
- **Answer Format**: Labeled sketch with equations and coordinates
- **Difficulty Level**: Advanced

### Example 6: Hyperbola Transformation (Question 11)
- **Location**: Page 16
- **Topic**: Hyperbola transformations
- **Problem Type**: Apply transformations to hyperbola, find new equation and asymptotes
- **Given Information**:
  - Original: $y = \frac{1}{x}$ for $x > 0$
  - Transformations: reflection in x-axis, then translation 3 units up
- **Required**: Equation of transformed path, horizontal asymptote
- **Solution Method**:
  1. Start with $y = \frac{1}{x}$
  2. Reflection in x-axis changes sign: $y = -\frac{1}{x}$
  3. Translation UP by 3 adds 3 to the function: $y = -\frac{1}{x} + 3$
  4. Find horizontal asymptote: as $x \to \infty$, $y \to 3$
  5. Asymptote equation: $y = 3$ (the k-value after transformations)
- **Key Formula Used**: Transformation rules for hyperbolas
- **Final Answer**:
  - Transformed equation: $y = -\frac{1}{x} + 3$
  - Horizontal asymptote: $y = 3$
- **Answer Format**: Function equation and asymptote equation
- **Difficulty Level**: Intermediate

### Example 7: Circle Sketching from Equation (Question 15)
- **Location**: Page 22
- **Topic**: Circles
- **Problem Type**: Sketch circle from standard form equation, label key points
- **Given Information**: $(x+5)^2 + (y-3)^2 = 25$
- **Required**: Graph with all key points labeled
- **Solution Method**:
  1. Identify center: $(h, k)$ from $(x-h)^2 + (y-k)^2 = r^2$ format
  2. Rewrite as $(x-(-5))^2 + (y-3)^2 = 25$, so center is $(-5, 3)$
  3. Identify radius: $r^2 = 25$, so $r = 5$
  4. Find key points by moving radius distance from center:
     - Top: $(-5, 3+5) = (-5, 8)$
     - Bottom: $(-5, 3-5) = (-5, -2)$
     - Right: $(-5+5, 3) = (0, 3)$
     - Left: $(-5-5, 3) = (-10, 3)$
  5. Find intercepts by setting $y = 0$ and $x = 0$
  6. Sketch circle with center and key points labeled
- **Key Formula Used**: $(x-h)^2 + (y-k)^2 = r^2$
- **Final Answer**: Circle with center $(-5, 3)$, radius 5, labeled with points $(0, 3)$, $(-10, 3)$, $(-5, 8)$, $(-5, -2)$
- **Answer Format**: Labeled sketch with coordinates
- **Difficulty Level**: Intermediate

---

## 4. Difficulty Benchmarks

### Basic Level
- **Characteristics**:
  - Direct application of definitions
  - Single-step problems
  - Clearly stated information
  - Recognition and identification tasks
- **Typical Number Ranges**:
  - Small integers (-10 to 10)
  - Simple fractions (halves, thirds, quarters)
  - Perfect squares (1, 4, 9, 16, 25)
  - Multiples of 3, 5, or 10
- **Steps Required**: 1-2 steps
- **Formulas Used**:
  - Direct substitution into formulas
  - Basic set notation
  - Simple interval notation
- **Reference Examples**:
  - Question 1: Identify if relation is a function from table
  - Question 2: Identify functions from graphs using vertical line test
  - Question 3: List elements of sets and perform basic operations

### Intermediate Level
- **Characteristics**:
  - Multi-step problem solving
  - Requires understanding of transformations
  - Combining multiple concepts
  - Finding domain/range from equations
  - Graphing with key features
- **Typical Number Ranges**:
  - Integers from -20 to 20
  - Decimal values (1 decimal place)
  - Fractions including halves, thirds, quarters
  - Square roots and surds
- **Steps Required**: 3-5 steps
- **Formulas Used**:
  - Transformation formulas
  - Domain/range determination
  - Asymptote finding
  - Completing the square (single variable)
  - Intercept calculations
- **Reference Examples**:
  - Question 4: Interval union and intersection
  - Question 6: Domain and range from restricted quadratic
  - Question 7: Domain and range from exponential graph
  - Question 8: Square root function graphing
  - Question 9: Hyperbola graphing with asymptotes
  - Question 11: Hyperbola transformations
  - Question 15: Circle sketching

### Advanced Level
- **Characteristics**:
  - Complex multi-part questions
  - Application problems with context
  - Multiple transformations
  - Converting between forms
  - Completing the square for circles (two variables)
  - Finding exact values (surds, radicals)
  - Justification and explanation required
- **Typical Number Ranges**:
  - Larger integers (up to ±30)
  - Exact radical values ($\sqrt{80}$, $\sqrt{81}$)
  - Complex fractions
  - Parameter values requiring algebraic manipulation
- **Steps Required**: 5+ steps, multi-part questions
- **Formulas Used**:
  - Completing square for both x and y
  - Multiple transformations in sequence
  - Intersection of curves
  - Applied modeling with functions
- **Reference Examples**:
  - Question 10: Hyperbola graphing with transformation
  - Question 12: Sequence of transformations
  - Question 13: Modeling drone path (application)
  - Question 14: Skate park design (application with circle-line intersection)
  - Question 16: Circle from general form (completing square twice)
  - Question 17: Circle with exact radius calculation

---

## 5. Solution Strategies Taught

### Strategy 1: Vertical Line Test for Functions
- **When Used**: Determining if a graph represents a function
- **Steps**:
  1. Look at the graph
  2. Imagine or draw vertical lines at various x-positions
  3. Check if any vertical line intersects the graph more than once
  4. If any vertical line intersects twice or more → NOT a function
  5. If all vertical lines intersect at most once → IS a function
- **Example Problem Types**: Graph identification problems (Question 2)
- **Common Mistakes to Avoid**: Confusing vertical line test with horizontal line test

### Strategy 2: Set Operations from Descriptions
- **When Used**: Finding sets based on verbal descriptions, then performing operations
- **Steps**:
  1. Read the set description carefully
  2. List all elements that satisfy the condition within the stated range
  3. For intersection ($\cap$): find elements in BOTH sets
  4. For union ($\cup$): list ALL unique elements from either set (no repeats)
  5. For difference ($A \setminus B$): list elements in first set that are NOT in second
  6. Write answer in set notation with braces
- **Example Problem Types**: Question 3 (perfect squares and multiples)
- **Common Mistakes to Avoid**: Repeating elements in union, forgetting boundary values

### Strategy 3: Interval Operations with Number Line
- **When Used**: Union and intersection of intervals
- **Steps**:
  1. Draw a number line
  2. Mark and shade the first interval (use open circle for parenthesis, closed for bracket)
  3. Mark and shade the second interval on the same line
  4. For union: combine all shaded regions into one interval
  5. For intersection: only keep doubly-shaded region
  6. Check endpoints: open if from parenthesis, closed if from bracket
  7. Write answer in interval notation
- **Example Problem Types**: Question 4 and 5 (interval operations)
- **Common Mistakes to Avoid**: Mixing up parentheses and brackets, incorrect endpoint notation

### Strategy 4: Domain and Range from Function Equations
- **When Used**: Finding domain and range given a function rule
- **Steps**:
  1. For domain: identify any restrictions (square root ≥ 0, denominator ≠ 0)
  2. Solve inequality to find valid x-values
  3. Write domain in interval notation
  4. For range: identify transformation form (h, k) to find starting/ending values
  5. Consider function behavior (increasing/decreasing, maximum/minimum)
  6. If domain is restricted, evaluate function at boundary points
  7. Write range in interval notation
- **Example Problem Types**: Questions 6, 7, 8 (domain/range from equations)
- **Common Mistakes to Avoid**: Ignoring domain restrictions, not evaluating at boundaries

### Strategy 5: Square Root Function Graphing
- **When Used**: Sketching square root functions with transformations
- **Steps**:
  1. Identify form: $y = a\sqrt{b(x-h)} + k$
  2. Find starting point: solve $b(x-h) = 0$ for x, then substitute to find y
  3. This gives the turning point where square root "begins"
  4. Determine direction: positive $a$ means curve goes up-right, negative means down-right
  5. Plot starting point
  6. Choose additional x-values and calculate y-values (pick values that make perfect squares)
  7. Sketch smooth curve through points
  8. Label key points with coordinates
- **Example Problem Types**: Question 8 (square root graphing)
- **Common Mistakes to Avoid**: Wrong starting point, incorrect direction, unlabeled points

### Strategy 6: Finding Hyperbola Asymptotes
- **When Used**: Determining asymptotes of hyperbola functions
- **Steps**:
  1. Write function in form $y = \frac{a}{x-h} + k$ (may need algebraic manipulation)
  2. Vertical asymptote: set denominator = 0 and solve for x
  3. This gives $x = h$ (the x-translation value)
  4. Horizontal asymptote: identify the k-value (constant term added outside fraction)
  5. This gives $y = k$ (the y-translation value)
  6. Alternative: as $x \to \infty$, the fraction $\to 0$, leaving only k
  7. Write asymptote equations and draw as dashed lines on graph
- **Example Problem Types**: Questions 9, 10 (hyperbola asymptotes)
- **Common Mistakes to Avoid**: Confusing h and k positions, algebraic errors in solving

### Strategy 7: Hyperbola Graphing with Intercepts
- **When Used**: Complete graphing of hyperbola with all key features
- **Steps**:
  1. Find vertical asymptote (set denominator = 0)
  2. Find horizontal asymptote (identify k-value)
  3. Find y-intercept: substitute $x = 0$ and solve for y
  4. Find x-intercept: substitute $y = 0$ and solve for x
  5. Draw asymptotes as dashed lines
  6. Plot intercepts
  7. Sketch hyperbola curves approaching asymptotes and passing through intercepts
  8. Label all key points and asymptote equations
- **Example Problem Types**: Questions 9, 10 (complete hyperbola sketches)
- **Common Mistakes to Avoid**: Curves crossing asymptotes, missing intercepts, incorrect curve shape

### Strategy 8: Function Transformations in Sequence
- **When Used**: Applying multiple transformations to a function
- **Steps**:
  1. Start with base function equation
  2. Apply transformations in order given (order matters!)
  3. Reflection in x-axis: multiply entire function by -1
  4. Reflection in y-axis: replace x with -x
  5. Vertical translation: add constant to entire function
  6. Horizontal translation: replace x with (x - h)
  7. Write final transformed equation
  8. Update asymptotes or key features accordingly
- **Example Problem Types**: Questions 11, 12 (transformation sequences)
- **Common Mistakes to Avoid**: Wrong transformation order, sign errors, forgetting to update features

### Strategy 9: Completing the Square for Circles
- **When Used**: Converting circle equation from general form to standard form
- **Steps**:
  1. Group x-terms and y-terms: $(x^2 + Dx) + (y^2 + Ey) = -F$
  2. For x-terms: take half of coefficient of x: $(\frac{D}{2})^2$
  3. Add and subtract this value: $(x^2 + Dx + (\frac{D}{2})^2) - (\frac{D}{2})^2$
  4. Factor perfect square: $(x + \frac{D}{2})^2$
  5. Repeat for y-terms: $(y + \frac{E}{2})^2$
  6. Move subtracted squares to right side
  7. Simplify right side to get $r^2$
  8. Identify center $(h, k)$ and radius $r$
- **Example Problem Types**: Questions 16, 17 (circle conversions)
- **Common Mistakes to Avoid**: Sign errors when completing square, forgetting to add to both sides, arithmetic errors

### Strategy 10: Circle Sketching from Standard Form
- **When Used**: Graphing a circle given its equation
- **Steps**:
  1. Identify center $(h, k)$ from $(x-h)^2 + (y-k)^2 = r^2$
  2. Calculate radius: $r = \sqrt{r^2}$
  3. Plot center point
  4. From center, move radius distance in 4 directions (up, down, left, right)
  5. Plot these 4 key points
  6. Find intercepts if needed: set $x=0$ for y-intercepts, $y=0$ for x-intercepts
  7. Draw smooth circle through all points
  8. Label center, radius, and key points with coordinates
- **Example Problem Types**: Questions 15, 16, 17 (circle sketching)
- **Common Mistakes to Avoid**: Wrong center signs, incorrect radius calculation, non-circular shape

---

## 6. Common Patterns

### Number Patterns Used

**Integers:**
- Small integers: -10 to 10 (basic problems)
- Medium integers: -20 to 20 (intermediate problems)
- Larger integers: up to ±30 (advanced problems)
- Perfect squares: 1, 4, 9, 16, 25 (set problems)
- Multiples: 3, 6, 9, 12, ... (set problems)

**Decimals:**
- Precision: typically 1-2 decimal places
- Common values: 0.5, 1.5, 2.5 (half integers)
- Fractions as decimals: $\frac{1}{3} = -0.67$ (approximate)
- Exact fractions preferred over decimals in answers

**Fractions:**
- Common denominators: 2, 3, 4
- Examples: $\frac{1}{2}, \frac{1}{3}, \frac{2}{3}, \frac{1}{4}, \frac{3}{4}$
- Negative fractions: $-\frac{2}{3}, -\frac{3}{2}$
- Improper fractions in intermediate steps

**Special Values:**
- Square roots: $\sqrt{2}, \sqrt{3}, \sqrt{4}, \sqrt{5}$
- Exact radicals: $\sqrt{25} = 5, \sqrt{80}, \sqrt{81}$
- Infinity notation: $\infty$ for unbounded ranges
- Zero as key reference point

**Measurements:**
- Distance: 0-16 meters (drone problem)
- Time: 0-16 seconds
- Diameter: 8 meters (circle problem)
- Horizontal distance: 15 meters (ramp problem)

### Question Formats

**Format 1: "Identify/Determine whether..." with table/graph**
- Example: "For each table of values below, decide whether the relation is a function"
- Provides: Table or graph
- Requires: Yes/No answer or identification
- Common in: Questions 1, 2

**Format 2: "Find the following..." with set/interval operations**
- Example: "Find $A \cup B, A \cap B, A \setminus B, B \setminus A$"
- Provides: Set descriptions or intervals
- Requires: Computed set or interval
- Common in: Questions 3, 4, 5

**Format 3: "State/Identify the domain and range..."**
- Example: "What is the domain, range and equation of the function?"
- Provides: Function equation or graph
- Requires: Interval notation for domain and range
- Common in: Questions 6, 7, 8

**Format 4: "Graph/Sketch the following..." with labels**
- Example: "Sketch the graph on the axes below. Label the intercept(s) and asymptote(s)"
- Provides: Function equation
- Requires: Accurate sketch with labeled features
- Common in: Questions 8, 9, 10, 15, 16

**Format 5: "Describe the transformation..." or "Write the equation..."**
- Example: "Describe the sequence of transformations that maps $y = \sqrt{x}$ to $y = -\sqrt{x} + 3$"
- Provides: Initial and final functions
- Requires: Step-by-step transformation description or new equation
- Common in: Questions 11, 12

**Format 6: Multi-part application problems**
- Example: "A skate park design includes... a. Write equation b. Sketch graph c. Calculate height"
- Provides: Real-world context
- Requires: Multiple related answers across parts
- Common in: Questions 13, 14 (extension problems)

**Format 7: "Extension" questions**
- Labeled explicitly as extensions
- Typically worth more marks (2-3 marks per part)
- Require deeper understanding and multi-step solutions
- Common in: Questions 13, 14, 17

### Answer Expectations

**Exact vs Approximate:**
- **Exact expected**: When answer involves surds, fractions, or simple integers
  - Examples: $r = 5$, $r = \sqrt{81} = 9$, center $(-5, 3)$
  - Radical form: $r = \sqrt{80} = 4\sqrt{5}$ (simplified surd)
- **Approximate acceptable**: When explicitly asked or when exact is very complex
  - Example: Domain from graph (visual estimation acceptable)
  - Typically round to 1-2 decimal places if approximating

**Units:**
- **Required when**: Problem involves real-world measurements
  - "15 meters", "16 seconds", "8 metres diameter"
- **Not required when**: Abstract mathematical problems
  - Domain/range in pure number form
- **Consistency**: Maintain units throughout problem (metres vs meters)

**Significant Figures:**
- Not explicitly emphasized in workbook
- Answers typically given as exact values or simple decimals
- When rounding needed: 1-2 decimal places standard

**Working Required:**
- **Basic questions**: Answer only may be acceptable
- **Walkthrough questions**: Full working shown in solutions
  - Step-by-step algebraic manipulation
  - Substitutions shown explicitly
  - Intermediate calculations displayed
- **Extension questions**: Working expected given higher mark allocation
- **Graphing questions**:
  - Key points must be labeled with coordinates
  - Asymptotes labeled with equations
  - Center and radius stated for circles

**Notation Standards:**
- Set notation: Use braces $\{...\}$ with commas between elements
- Interval notation: Use $[$ or $($ consistently, with comma separating endpoints
- Infinity: Use $\infty$ symbol, always with parenthesis (never bracket)
- Function notation: $f(x)$ or $y =$ acceptable
- Coordinate points: Use parentheses $(x, y)$
- Equations: State clearly "$y = ...$" or "$x = ...$" for asymptotes

---

## 7. Visual Diagram Patterns

### 7.1 Diagram Configuration → Concept Mapping

| Concept/Theorem | Diagram Configuration | Key Visual Elements | How to Recognize |
|-----------------|----------------------|---------------------|------------------|
| Function vs Relation | Table with x and y columns | Each x-value paired with y-value(s) | If any x repeats with different y → relation. If each x appears once → function |
| Vertical Line Test | Graph on coordinate plane | Various curve types | Draw imaginary vertical lines. If any intersects curve twice → not function |
| Set Elements | Bag/collection diagram with numbered balls | Numbers in visual container | Numbers represent discrete elements in set |
| Interval on Number Line | Horizontal line with marked points | Open circles (non-inclusive), closed circles (inclusive), shaded region between | Shading shows included values, circle type shows endpoint inclusion |
| Union of Intervals | Two overlapping shaded regions on number line | Separate shaded regions combining | Combined shading spans from leftmost to rightmost point |
| Intersection of Intervals | Overlapping portion of two shaded regions | Only doubly-shaded area counts | Result is only where both intervals overlap |
| Square Root Function | Curved graph starting at point, extending right-upward | Starting point (h, k), curve increases to right | Starts at specific point, grows like half-parabola sideways |
| Square Root Reflection | Curved graph with different orientations | Curve direction changes (up-right vs down-right vs up-left vs down-left) | Negative 'a' flips vertically, negative 'b' flips horizontally |
| Rectangular Hyperbola | Two separate curve branches with asymptotes | Dashed vertical and horizontal lines, curves in opposite quadrants | Curves approach but never touch dashed lines (asymptotes) |
| Hyperbola Intercepts | Points where hyperbola crosses axes | Labeled points on x-axis and y-axis | Curves pass through these specific coordinate points |
| Circle (Standard Form) | Circular shape centered at point | Center point, radius lines to edge, key points at cardinal directions | Perfect circle with marked center and 4 key points (up, down, left, right) |
| Circle Intercepts | Points where circle crosses axes | Labeled intersection points with coordinate axes | Circle crosses axes at specific calculable points |

### 7.2 Visual Elements and Their Meaning

| Visual Element | What It Indicates | Testing Aspect |
|----------------|-------------------|----------------|
| **Table with repeated x-value** | Not a function (fails vertical line test) | Student must recognize one-to-one correspondence |
| **Open circle on number line** | Boundary not included (parenthesis notation) | Understanding of inclusive vs non-inclusive |
| **Closed circle on number line** | Boundary included (bracket notation) | Understanding of inclusive vs non-inclusive |
| **Shaded region on number line** | Values included in interval/set | Visual representation of domain/range |
| **Dashed line (asymptote)** | Line that curve approaches but never touches | Identifying limiting behavior of functions |
| **Solid curve** | The actual function graph | Distinguishing function from asymptotes |
| **Labeled point (x, y)** | Specific coordinate student should identify | Intercepts, turning points, key features |
| **Coordinate axes with grid** | Graph to be sketched | Student must draw accurate function shape |
| **Arrow on curve** | Direction of function behavior | Indicates function continues infinitely |
| **Center point marked** | Circle center or function center | Reference point for transformations |
| **Radius line** | Distance from center to edge | Measurement of circle size |

### 7.3 Standard Diagram Patterns by Topic

**Functions and Correspondence:**
```
Pattern: Table or Graph → Function Determination
├── Table with unique x-values → Function
├── Table with repeated x-values → Not a function (relation)
├── Graph passing vertical line test → Function
└── Graph failing vertical line test → Not a function
```

**Set Operations:**
```
Pattern: Number Line or List → Combined Set
├── Two separate lists → Union combines all unique elements
├── Two separate lists → Intersection finds common elements
├── Two separate lists → Difference removes second from first
└── Visual bag with numbered balls → Concrete set representation
```

**Interval Operations:**
```
Pattern: Number Line with Shaded Regions
├── Two intervals side-by-side → Union spans entire range
├── Two intervals overlapping → Intersection is overlap only
├── Parentheses boundary → Open circle (not included)
└── Bracket boundary → Closed circle (included)
```

**Square Root Functions:**
```
Pattern: Transformed Square Root Curve
├── Standard (a > 0, b > 0) → Starts bottom-left, curves up-right
├── x-axis reflection (a < 0) → Starts top-left, curves down-right
├── y-axis reflection (b < 0) → Starts bottom-right, curves up-left
└── Both reflections (a < 0, b < 0) → Starts top-right, curves down-left
```

**Hyperbola:**
```
Pattern: Two-Branch Curve with Asymptotes
├── Positive 'a' → Branches in quadrants I and III (positive correlation)
├── Negative 'a' → Branches in quadrants II and IV (negative correlation)
├── Vertical asymptote at x = h → Vertical dashed line
└── Horizontal asymptote at y = k → Horizontal dashed line
```

**Circles:**
```
Pattern: Circular Shape with Key Features
├── Center at (h, k) → Marked center point
├── Radius r → Distance from center to edge
├── Four cardinal points → (h±r, k) and (h, k±r)
└── Intercepts → Where circle crosses axes (found by substitution)
```

### 7.4 Diagram Variations in Workbook

| Concept | Variation 1 | Variation 2 | Variation 3 |
|---------|-------------|-------------|-------------|
| Function identification | Table format | Smooth curve graph | Piecewise graph |
| Interval notation | Union of non-overlapping intervals | Union of overlapping intervals | Intersection of intervals |
| Square root function | Standard orientation (up-right) | Reflected in x-axis (down-right) | With vertical and horizontal shift |
| Hyperbola | Standard reciprocal (origin-centered) | Translated horizontally and vertically | With intercepts labeled |
| Circle | Standard form directly given | General form requiring completing square | With line intersection (application) |
| Domain/range | From equation (calculate) | From graph (read visually) | From restricted function notation |

**Pedagogical Pattern**: Workbook progresses from:
1. **Recognition** (identify from given information)
2. **Calculation** (apply formulas to find features)
3. **Graphing** (create visual representation with labels)
4. **Application** (use concepts in real-world context)

This allows the question generator to choose DIFFERENT but VALID diagram configurations that test the SAME concept at appropriate difficulty levels.

---

## 8. Constraints for Question Variations

### MUST DO:

1. **Only use formulas documented in Section 2**
   - Function notation and vertical line test
   - Set operations (intersection, union, difference)
   - Interval notation (parentheses and brackets)
   - Square root function transformations
   - Hyperbola standard form and asymptotes
   - Circle equation and completing the square

2. **Match difficulty levels defined in Section 4**
   - Basic: 1-2 steps, direct application, small integers
   - Intermediate: 3-5 steps, transformations, calculations
   - Advanced: 5+ steps, applications, exact values with surds

3. **Follow solution strategies from Section 5**
   - Use number lines for interval operations
   - Complete the square properly for circles
   - Find asymptotes using substitution method
   - Apply transformations in correct sequence

4. **Use number patterns from Section 6**
   - Integers primarily in range -30 to 30
   - Common fractions: halves, thirds, quarters
   - Perfect squares for sets: 1, 4, 9, 16, 25, 36, ...
   - Exact radical form preferred: $\sqrt{25} = 5$, not 5.0

5. **Maintain question formats from Section 6**
   - "Identify whether..." for recognition tasks
   - "Find..." for calculation tasks
   - "Sketch/Graph..." for graphing tasks with "label all key points"
   - "Describe..." for transformation tasks
   - Multi-part questions for applications (labeled a, b, c, etc.)

### MUST NOT:

1. **Introduce formulas not taught in this workbook**
   - No trigonometric functions (sin, cos, tan)
   - No logarithmic functions
   - No exponential functions beyond context (seen in graph but not formula)
   - No polynomial functions beyond quadratics
   - No calculus (derivatives, integrals)

2. **Exceed the advanced difficulty benchmark**
   - Keep number ranges reasonable (max ±30 for integers)
   - Maximum 2-3 transformations in sequence
   - Avoid overly complex algebra
   - Extension questions should be challenging but achievable with curriculum knowledge

3. **Require methods not demonstrated in worked examples**
   - Don't ask for proof or derivation
   - Don't require advanced algebraic techniques beyond completing the square
   - Don't require calculator-specific methods
   - Don't assume knowledge of advanced circle theorems

4. **Use number ranges outside documented patterns**
   - Avoid decimals beyond 2 decimal places
   - Avoid fractions with denominators > 4 unless simplified
   - Avoid irrational numbers except common surds ($\sqrt{2}, \sqrt{3}, \sqrt{5}$, etc.)
   - Avoid very large numbers (>100) unless in context like squared values

### ADDITIONAL GUIDELINES:

**For Set Questions:**
- Define sets clearly with conditions (e.g., "less than 30", "perfect squares")
- Use realistic set sizes (5-10 elements typical)
- Ensure operations produce meaningful results (intersection not empty unless intentional)

**For Interval Questions:**
- Use integer or half-integer boundaries preferred
- Mix inclusive and non-inclusive endpoints for variety
- Ensure union and intersection produce valid intervals

**For Function Questions:**
- Always specify domain if restricted
- Include both tables and graphs for variety
- Ensure "not a function" examples have clear repeated x-values

**For Graphing Questions:**
- Always state "label all key points" or similar
- Specify what features to label (intercepts, asymptotes, center, etc.)
- Provide coordinate axes when sketch required

**For Transformation Questions:**
- State transformations in clear, sequential language
- Specify order of transformations when multiple applied
- Include both algebraic and geometric interpretations

**For Application Questions:**
- Use realistic contexts (skate parks, drones, beams, etc.)
- Ensure measurements have appropriate units
- Multi-part questions should build logically (parts connect)

---

## Summary Statistics

- **Total Topics**: 5 (Functions, Domain/Range, Square Root Functions, Hyperbola, Circles)
- **Total Formulas/Theorems**: 14 key formulas
- **Worked Examples Analyzed**: 7 detailed walkthroughs
- **Total Questions in Workbook**: 17 questions
- **Difficulty Distribution**:
  - Basic: ~35% (Questions 1, 2, 3)
  - Intermediate: ~45% (Questions 4, 5, 6, 7, 8, 9, 11, 12, 15)
  - Advanced: ~20% (Questions 10, 13, 14, 16, 17 - extensions)
- **Question Format Distribution**:
  - Identification: 2 questions (1, 2)
  - Calculation: 5 questions (3, 4, 5, 6, 7)
  - Graphing: 5 questions (8, 9, 10, 15, 16)
  - Transformation: 2 questions (11, 12)
  - Application/Extension: 3 questions (13, 14, 17)

**Coverage Summary:**
This workbook comprehensively covers foundational concepts in functions and their graphical representations, with emphasis on:
- Understanding function definitions and properties
- Set theory and interval notation
- Transformations of standard function forms (square root, hyperbola, circle)
- Graphical analysis and sketching skills
- Real-world applications of mathematical functions

**Pedagogical Approach:**
- Definitions provided with visual aids
- Scaffolded progression from recognition to application
- Worked solutions demonstrate complete method
- Extension questions challenge advanced understanding
- Balance of procedural skills and conceptual understanding
