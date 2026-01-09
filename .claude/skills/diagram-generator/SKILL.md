# Diagram Generator Skill

Generate NEW diagrams for test question variations. This skill provides a flexible, configuration-driven system that can be extended for any curriculum topic.

## Quick Pattern Lookup (CHECK FIRST!)

Before writing any diagram code, check if a pattern exists:

| Category | Script | Available Types |
|----------|--------|-----------------|
| **Geometry** | `geometry_diagrams.py` | `circle_inscribed`, `circle_segment`, `circle_theorem`, `solid_similar`, `solid_composite`, `area_composite`, `prism` |
| **Statistics** | `statistics_diagrams.py` | `venn`, `tree_simple`, `tree`, `two_way_table`, `box_plot`, `scatter`, `histogram`, `stem_leaf`, `normal` |
| **Polynomial** | `polynomial_diagrams.py` | `cubic_graph`, `blank_grid`, `quartic_tp` |

**Pattern exists?** → Use it directly with config
**Pattern missing?** → Follow "Self-Extending Algorithm" section below to add it FIRST, then use

## Overview

Three Python scripts organized by mathematical domain:
1. **geometry_diagrams.py** - Circles, 3D shapes, composite areas, prisms
2. **statistics_diagrams.py** - Venn diagrams, tree diagrams, box plots, scatter plots, tables
3. **polynomial_diagrams.py** - Polynomial graphs (cubics, quartics), coordinate grids for sketching

## Design Philosophy

- **Configuration-driven**: All diagrams accept a config dict, making them easy to customize
- **Extensible**: Add new diagram types by following the pattern and registering in DIAGRAM_REGISTRY
- **Topic-agnostic**: Organized by diagram CATEGORY, not curriculum topic (works for any AOS)

## Quick Start

### Generate Geometry Diagrams

```python
# Import and use directly
import sys
sys.path.append('.claude/skills/diagram-generator/scripts')
from geometry_diagrams import generate_diagram

# Circle with inscribed square
generate_diagram('circle_inscribed', {
    'outer_shape': 'circle',
    'inner_shape': 'square',
    'dimension': 9,
    'dimension_label': '9 cm',
    'output_path': 'new_images/q6.png'
})

# Two secants from external point
generate_diagram('circle_theorem', {
    'theorem_type': 'two_secants',
    'segments': {'pa': 3, 'ab': 5, 'pc': 'x', 'cd': 4},
    'output_path': 'new_images/q9.png'
})

# Composite solid (lighthouse)
generate_diagram('solid_composite', {
    'components': [
        {'type': 'cylinder', 'radius': 2.5, 'height': 18},
        {'type': 'cone', 'radius': 2.5, 'height': 5}
    ],
    'title': 'Lighthouse',
    'output_path': 'new_images/q18.png'
})
```

### Generate Statistics Diagrams

```python
from statistics_diagrams import generate_diagram

# Venn diagram (2 sets)
generate_diagram('venn', {
    'num_sets': 2,
    'values': {'a_only': 17, 'b_only': 12, 'both': 8, 'neither': 13},
    'labels': {'a': 'Cat', 'b': 'Dog'},
    'total': 50,
    'output_path': 'new_images/q6_venn.png'
})

# Tree diagram (with replacement)
generate_diagram('tree_simple', {
    'items': {'R': 2, 'B': 1},
    'stages': 2,
    'replacement': True,
    'output_path': 'new_images/q11_tree.png'
})

# Box plot comparison
generate_diagram('box_plot', {
    'datasets': [
        {'min': 45, 'q1': 52, 'median': 58, 'q3': 65, 'max': 78},
        {'min': 50, 'q1': 60, 'median': 68, 'q3': 75, 'max': 85}
    ],
    'labels': ['Class A', 'Class B'],
    'show_values': True,
    'output_path': 'new_images/q9_boxplot.png'
})

# Scatter plot with line of best fit
generate_diagram('scatter', {
    'x_data': [18, 20, 22, 24, 26, 28, 30],
    'y_data': [40, 50, 55, 70, 75, 85, 95],
    'x_label': 'Temperature (°C)',
    'y_label': 'Ice creams sold',
    'show_lobf': True,
    'output_path': 'new_images/q15_scatter.png'
})
```

### Generate Polynomial Diagrams

