#!/usr/bin/env python3
"""
Test PDF Generator

Creates professional test/exam PDFs with questions, diagrams, and working space.
Configuration-driven design for flexibility and maintainability.

Usage:
    # As a module
    from test_pdf_generator import create_test_pdf
    create_test_pdf(config)

    # From command line
    python3 test_pdf_generator.py --config test_config.json
"""

import json
import os
import sys
import argparse
from pathlib import Path

try:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import cm
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, Image,
        Table, TableStyle, PageBreak, KeepTogether
    )
    from reportlab.lib import colors
    from PIL import Image as PILImage
except ImportError as e:
    print(f"Missing dependency: {e}")
    print("Install with: pip3 install reportlab Pillow")
    sys.exit(1)


# Page setup
PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 2 * cm
CONTENT_WIDTH = PAGE_WIDTH - 2 * MARGIN
MAX_IMAGE_WIDTH = 10 * cm
MAX_IMAGE_HEIGHT = 8 * cm


def get_styles():
    """Create and return custom paragraph styles."""
    styles = getSampleStyleSheet()

    # Title style
    styles.add(ParagraphStyle(
        name='TestTitle',
        parent=styles['Heading1'],
        fontSize=18,
        alignment=TA_CENTER,
        spaceAfter=6
    ))

    # Subtitle style
    styles.add(ParagraphStyle(
        name='TestSubtitle',
        parent=styles['Heading2'],
        fontSize=14,
        alignment=TA_CENTER,
        spaceAfter=12
    ))

    # Version style
    styles.add(ParagraphStyle(
        name='TestVersion',
        parent=styles['Normal'],
        fontSize=12,
        alignment=TA_CENTER,
        spaceAfter=20
    ))

    # Section header style
    styles.add(ParagraphStyle(
        name='SectionHeader',
        parent=styles['Heading2'],
        fontSize=12,
        spaceBefore=12,
        spaceAfter=8,
        textColor=colors.black
    ))

    # Question number style
    styles.add(ParagraphStyle(
        name='QuestionNumber',
        parent=styles['Normal'],
        fontSize=11,
        fontName='Helvetica-Bold',
        spaceBefore=10,
        spaceAfter=4
    ))

    # Question text style
    styles.add(ParagraphStyle(
        name='QuestionText',
        parent=styles['Normal'],
        fontSize=11,
        spaceBefore=0,
        spaceAfter=6,
        leading=14
    ))

    # Part label style (a), (b), etc.
    styles.add(ParagraphStyle(
        name='PartLabel',
        parent=styles['Normal'],
        fontSize=11,
        fontName='Helvetica-Bold',
        leftIndent=20,
        spaceBefore=6,
        spaceAfter=2
    ))

    # Part text style
    styles.add(ParagraphStyle(
        name='PartText',
        parent=styles['Normal'],
        fontSize=11,
        leftIndent=40,
        spaceBefore=0,
        spaceAfter=4
    ))

    # Instruction style
    styles.add(ParagraphStyle(
        name='Instruction',
        parent=styles['Normal'],
        fontSize=10,
        leftIndent=20,
        spaceBefore=2,
        spaceAfter=2
    ))

    # Info style (time, marks)
    styles.add(ParagraphStyle(
        name='TestInfo',
        parent=styles['Normal'],
        fontSize=11,
        alignment=TA_CENTER,
        spaceBefore=4,
        spaceAfter=4
    ))

    return styles


def create_data_table(table_config):
    """
    Create a formatted data table for questions.

    Args:
        table_config: Dictionary with table configuration:
            {
                'headers': ['Col1', 'Col2', ...],
                'rows': [['val1', 'val2', ...], ...],
                'col_widths': [width1, width2, ...] (optional, in cm)
            }

    Returns:
        ReportLab Table object
    """
    headers = table_config.get('headers', [])
    rows = table_config.get('rows', [])
    col_widths = table_config.get('col_widths', None)

    # Build table data with headers
    table_data = []
    if headers:
        table_data.append(headers)
    table_data.extend(rows)

    # Calculate column widths if not provided
    if col_widths:
        col_widths = [w * cm for w in col_widths]
    else:
        # Auto-calculate based on content width
        num_cols = len(headers) if headers else (len(rows[0]) if rows else 1)
        col_width = min(CONTENT_WIDTH / num_cols, 3 * cm)
        col_widths = [col_width] * num_cols

    # Create table
    table = Table(table_data, colWidths=col_widths)

    # Style the table
    style_commands = [
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Bold headers
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.Color(0.9, 0.9, 0.9)),  # Light gray header
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
    ]

    table.setStyle(TableStyle(style_commands))
    return table


