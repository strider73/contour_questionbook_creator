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