```python
from polynomial_diagrams import generate_diagram

# Cubic graph for reading intercepts
generate_diagram('cubic_graph', {
    'x_intercepts': [-3, 1, 4],
    'leading_coef': 1,
    'output_path': 'new_images/q5_cubic.png'
})

# Blank grid for quartic sketching (turning point form)
generate_diagram('blank_grid', {
    'x_range': [-4, 5],
    'y_range': [-20, 20],
    'y_tick_spacing': 5,
    'output_path': 'new_images/q9_grid.png'
})

# Blank grid for cubic sketching with specific interval
generate_diagram('blank_grid', {
    'x_range': [-1, 6],
    'y_range': [-20, 60],
    'y_tick_spacing': 10,
    'output_path': 'new_images/q15e_grid.png'
})

# Quartic in turning point form (with or without curve)
generate_diagram('quartic_tp', {
    'h': 1,           # horizontal shift
    'k': -16,         # vertical shift
    'show_curve': False,  # False = blank grid only
    'x_range': [-4, 5],
    'y_range': [-20, 20],
    'output_path': 'new_images/quartic_grid.png'
})
```

### CLI Usage

```bash
# Generate examples
python3 .claude/skills/diagram-generator/scripts/geometry_diagrams.py
python3 .claude/skills/diagram-generator/scripts/statistics_diagrams.py

# Generate specific diagram with config
python3 .claude/skills/diagram-generator/scripts/geometry_diagrams.py \
    -t circle_inscribed \
    -c '{"outer_shape": "circle", "inner_shape": "square", "dimension": 9}' \
    -o new_images/custom.png
```

## Available Diagram Types

### Geometry Diagrams

| Type | Description | Key Config Options |
|------|-------------|-------------------|
| `circle_inscribed` | Circle/square inscribed combinations | `outer_shape`, `inner_shape`, `dimension` |
| `circle_segment` | Minor/major segment with central angle | `radius`, `angle` |
| `circle_theorem` | Tangent-secant, two secants, chord perpendicular | `theorem_type`, `segments` |
| `solid_similar` | Two similar solids (cones, cylinders) | `solid_type`, `dim1`, `dim2` |
| `solid_composite` | Composite 3D (cylinder+cone, etc.) | `components` list |
| `area_composite` | Annulus, square with path | `shape_type`, `dimensions` |
| `prism` | Triangular, trapezoidal prisms | `cross_section`, `dimensions` |

### Statistics Diagrams

| Type | Description | Key Config Options |
|------|-------------|-------------------|
| `venn` | 2 or 3 set Venn diagrams | `num_sets`, `values`, `labels` |
| `tree_simple` | Common tree diagram scenarios | `items`, `stages`, `replacement` |
| `tree` | Custom tree structure | `branches` list |
| `two_way_table` | Contingency table | `data`, `row_labels`, `col_labels` |
| `box_plot` | Single or comparison box plots | `datasets`, `labels`, `outliers` |
| `scatter` | Scatter plot with optional LOBF | `x_data`, `y_data`, `show_lobf` |
| `histogram` | Frequency histogram | `data`, `bins` |
| `stem_leaf` | Stem-and-leaf plot | `data`, `stem_unit` |
| `normal` | Normal distribution curve | `mean`, `std`, `show_regions` |

### Polynomial Diagrams (AOS 8 - Polynomials)

| Type | Description | Key Config Options |
|------|-------------|-------------------|
| `cubic_graph` | Cubic curve for reading intercepts | `x_intercepts`, `leading_coef`, `x_range`, `y_range` |
| `blank_grid` | Empty coordinate grid for sketching | `x_range`, `y_range`, `x_tick_spacing`, `y_tick_spacing` |
| `quartic_tp` | Quartic in turning point form | `h`, `k`, `a`, `show_curve`, `x_range`, `y_range` |

## Self-Extending Algorithm (CRITICAL)

When you encounter a diagram that **doesn't match any existing pattern**, you MUST extend the skill on-the-fly:

### Step 1: Detect Missing Pattern

Check if the required diagram type exists:
```python
# Available patterns by script:
# geometry_diagrams.py: circle_inscribed, circle_segment, circle_theorem, solid_similar, solid_composite, area_composite, prism
# statistics_diagrams.py: venn, tree_simple, tree, two_way_table, box_plot, scatter, histogram, stem_leaf, normal
# polynomial_diagrams.py: cubic_graph, blank_grid, quartic_tp
```

If the diagram type is NOT in the list above → **CREATE NEW PATTERN**

### Step 2: Determine Target Script

Choose the appropriate script based on diagram category:
- **Geometry** (shapes, circles, 3D solids, areas) → `geometry_diagrams.py`
- **Statistics** (data visualization, probability) → `statistics_diagrams.py`
- **Polynomial/Algebra** (graphs, coordinate grids, functions) → `polynomial_diagrams.py`
- **New category needed?** → Create new script: `{category}_diagrams.py`

### Step 3: Create the Pattern Function