def get_image_with_aspect_ratio(image_path, max_width=MAX_IMAGE_WIDTH, max_height=MAX_IMAGE_HEIGHT):
    """
    Load an image and return a ReportLab Image object with preserved aspect ratio.

    Args:
        image_path: Path to the image file
        max_width: Maximum width in points
        max_height: Maximum height in points

    Returns:
        ReportLab Image object or None if image not found
    """
    if not image_path or not os.path.exists(image_path):
        return None

    try:
        with PILImage.open(image_path) as img:
            img_width, img_height = img.size

        # Calculate scaling to fit within max dimensions
        width_ratio = max_width / img_width
        height_ratio = max_height / img_height
        scale = min(width_ratio, height_ratio, 1.0)  # Don't upscale

        final_width = img_width * scale
        final_height = img_height * scale

        return Image(image_path, width=final_width, height=final_height)
    except Exception as e:
        print(f"Warning: Could not load image {image_path}: {e}")
        return None


def create_working_space(height_cm):
    """
    Create a working space area for student answers.

    Args:
        height_cm: Height of working space in centimeters

    Returns:
        List of flowables representing the working space
    """
    height = height_cm * cm

    # Create a table with dotted lines for working space
    data = [['']]
    table = Table(data, colWidths=[CONTENT_WIDTH], rowHeights=[height])
    table.setStyle(TableStyle([
        ('BOX', (0, 0), (-1, -1), 0.5, colors.lightgrey),
        ('LINEBELOW', (0, 0), (-1, -1), 0.25, colors.lightgrey),
    ]))

    return [Spacer(1, 4), table, Spacer(1, 6)]


def create_title_page(config, styles):
    """
    Create the title page elements.

    Args:
        config: Test configuration dictionary
        styles: Paragraph styles

    Returns:
        List of flowables for the title page
    """
    elements = []

    # Title
    elements.append(Paragraph(config.get('title', 'Test'), styles['TestTitle']))

    # Subtitle
    if config.get('subtitle'):
        elements.append(Paragraph(config['subtitle'], styles['TestSubtitle']))

    # Version
    if config.get('version'):
        elements.append(Paragraph(config['version'], styles['TestVersion']))

    elements.append(Spacer(1, 20))

    # Student name field
    if config.get('student_name_field', True):
        name_table = Table(
            [['Name:', '_' * 40]],
            colWidths=[2*cm, 10*cm]
        )
        name_table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 11),
            ('ALIGN', (0, 0), (0, 0), 'RIGHT'),
            ('VALIGN', (0, 0), (-1, -1), 'BOTTOM'),
        ]))
        elements.append(name_table)
        elements.append(Spacer(1, 15))

    # Test info (time and marks)
    info_text = []
    if config.get('time_allowed'):
        info_text.append(f"Time Allowed: {config['time_allowed']}")
    if config.get('total_marks'):
        info_text.append(f"Total Marks: {config['total_marks']}")

    if info_text:
        elements.append(Paragraph(' | '.join(info_text), styles['TestInfo']))
        elements.append(Spacer(1, 15))

    # Instructions
    if config.get('instructions'):
        elements.append(Paragraph('<b>Instructions:</b>', styles['Normal']))
        for instruction in config['instructions']:
            elements.append(Paragraph(f"• {instruction}", styles['Instruction']))
        elements.append(Spacer(1, 10))

    elements.append(Spacer(1, 20))

    return elements


def create_question(question, styles):
    """
    Create elements for a single question.

    Args:
        question: Question configuration dictionary
        styles: Paragraph styles

    Returns:
        List of flowables for the question
    """
    elements = []

    # Question number and marks
    q_num = question['number']
    marks = question['marks']
    mark_text = f"[{marks} mark{'s' if marks != 1 else ''}]"

    # Tech-active indicator
    tech_indicator = " (Tech-Active)" if question.get('tech_active') else ""

    elements.append(Paragraph(
        f"<b>Question {q_num}</b> {mark_text}{tech_indicator}",
        styles['QuestionNumber']
    ))

    # Question text
    if question.get('text'):
        elements.append(Paragraph(question['text'], styles['QuestionText']))

    # Data table (if any) - rendered BEFORE diagram
    if question.get('table'):
        table = create_data_table(question['table'])
        elements.append(Spacer(1, 6))
        elements.append(table)
        elements.append(Spacer(1, 6))

    # Diagram (if any)
    if question.get('diagram'):
        img = get_image_with_aspect_ratio(question['diagram'])
        if img:
            elements.append(Spacer(1, 6))
            elements.append(img)
            elements.append(Spacer(1, 6))

    # Multi-part questions
    if question.get('parts'):
        for part in question['parts']:
            part_label = part['label']
            part_marks = part['marks']
            part_mark_text = f"[{part_marks} mark{'s' if part_marks != 1 else ''}]"

            elements.append(Paragraph(
                f"<b>({part_label})</b> {part_mark_text}",
                styles['PartLabel']
            ))
            elements.append(Paragraph(part['text'], styles['PartText']))

            # Part diagram (if any)
            if part.get('diagram'):
                img = get_image_with_aspect_ratio(part['diagram'])
                if img:
                    elements.append(Spacer(1, 4))
                    elements.append(img)
                    elements.append(Spacer(1, 4))

            # Working space for part
            part_space = part.get('space', 3)
            elements.extend(create_working_space(part_space))
    else:
        # Working space for simple question
        space = question.get('space', 4)
        elements.extend(create_working_space(space))

    return elements


