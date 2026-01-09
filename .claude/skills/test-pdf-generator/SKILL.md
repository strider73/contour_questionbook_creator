# Test PDF Generator Skill

Generate professional test/exam PDFs with questions, diagrams, and working space.

## Overview

This skill creates formatted test papers in PDF format, designed for mathematics assessments. It handles:
- Title pages with test information
- Question formatting with mark allocation
- Embedded diagrams with correct aspect ratios
- Working space for student answers
- Multi-part questions
- Section headers

## When to Use

This skill is triggered by `curriculum-aligned-question-generator` agent at the final step when creating the Version B test PDF.

**Trigger point in workflow:**
```
/generate-test → ... → curriculum-aligned-question-generator
                              │
                              └── Step 7: Create Final PDF
                                    │
                                    └── Use /test-pdf-generator skill
```

## Quick Start

```python
import sys
sys.path.append('.claude/skills/test-pdf-generator/scripts')
from test_pdf_generator import create_test_pdf

# Define test configuration
config = {
    'title': 'Year 10 Mathematics',
    'subtitle': 'AOS 7 Revision [10.2]',
    'version': 'Version B',
    'total_marks': 50,
    'time_allowed': '90 minutes',
    'instructions': [
        'Answer all questions',
        'Show all working',
        'Calculators permitted for Tech-Active questions'
    ],
    'sections': [
        {
            'name': 'Section A: Short Answer Questions',
            'marks': 34,
            'questions': [
                {
                    'number': 1,
                    'marks': 1,
                    'text': 'Find the surface area of a cube with side length 5 cm.',
                    'diagram': None,
                    'space': 4  # cm of working space
                },
                {
                    'number': 2,
                    'marks': 2,
                    'text': 'Find the shaded area in the diagram.',
                    'diagram': 'new_images/q2.png',
                    'space': 3
                }
            ]
        },
        {
            'name': 'Section B: Extended Response',
            'marks': 16,
            'questions': [
                {
                    'number': 17,
                    'marks': 7,
                    'text': 'A swimming pool has a trapezoidal cross-section...',
                    'diagram': 'new_images/q17.png',
                    'parts': [
                        {'label': 'a', 'text': 'Calculate the area...', 'marks': 1, 'space': 3},
                        {'label': 'b', 'text': 'Find the volume...', 'marks': 2, 'space': 4}
                    ]
                }
            ]
        }
    ],
    'output_path': 'Test_Version_B.pdf'
}

create_test_pdf(config)
```

## Configuration Reference

### Top-Level Config

| Key | Type | Required | Description |
|-----|------|----------|-------------|
| `title` | string | Yes | Main test title |
| `subtitle` | string | No | Subtitle (e.g., topic/unit) |
| `version` | string | No | Version identifier |
| `total_marks` | int | Yes | Total marks for the test |
| `time_allowed` | string | Yes | Time limit (e.g., '90 minutes') |
| `instructions` | list | No | List of instruction strings |
| `sections` | list | Yes | List of section configs |
| `output_path` | string | Yes | Output PDF filename |
| `student_name_field` | bool | No | Include name field (default: True) |

### Section Config

| Key | Type | Required | Description |
|-----|------|----------|-------------|
| `name` | string | Yes | Section header text |
| `marks` | int | No | Total marks for section |
| `questions` | list | Yes | List of question configs |
| `new_page` | bool | No | Start section on new page (default: True) |

### Question Config

| Key | Type | Required | Description |
|-----|------|----------|-------------|
| `number` | int | Yes | Question number |
| `marks` | int | Yes | Marks for this question |
| `text` | string | Yes | Question text (supports HTML: `<b>`, `<i>`, `<br/>`) |
| `table` | dict | No | Data table config (see Table Config below) |
| `diagram` | string | No | Path to diagram image |
| `space` | float | No | Working space in cm (default: 4) |
| `new_page` | bool | No | Start question on new page |
| `tech_active` | bool | No | Mark as calculator question |
| `parts` | list | No | For multi-part questions |

### Table Config (for data tables in questions)

| Key | Type | Required | Description |
|-----|------|----------|-------------|
| `headers` | list | Yes | Column headers (e.g., `['x', 'y', 'z']`) |
| `rows` | list | Yes | List of row data (e.g., `[['1', '2', '3'], ['4', '5', '6']]`) |
| `col_widths` | list | No | Column widths in cm (auto-calculated if not provided) |

### Multi-Part Question

| Key | Type | Required | Description |
|-----|------|----------|-------------|
| `label` | string | Yes | Part label (a, b, c, i, ii) |
| `text` | string | Yes | Part question text |
| `marks` | int | Yes | Marks for this part |
| `space` | float | No | Working space in cm |
| `diagram` | string | No | Diagram for this part only |

## Examples

### Simple Test (No Sections)

```python
config = {
    'title': 'Quick Quiz',
    'total_marks': 10,
    'time_allowed': '15 minutes',
    'sections': [{
        'name': 'Questions',
        'questions': [
            {'number': 1, 'marks': 2, 'text': 'What is 2 + 2?', 'space': 2},
            {'number': 2, 'marks': 3, 'text': 'Solve x + 5 = 12', 'space': 3},
            {'number': 3, 'marks': 5, 'text': 'Find the area of a circle with radius 7 cm.', 'space': 5}
        ]
    }],
    'output_path': 'quick_quiz.pdf'
}
```