Use this template:
```python
def create_{diagram_type}(config):
    """
    {Description of what this diagram shows}

    Config:
        {param1}: {description} (default: {value})
        {param2}: {description} (default: {value})
        output_path: Where to save (default: new_images/{type}.png)
        figsize: Tuple (width, height) in inches (default (8, 8))

    Returns:
        dict with key values for answer key (if applicable)
    """
    # Extract config with defaults
    param1 = config.get('param1', default_value)
    output_path = config.get('output_path', 'new_images/{type}.png')
    figsize = config.get('figsize', (8, 8))

    # Create figure
    fig, ax = plt.subplots(figsize=figsize)

    # === DRAWING CODE HERE ===
    # Use matplotlib to draw the diagram
    # Follow quality standards: 150 DPI, white background, clear labels

    # Save
    save_diagram(fig, output_path)

    # Return key values (optional, for answer generation)
    return {'key': value}
```

### Step 4: Register in DIAGRAM_REGISTRY

Add to the appropriate script's registry:
```python
DIAGRAM_REGISTRY = {
    # ... existing types ...
    '{new_type}': create_{new_type},
}
```

### Step 5: Update SKILL.md Documentation

Add the new type to the "Available Diagram Types" table in this file.

### Step 6: Use Immediately

```python
generate_diagram('{new_type}', {config})
```

---

### Example: Adding a New Pattern On-The-Fly

**Scenario**: Need a "number_line" diagram for AOS 5 (Linear Relations)

**Step 1**: Check existing patterns → Not found

**Step 2**: Category = Algebra/Functions → Add to `polynomial_diagrams.py`

**Step 3**: Create function:
```python
def create_number_line(config):
    """Number line with marked points and intervals."""
    x_range = config.get('x_range', [-10, 10])
    points = config.get('points', [])  # List of {value, label, style}
    output_path = config.get('output_path', 'new_images/number_line.png')

    fig, ax = plt.subplots(figsize=(10, 2))
    # ... drawing code ...
    save_diagram(fig, output_path)
```

**Step 4**: Register:
```python
DIAGRAM_REGISTRY['number_line'] = create_number_line
```

**Step 5**: Update this SKILL.md with new entry in table

**Step 6**: Use:
```python
generate_diagram('number_line', {'x_range': [-5, 5], 'points': [{'value': 2, 'label': 'x'}]})
```

---

## Manual Extension (Alternative)

### Adding a New Diagram Type

1. Create a function in the appropriate script:

```python
def create_new_diagram_type(config):
    """
    Description of what this diagram shows.

    Config:
        param1: Description
        param2: Description
        output_path: Where to save
        title: Optional title
    """
    # Get config values with defaults
    param1 = config.get('param1', default_value)
    output_path = config.get('output_path', 'new_images/default.png')

    fig, ax = plt.subplots(figsize=(5, 5), dpi=150)

    # ... drawing code ...

    save_diagram(fig, output_path)
```

2. Register in DIAGRAM_REGISTRY:

```python
DIAGRAM_REGISTRY = {
    # ... existing types ...
    'new_diagram_type': create_new_diagram_type,
}
```

3. Use it:

```python
generate_diagram('new_diagram_type', {'param1': value, ...})
```

## Quality Standards

All diagrams follow these standards:
- **Resolution**: 150 DPI for print quality
- **Aspect ratio**: `ax.set_aspect('equal')` for geometric shapes
- **Background**: White (`facecolor='white'`)
- **Labels**: Clear, readable font sizes (10-12pt)
- **Output**: PNG format in `new_images/` folder

## Integration with Question Generator

The `curriculum-aligned-question-generator` agent should:

1. **Identify diagram type** from ExtractedQuestions.md
2. **Map to diagram category** (circle_theorem, venn, box_plot, etc.)
3. **Build config** with new values matching the fresh question
4. **Call generate_diagram()** with appropriate script
5. **Verify output** with `ls new_images/`

Example workflow:

```
1. Read ExtractedQuestions.md → Q6 has Venn diagram with cat/dog data
2. Design fresh question: survey about sports preferences
3. Build config:
   {
     'num_sets': 2,
     'values': {'a_only': 25, 'b_only': 18, 'both': 12, 'neither': 5},
     'labels': {'a': 'Football', 'b': 'Basketball'},
     'total': 60,
     'output_path': 'new_images/q6_venn.png'
   }
4. Run: generate_diagram('venn', config)
5. Verify: ls new_images/q6_venn.png
```

## File Structure

```
.claude/skills/diagram-generator/
├── SKILL.md                      # This file
└── scripts/
    ├── geometry_diagrams.py      # Circles, 3D solids, areas, prisms
    ├── statistics_diagrams.py    # Venn, tree, table, box plot, scatter
    └── polynomial_diagrams.py    # Cubic/quartic graphs, coordinate grids
```

## Dependencies

Required Python packages:
- `matplotlib` - Diagram creation
- `numpy` - Mathematical calculations