def create_section(section, styles):
    """
    Create elements for a section.

    Args:
        section: Section configuration dictionary
        styles: Paragraph styles

    Returns:
        List of flowables for the section
    """
    elements = []

    # Section header
    section_name = section.get('name', '')
    section_marks = section.get('marks')

    if section_marks:
        header_text = f"<b>{section_name}</b> ({section_marks} marks)"
    else:
        header_text = f"<b>{section_name}</b>"

    elements.append(Paragraph(header_text, styles['SectionHeader']))
    elements.append(Spacer(1, 6))

    # Questions
    for i, question in enumerate(section.get('questions', [])):
        # New page before question if specified
        if question.get('new_page') and i > 0:
            elements.append(PageBreak())

        q_elements = create_question(question, styles)

        # Try to keep question together on one page (if not too long)
        if len(q_elements) <= 8:  # Simple heuristic
            elements.append(KeepTogether(q_elements))
        else:
            elements.extend(q_elements)

    return elements


def create_test_pdf(config):
    """
    Generate a test PDF from the given configuration.

    Args:
        config: Test configuration dictionary with structure:
            {
                'title': str,
                'subtitle': str (optional),
                'version': str (optional),
                'total_marks': int,
                'time_allowed': str,
                'instructions': list[str] (optional),
                'student_name_field': bool (optional, default True),
                'sections': list[section_config],
                'output_path': str
            }

    Returns:
        Path to the generated PDF file
    """
    output_path = config.get('output_path', 'test_output.pdf')

    # Ensure output directory exists
    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    # Create document
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=MARGIN,
        bottomMargin=MARGIN
    )

    styles = get_styles()
    elements = []

    # Title page
    elements.extend(create_title_page(config, styles))

    # Sections
    for i, section in enumerate(config.get('sections', [])):
        # New page before section (except first)
        if i > 0 and section.get('new_page', True):
            elements.append(PageBreak())

        elements.extend(create_section(section, styles))

    # Build PDF
    doc.build(elements)

    print(f"✓ PDF created: {output_path}")
    return output_path


def main():
    """Command-line interface for test PDF generation."""
    parser = argparse.ArgumentParser(
        description='Generate test PDFs from configuration'
    )
    parser.add_argument(
        '--config', '-c',
        required=True,
        help='Path to JSON config file or inline JSON string'
    )
    parser.add_argument(
        '--output', '-o',
        help='Override output path'
    )

    args = parser.parse_args()

    # Load config
    if os.path.isfile(args.config):
        with open(args.config, 'r') as f:
            config = json.load(f)
    else:
        # Try parsing as inline JSON
        try:
            config = json.loads(args.config)
        except json.JSONDecodeError:
            print(f"Error: Could not parse config. Provide a valid JSON file or JSON string.")
            sys.exit(1)

    # Override output path if specified
    if args.output:
        config['output_path'] = args.output

    # Generate PDF
    create_test_pdf(config)


if __name__ == '__main__':
    # If run directly without args, generate a sample test
    if len(sys.argv) == 1:
        print("Generating sample test PDF...")

        sample_config = {
            'title': 'Year 10 Mathematics',
            'subtitle': 'Sample Test',
            'version': 'Version B',
            'total_marks': 15,
            'time_allowed': '30 minutes',
            'instructions': [
                'Answer all questions',
                'Show all working',
                'Calculators permitted'
            ],
            'sections': [
                {
                    'name': 'Section A: Short Answer',
                    'marks': 10,
                    'questions': [
                        {
                            'number': 1,
                            'marks': 2,
                            'text': 'Calculate the surface area of a cube with side length 4 cm.',
                            'space': 4
                        },
                        {
                            'number': 2,
                            'marks': 3,
                            'text': 'A cylinder has radius 5 cm and height 12 cm. Find its volume.',
                            'space': 5
                        },
                        {
                            'number': 3,
                            'marks': 5,
                            'text': 'A composite shape consists of a rectangle and semicircle.',
                            'parts': [
                                {'label': 'a', 'text': 'Find the area of the rectangle.', 'marks': 2, 'space': 3},
                                {'label': 'b', 'text': 'Find the area of the semicircle.', 'marks': 2, 'space': 3},
                                {'label': 'c', 'text': 'Hence find the total area.', 'marks': 1, 'space': 2}
                            ]
                        }
                    ]
                },
                {
                    'name': 'Section B: Extended Response',
                    'marks': 5,
                    'questions': [
                        {
                            'number': 4,
                            'marks': 5,
                            'text': 'A water tank is in the shape of a cylinder with a hemisphere on top. The cylinder has radius 2 m and height 3 m.',
                            'parts': [
                                {'label': 'a', 'text': 'Find the volume of the cylindrical part.', 'marks': 2, 'space': 4},
                                {'label': 'b', 'text': 'Find the volume of the hemispherical part.', 'marks': 2, 'space': 4},
                                {'label': 'c', 'text': 'Calculate the total capacity in litres.', 'marks': 1, 'space': 3}
                            ]
                        }
                    ]
                }
            ],
            'output_path': 'sample_test.pdf'
        }

        create_test_pdf(sample_config)
    else:
        main()