### Test with Diagrams

```python
config = {
    'title': 'Geometry Test',
    'subtitle': 'Circles and Segments',
    'total_marks': 20,
    'time_allowed': '30 minutes',
    'sections': [{
        'name': 'Questions',
        'questions': [
            {
                'number': 1,
                'marks': 3,
                'text': 'Find the area of the shaded segment.',
                'diagram': 'new_images/segment.png',
                'space': 4
            },
            {
                'number': 2,
                'marks': 4,
                'text': 'In the diagram, find the value of x.',
                'diagram': 'new_images/circle_theorem.png',
                'tech_active': True,
                'space': 5
            }
        ]
    }],
    'output_path': 'geometry_test.pdf'
}
```

### Question with Data Table

```python
{
    'number': 5,
    'marks': 3,
    'text': 'The two-way table shows the preferred sport for Year 10 students.',
    'table': {
        'headers': ['', 'Basketball', 'Soccer', 'Total'],
        'rows': [
            ['Boys', '18', '12', '30'],
            ['Girls', '15', '10', '25'],
            ['Total', '33', '22', '55']
        ],
        'col_widths': [2.5, 2.5, 2.5, 2]  # in cm
    },
    'parts': [
        {'label': 'a', 'text': 'How many girls prefer basketball?', 'marks': 1, 'space': 2},
        {'label': 'b', 'text': 'What is the probability a random student is a girl who prefers soccer?', 'marks': 2, 'space': 3}
    ]
}
```

### Question with Bivariate Data Table

```python
{
    'number': 12,
    'marks': 4,
    'text': 'The table shows hours studied and test scores.',
    'table': {
        'headers': ['Hours Studied (x)', '1', '2', '4', '5', '6'],
        'rows': [
            ['Test Score (y)', '55', '60', '75', '80', '95']
        ]
    },
    'tech_active': True,
    'parts': [
        {'label': 'a', 'text': 'Describe the correlation.', 'marks': 1, 'space': 2},
        {'label': 'b', 'text': 'Find the equation of the line of best fit.', 'marks': 2, 'space': 4},
        {'label': 'c', 'text': 'Predict the score for 3 hours of study.', 'marks': 1, 'space': 2}
    ]
}
```

### Multi-Part Extended Response

```python
{
    'number': 15,
    'marks': 8,
    'text': 'A water tank consists of a cylinder with a hemisphere on top.',
    'diagram': 'new_images/tank.png',
    'parts': [
        {
            'label': 'a',
            'text': 'Find the volume of the cylinder.',
            'marks': 2,
            'space': 4
        },
        {
            'label': 'b',
            'text': 'Find the volume of the hemisphere.',
            'marks': 2,
            'space': 4
        },
        {
            'label': 'c',
            'text': 'Hence find the total volume of the tank.',
            'marks': 1,
            'space': 3
        },
        {
            'label': 'd',
            'text': 'Find the total surface area to be painted.',
            'marks': 3,
            'space': 5
        }
    ]
}
```

## CLI Usage

```bash
# Generate PDF from JSON config file
python3 .claude/skills/test-pdf-generator/scripts/test_pdf_generator.py \
    --config test_config.json

# Generate PDF with inline JSON
python3 .claude/skills/test-pdf-generator/scripts/test_pdf_generator.py \
    --config '{"title": "Quick Test", ...}'
```

## Integration with Question Generator

The `curriculum-aligned-question-generator` agent should:

1. **Generate all questions** and diagrams first
2. **Build the config dict** with all question data
3. **Call the skill** to create the PDF

Example in agent workflow:

```python
# After generating questions and diagrams...

import sys
sys.path.append('.claude/skills/test-pdf-generator/scripts')
from test_pdf_generator import create_test_pdf

config = {
    'title': 'Year 10 Mathematics',
    'subtitle': f'AOS {aos_number} Revision [{revision}]',
    'version': 'Version B',
    'total_marks': total_marks,
    'time_allowed': '90 minutes',
    'instructions': [
        'Answer all questions',
        'Show all working',
        'Calculators permitted for Tech-Active questions'
    ],
    'sections': sections_list,  # Built from generated questions
    'output_path': f'{test_name}_Version_B.pdf'
}

create_test_pdf(config)
print(f"✓ PDF created: {config['output_path']}")
```

## File Structure

```
.claude/skills/test-pdf-generator/
├── SKILL.md                           # This file
└── scripts/
    └── test_pdf_generator.py          # Main PDF generation script
```

## Dependencies

Required Python packages:
- `reportlab` - PDF generation
- `Pillow` (PIL) - Image handling for diagrams

## Quality Standards

Generated PDFs follow these standards:
- **Page size**: A4
- **Margins**: 2cm all sides
- **Font**: Helvetica family
- **Question numbers**: Bold with mark allocation
- **Diagrams**: Aspect ratio preserved, max 10cm width
- **Working space**: Clearly defined areas for answers
