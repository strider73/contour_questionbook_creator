"""
Geometry Diagram Generator

A flexible, extensible diagram generation system for mathematical test questions.
Diagrams are organized by CATEGORY (not by specific curriculum topic) so they can
be used across different Areas of Study (AOS).

USAGE:
    1. Import the module and call functions directly
    2. Run as CLI with JSON configuration
    3. Add new diagram types by creating new functions following the pattern

EXTENDING:
    To add a new diagram type:
    1. Create a function following the naming pattern: create_[category]_[type]()
    2. Add it to DIAGRAM_REGISTRY at the bottom of this file
    3. Document parameters and usage

All diagrams follow quality standards:
- ax.set_aspect('equal') for geometric shapes
- 150 DPI for print quality
- White background
- Clear labels with appropriate font sizes
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from matplotlib.patches import Arc, Wedge
import os
import json
import argparse

# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

def ensure_output_dir(path='new_images'):
    """Create output directory if it doesn't exist."""
    dir_path = os.path.dirname(path) if os.path.dirname(path) else 'new_images'
    os.makedirs(dir_path, exist_ok=True)


def setup_axes(ax, xlim, ylim, title=None):
    """Standard axis setup for all diagrams."""
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_aspect('equal')
    ax.axis('off')
    if title:
        ax.set_title(title, fontsize=11, pad=10, fontweight='bold')


def save_diagram(fig, output_path):
    """Save diagram with standard settings."""
    ensure_output_dir(output_path)
    plt.savefig(output_path, bbox_inches='tight', facecolor='white', dpi=150)
    plt.close()
    print(f"✓ Created: {output_path}")


# =============================================================================
# CATEGORY: CIRCLES
# =============================================================================

def create_circle_inscribed(config):
    """
    Circle with inscribed shape OR shape with inscribed circle.

    Config:
        outer_shape: 'circle' or 'square'
        inner_shape: 'circle' or 'square'
        dimension: The given dimension (radius if outer is circle, side if square)
        dimension_label: Label text (e.g., '9 cm')
        shaded: 'corners' or 'segment' - what is shaded
        output_path: Where to save
        title: Optional title
    """
    fig, ax = plt.subplots(figsize=(5, 5), dpi=150)

    outer = config.get('outer_shape', 'square')
    inner = config.get('inner_shape', 'circle')
    dim = config.get('dimension', 10)
    dim_label = config.get('dimension_label', f'{dim} cm')
    output_path = config.get('output_path', 'new_images/inscribed.png')
    title = config.get('title', f'{outer.title()} with inscribed {inner}')

    if outer == 'square' and inner == 'circle':
        # Square with inscribed circle
        square = patches.Rectangle((0, 0), dim, dim, fill=True,
                                   facecolor='lightgray', edgecolor='black', linewidth=2)
        ax.add_patch(square)

        radius = dim / 2
        circle = plt.Circle((dim/2, dim/2), radius, fill=True,
                            facecolor='white', edgecolor='black', linewidth=2)
        ax.add_patch(circle)

        ax.text(dim/2, -0.8, dim_label, ha='center', fontsize=11)
        margin = dim * 0.15
        setup_axes(ax, (-margin, dim + margin), (-margin - 1, dim + margin), title)

    elif outer == 'circle' and inner == 'square':
        # Circle with inscribed square
        radius = dim
        circle = plt.Circle((0, 0), radius, fill=True,
                           facecolor='lightgray', edgecolor='black', linewidth=2)
        ax.add_patch(circle)

        # Inscribed square: diagonal = diameter, side = diameter/sqrt(2)
        square_side = radius * np.sqrt(2)
        half_side = square_side / 2
        square = plt.Polygon([(-half_side, -half_side), (half_side, -half_side),
                             (half_side, half_side), (-half_side, half_side)],
                            fill=True, facecolor='white', edgecolor='black', linewidth=2)
        ax.add_patch(square)

        ax.plot([0, radius], [0, 0], 'k--', linewidth=1)
        ax.plot(0, 0, 'ko', markersize=4)
        ax.text(radius/2, -0.8, dim_label, fontsize=11, ha='center')
        ax.text(0.3, 0.3, 'O', fontsize=10)

        margin = radius * 0.2
        setup_axes(ax, (-radius - margin, radius + margin),
                  (-radius - margin, radius + margin), title)

    save_diagram(fig, output_path)


def create_circle_segment(config):
    """
    Circle with segment (sector minus triangle).

    Config:
        radius: Circle radius
        angle: Central angle in degrees
        radius_label: Label for radius (e.g., 'r = 8 cm')
        output_path: Where to save
        title: Optional title
    """
    fig, ax = plt.subplots(figsize=(5, 5), dpi=150)

    radius = config.get('radius', 8)
    angle_deg = config.get('angle', 90)
    radius_label = config.get('radius_label', f'r = {radius} cm')
    output_path = config.get('output_path', 'new_images/segment.png')
    title = config.get('title', 'Minor segment (shaded)')

    # Circle
    circle = plt.Circle((0, 0), radius, fill=False, edgecolor='black', linewidth=2)
    ax.add_patch(circle)
    ax.plot(0, 0, 'ko', markersize=4)
    ax.text(0.3, 0.3, 'O', fontsize=10)

    # Segment positioning
    start_angle = 90 - angle_deg/2
    end_angle = 90 + angle_deg/2

    # Shaded sector
    wedge = Wedge((0, 0), radius, start_angle, end_angle,
                  facecolor='lightblue', edgecolor='blue', linewidth=2, alpha=0.5)
    ax.add_patch(wedge)

    # Chord endpoints and radii
    x1 = radius * np.cos(np.radians(start_angle))
    y1 = radius * np.sin(np.radians(start_angle))
    x2 = radius * np.cos(np.radians(end_angle))
    y2 = radius * np.sin(np.radians(end_angle))

    ax.plot([0, x1], [0, y1], 'k-', linewidth=1.5)
    ax.plot([0, x2], [0, y2], 'k-', linewidth=1.5)
    ax.plot([x1, x2], [y1, y2], 'k-', linewidth=2)

    # Labels
    ax.plot([0, radius], [0, 0], 'k--', linewidth=1, alpha=0.5)
    ax.text(radius/2, -1, radius_label, fontsize=11, ha='center')

    arc_angle = Arc((0, 0), 2.5, 2.5, angle=0, theta1=start_angle, theta2=end_angle,
                    color='red', linewidth=1.5)
    ax.add_patch(arc_angle)
    ax.text(0, 2, f'{angle_deg}°', fontsize=11, color='red', ha='center')

    margin = radius * 0.25
    setup_axes(ax, (-radius - margin, radius + margin),
              (-radius - margin, radius + margin), title)
    save_diagram(fig, output_path)


def create_circle_theorem(config):
    """
    Circle theorem diagram (tangent-secant, two secants, chord perpendicular, etc.)

    Config:
        theorem_type: 'tangent_secant', 'two_secants', 'chord_perpendicular'
        segments: Dict of segment values (can include 'x' for unknown)
        output_path: Where to save
        title: Optional title
    """
    theorem_type = config.get('theorem_type', 'two_secants')
    segments = config.get('segments', {})
    output_path = config.get('output_path', 'new_images/circle_theorem.png')
    title = config.get('title', None)

    fig, ax = plt.subplots(figsize=(6, 5), dpi=150)

    if theorem_type == 'two_secants':
        # Two secants from external point
        pa = segments.get('pa', 3)
        ab = segments.get('ab', 5)
        pc = segments.get('pc', 'x')
        cd = segments.get('cd', 4)

        circle = plt.Circle((4, 3), 2.5, fill=False, edgecolor='black', linewidth=2)
        ax.add_patch(circle)
        ax.plot(4, 3, 'ko', markersize=4)
        ax.text(4.2, 3.2, 'O', fontsize=10)

        P = (0, 3)
        ax.plot(*P, 'ko', markersize=6)
        ax.text(-0.4, 3, 'P', fontsize=11, fontweight='bold')

        # First secant
        ax.plot([0, 7], [3, 3], 'b-', linewidth=1.5)
        ax.plot(1.5, 3, 'bo', markersize=5)
        ax.plot(6.5, 3, 'bo', markersize=5)
        ax.text(1.5, 2.5, 'A', fontsize=10, ha='center')
        ax.text(6.5, 2.5, 'B', fontsize=10, ha='center')

        # Second secant
        ax.plot([0, 5.2], [3, 5.6], 'r-', linewidth=1.5)
        ax.plot(2.1, 3.9, 'ro', markersize=5)
        ax.plot(5, 5.4, 'ro', markersize=5)
        ax.text(2.1-0.3, 3.9, 'C', fontsize=10)
        ax.text(5+0.2, 5.4, 'D', fontsize=10)

        # Labels
        ax.text(0.7, 2.4, f'{pa} cm', fontsize=10, color='blue', fontweight='bold')
        ax.text(4, 2.4, f'{ab} cm', fontsize=10, color='blue', fontweight='bold')
        ax.text(0.8, 3.6, f'{pc}', fontsize=11, color='red', fontweight='bold')
        ax.text(3.5, 4.8, f'{cd} cm', fontsize=10, color='red', fontweight='bold')

        if not title:
            title = 'Two secants from external point P'
        setup_axes(ax, (-1, 8), (1, 6.5), title)

    elif theorem_type == 'chord_perpendicular':
        radius = segments.get('radius', 10)
        chord = segments.get('chord', 16)

        circle = plt.Circle((0, 0), radius, fill=False, edgecolor='black', linewidth=2)
        ax.add_patch(circle)
        ax.plot(0, 0, 'ko', markersize=5)
        ax.text(0.3, 0.3, 'O', fontsize=11, fontweight='bold')

        half_chord = chord / 2
        dist_to_chord = np.sqrt(radius**2 - half_chord**2) * 0.8
        chord_y = -dist_to_chord

        ax.plot([-half_chord, half_chord], [chord_y, chord_y], 'b-', linewidth=2)
        ax.plot(-half_chord, chord_y, 'bo', markersize=5)
        ax.plot(half_chord, chord_y, 'bo', markersize=5)
        ax.text(-half_chord-0.5, chord_y, 'A', fontsize=10)
        ax.text(half_chord+0.3, chord_y, 'B', fontsize=10)

        ax.plot(0, chord_y, 'ro', markersize=5)
        ax.text(0.3, chord_y-0.5, 'M', fontsize=10, color='red')
        ax.plot([0, 0], [0, chord_y], 'r--', linewidth=2)

        sq_size = 0.4
        square = patches.Rectangle((0, chord_y), sq_size, sq_size,
                                   fill=False, edgecolor='red', linewidth=1.5)
        ax.add_patch(square)

        ax.plot([0, -half_chord], [0, chord_y], 'k-', linewidth=1.5)
        ax.text(0, -radius-1, f'Chord = {chord} cm', fontsize=10, ha='center')
        ax.text(-half_chord/2-0.8, chord_y/2, f'r = {radius} cm', fontsize=10, rotation=45)

        if not title:
            title = 'Perpendicular from centre to chord'
        margin = radius * 0.3
        setup_axes(ax, (-radius - margin, radius + margin),
                  (-radius - margin - 1.5, radius + margin), title)

    save_diagram(fig, output_path)


# =============================================================================
# CATEGORY: 3D SOLIDS
# =============================================================================

def create_solid_similar(config):
    """
    Two similar 3D solids for comparison.

    Config:
        solid_type: 'cone', 'cylinder', 'pyramid', 'sphere'
        dim1: Dimensions of smaller solid (dict with relevant measurements)
        dim2: Dimensions of larger solid
        output_path: Where to save
        title: Optional title
    """
    solid_type = config.get('solid_type', 'cone')
    dim1 = config.get('dim1', {'height': 4})
    dim2 = config.get('dim2', {'height': 6})
    output_path = config.get('output_path', 'new_images/similar_solids.png')
    title = config.get('title', f'Two similar {solid_type}s')

    fig, ax = plt.subplots(figsize=(7, 4), dpi=150)
    scale = 0.5

    if solid_type == 'cone':
        h1 = dim1.get('height', 4) * scale
        h2 = dim2.get('height', 6) * scale
        r1 = h1 * 0.3
        r2 = h2 * 0.3

        # Small cone
        ellipse1 = patches.Ellipse((2, 0.5), r1*2, 0.4, fill=True,
                                   facecolor='lightgray', edgecolor='black', linewidth=2)
        ax.add_patch(ellipse1)
        cone1 = plt.Polygon([(2-r1, 0.5), (2+r1, 0.5), (2, 0.5+h1)],
                           fill=True, facecolor='lightgray',
                           edgecolor='black', linewidth=2, alpha=0.7)
        ax.add_patch(cone1)
        ax.plot([2, 2], [0.5, 0.5+h1], 'k--', linewidth=1)
        ax.text(1.5, 0.5+h1/2, f'{dim1.get("height", 4)} cm', fontsize=10,
                rotation=90, va='center')

        # Large cone
        ellipse2 = patches.Ellipse((6, 0.5), r2*2, 0.6, fill=True,
                                   facecolor='lightgray', edgecolor='black', linewidth=2)
        ax.add_patch(ellipse2)
        cone2 = plt.Polygon([(6-r2, 0.5), (6+r2, 0.5), (6, 0.5+h2)],
                           fill=True, facecolor='lightgray',
                           edgecolor='black', linewidth=2, alpha=0.7)
        ax.add_patch(cone2)
        ax.plot([6, 6], [0.5, 0.5+h2], 'k--', linewidth=1)
        ax.text(5.5, 0.5+h2/2, f'{dim2.get("height", 6)} cm', fontsize=10,
                rotation=90, va='center')

        setup_axes(ax, (0, 8.5), (-0.5, max(h1, h2) + 1.5), title)

    elif solid_type == 'cylinder':
        h1 = dim1.get('height', 6) * scale
        r1 = dim1.get('radius', 3) * scale
        h2 = dim2.get('height', 9) * scale

        # Small cylinder
        ellipse1 = patches.Ellipse((2, 0.5), r1*2, 0.4, fill=True,
                                   facecolor='lightgray', edgecolor='black', linewidth=2)
        ax.add_patch(ellipse1)
        rect1 = patches.Rectangle((2-r1, 0.5), r1*2, h1, fill=True,
                                  facecolor='lightgray', edgecolor='black', linewidth=2)
        ax.add_patch(rect1)
        ellipse1_top = patches.Ellipse((2, 0.5+h1), r1*2, 0.4, fill=True,
                                       facecolor='gray', edgecolor='black', linewidth=2)
        ax.add_patch(ellipse1_top)
        ax.text(2, -0.3, f'r = {dim1.get("radius", 3)} cm', fontsize=9, ha='center')
        ax.text(0.8, 0.5+h1/2, f'{dim1.get("height", 6)} cm', fontsize=10,
                rotation=90, va='center')

        # Large cylinder
        ratio = dim2.get('height', 9) / dim1.get('height', 6)
        r2 = r1 * ratio
        ellipse2 = patches.Ellipse((6, 0.5), r2*2, 0.5, fill=True,
                                   facecolor='lightgray', edgecolor='black', linewidth=2)
        ax.add_patch(ellipse2)
        rect2 = patches.Rectangle((6-r2, 0.5), r2*2, h2, fill=True,
                                  facecolor='lightgray', edgecolor='black', linewidth=2)
        ax.add_patch(rect2)
        ellipse2_top = patches.Ellipse((6, 0.5+h2), r2*2, 0.5, fill=True,
                                       facecolor='gray', edgecolor='black', linewidth=2)
        ax.add_patch(ellipse2_top)
        ax.text(4.3, 0.5+h2/2, f'{dim2.get("height", 9)} cm', fontsize=10,
                rotation=90, va='center')

        setup_axes(ax, (0, 9), (-1, max(h1, h2) + 1.5), title)

    save_diagram(fig, output_path)


def create_solid_composite(config):
    """
    Composite 3D solid (e.g., cylinder + cone, cylinder + hemisphere).

    Config:
        components: List of component shapes with their dimensions
        output_path: Where to save
        title: Optional title
    """
    components = config.get('components', [
        {'type': 'cylinder', 'radius': 2.5, 'height': 18},
        {'type': 'cone', 'radius': 2.5, 'height': 5}
    ])
    output_path = config.get('output_path', 'new_images/composite_solid.png')
    title = config.get('title', 'Composite solid')

    fig, ax = plt.subplots(figsize=(5, 8), dpi=150)
    scale = 0.25

    y_offset = 1
    for comp in components:
        if comp['type'] == 'cylinder':
            r = comp['radius'] * scale
            h = comp['height'] * scale

            rect = patches.Rectangle((3-r, y_offset), r*2, h, fill=True,
                                     facecolor='lightgray', edgecolor='black', linewidth=2)
            ax.add_patch(rect)
            ellipse_top = patches.Ellipse((3, y_offset+h), r*2, 0.4, fill=True,
                                          facecolor='gray', edgecolor='black', linewidth=2)
            ax.add_patch(ellipse_top)
            ellipse_bot = patches.Ellipse((3, y_offset), r*2, 0.4, fill=True,
                                          facecolor='darkgray', edgecolor='black', linewidth=2)
            ax.add_patch(ellipse_bot)

            ax.annotate('', xy=(3+r+0.8, y_offset), xytext=(3+r+0.8, y_offset+h),
                        arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
            ax.text(3+r+1.1, y_offset+h/2, f'{comp["height"]} m', fontsize=10,
                    rotation=90, va='center')
            ax.plot([3, 3+r], [y_offset, y_offset], 'b-', linewidth=2)
            ax.text(3+r/2, y_offset-0.6, f'r = {comp["radius"]} m', fontsize=10,
                    ha='center', color='blue')

            y_offset += h

        elif comp['type'] == 'cone':
            r = comp['radius'] * scale
            h = comp['height'] * scale

            cone = plt.Polygon([(3-r, y_offset), (3+r, y_offset), (3, y_offset+h)],
                              fill=True, facecolor='red', edgecolor='darkred', linewidth=2)
            ax.add_patch(cone)

            ax.annotate('', xy=(3+r+0.8, y_offset), xytext=(3+r+0.8, y_offset+h),
                        arrowprops=dict(arrowstyle='<->', color='red', lw=1.5))
            ax.text(3+r+1.1, y_offset+h/2, f'{comp["height"]} m', fontsize=10,
                    rotation=90, va='center', color='red')

            y_offset += h

        elif comp['type'] == 'hemisphere':
            r = comp['radius'] * scale
            hemisphere = patches.Wedge((3, y_offset), r, 0, 180, fill=True,
                                       facecolor='lightblue', edgecolor='black', linewidth=2)
            ax.add_patch(hemisphere)
            y_offset += r

    setup_axes(ax, (0, 7), (-0.5, y_offset + 1), title)
    save_diagram(fig, output_path)


# =============================================================================
# CATEGORY: COMPOSITE AREAS
# =============================================================================

def create_area_composite(config):
    """
    Composite area diagram (annulus, shape with path, etc.)

    Config:
        shape_type: 'annulus', 'square_path', 'rectangle_semicircles'
        dimensions: Dict with relevant measurements
        labels: Dict with labels for regions
        output_path: Where to save
        title: Optional title
    """
    shape_type = config.get('shape_type', 'annulus')
    dimensions = config.get('dimensions', {})
    labels = config.get('labels', {})
    output_path = config.get('output_path', 'new_images/composite_area.png')
    title = config.get('title', None)

    fig, ax = plt.subplots(figsize=(5, 5), dpi=150)

    if shape_type == 'annulus':
        inner_r = dimensions.get('inner_radius', 4)
        outer_r = dimensions.get('outer_radius', 5.5)
        inner_label = labels.get('inner', 'Pool')
        outer_label = labels.get('outer', 'Path')

        outer = plt.Circle((0, 0), outer_r, fill=True,
                          facecolor='sandybrown', edgecolor='black', linewidth=2, alpha=0.6)
        ax.add_patch(outer)
        inner = plt.Circle((0, 0), inner_r, fill=True,
                          facecolor='deepskyblue', edgecolor='black', linewidth=2)
        ax.add_patch(inner)

        ax.plot(0, 0, 'ko', markersize=4)
        ax.plot([0, inner_r], [0, 0], 'k-', linewidth=1.5)
        ax.text(inner_r/2, 0.4, f'{inner_r} m', fontsize=10, ha='center')

        path_width = outer_r - inner_r
        ax.annotate('', xy=(inner_r, 0), xytext=(outer_r, 0),
                    arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
        ax.text((inner_r + outer_r)/2, -0.6, f'{path_width} m', fontsize=10, ha='center')

        ax.text(0, 0, inner_label, fontsize=10, ha='center', va='center', fontweight='bold')
        ax.text(0, -outer_r + 0.5, outer_label, fontsize=9, ha='center', color='brown')

        if not title:
            title = f'Circular {inner_label.lower()} with {outer_label.lower()}'
        margin = outer_r * 0.25
        setup_axes(ax, (-outer_r - margin, outer_r + margin),
                  (-outer_r - margin - 1, outer_r + margin), title)

    elif shape_type == 'square_path':
        inner_side = dimensions.get('inner_side', 8)
        path_width = dimensions.get('path_width', 1.5)
        inner_label = labels.get('inner', 'Garden')
        outer_label = labels.get('outer', 'Path')

        outer_side = inner_side + 2 * path_width
        outer = patches.Rectangle((0, 0), outer_side, outer_side,
                                  fill=True, facecolor='sandybrown',
                                  edgecolor='black', linewidth=2, alpha=0.6)
        ax.add_patch(outer)
        inner = patches.Rectangle((path_width, path_width), inner_side, inner_side,
                                  fill=True, facecolor='lightgreen',
                                  edgecolor='darkgreen', linewidth=2)
        ax.add_patch(inner)

        ax.annotate('', xy=(path_width, -0.5), xytext=(path_width + inner_side, -0.5),
                    arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
        ax.text(path_width + inner_side/2, -1.2, f'{inner_side} m', fontsize=11,
                ha='center', fontweight='bold')

        ax.annotate('', xy=(path_width + inner_side, path_width/2),
                    xytext=(outer_side, path_width/2),
                    arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
        ax.text(path_width + inner_side + path_width/2, path_width/2 - 0.5,
                f'{path_width} m', fontsize=10, ha='center')

        ax.text(path_width + inner_side/2, path_width + inner_side/2, inner_label,
                fontsize=11, ha='center', va='center', fontweight='bold', color='darkgreen')
        ax.text(path_width/2, outer_side/2, outer_label, fontsize=10, ha='center',
                va='center', rotation=90, color='brown')

        if not title:
            title = f'Square {inner_label.lower()} with {outer_label.lower()}'
        margin = outer_side * 0.1
        setup_axes(ax, (-margin, outer_side + margin),
                  (-margin - 1.5, outer_side + margin), title)

    save_diagram(fig, output_path)


# =============================================================================
# CATEGORY: PRISMS
# =============================================================================

def create_prism(config):
    """
    Prism diagram (triangular, rectangular, trapezoidal, hexagonal).

    Config:
        cross_section: 'triangle', 'rectangle', 'trapezoid', 'hexagon'
        dimensions: Dict with relevant measurements
        output_path: Where to save
        title: Optional title
    """
    cross_section = config.get('cross_section', 'triangle')
    dimensions = config.get('dimensions', {})
    output_path = config.get('output_path', 'new_images/prism.png')
    title = config.get('title', f'{cross_section.title()} prism')

    fig, ax = plt.subplots(figsize=(7, 5), dpi=150)
    scale = 0.3

    if cross_section == 'triangle':
        base = dimensions.get('base', 6) * scale
        height_tri = dimensions.get('height', 8) * scale
        length = dimensions.get('length', 15) * scale

        front = plt.Polygon([(1, 1), (1+base, 1), (1, 1+height_tri)],
                           fill=True, facecolor='lightcoral',
                           edgecolor='darkred', linewidth=2, alpha=0.7)
        ax.add_patch(front)

        offset = length * 0.5
        back = plt.Polygon([(1+offset, 1+offset*0.4), (1+base+offset, 1+offset*0.4),
                           (1+offset, 1+height_tri+offset*0.4)],
                          fill=True, facecolor='salmon',
                          edgecolor='darkred', linewidth=2, alpha=0.5)
        ax.add_patch(back)

        ax.plot([1, 1+offset], [1, 1+offset*0.4], 'darkred', linewidth=1.5)
        ax.plot([1+base, 1+base+offset], [1, 1+offset*0.4], 'darkred', linewidth=1.5)
        ax.plot([1, 1+offset], [1+height_tri, 1+height_tri+offset*0.4], 'darkred', linewidth=1.5)

        sq_size = 0.25
        square = patches.Rectangle((1, 1), sq_size, sq_size,
                                   fill=False, edgecolor='red', linewidth=1.5)
        ax.add_patch(square)

        ax.text(1+base/2, 0.5, f'{dimensions.get("base", 6)} cm', fontsize=10,
                ha='center', fontweight='bold')
        ax.text(0.3, 1+height_tri/2, f'{dimensions.get("height", 8)} cm', fontsize=10,
                rotation=90, va='center', fontweight='bold')
        ax.text(1+base+offset/2+0.3, 1+offset*0.2, f'{dimensions.get("length", 15)} cm',
                fontsize=10, rotation=20)

        setup_axes(ax, (-0.5, 1+base+offset+1), (-0.5, 1+height_tri+offset*0.4+1), title)

    elif cross_section == 'trapezoid':
        # Swimming pool style
        shallow = dimensions.get('shallow', 0.9)
        deep = dimensions.get('deep', 1.8)
        length = dimensions.get('length', 30)
        width = dimensions.get('width', 12)

        trapezoid = plt.Polygon([(1, 2), (1, 2+shallow), (6, 2+deep), (6, 2)],
                               fill=True, facecolor='lightblue',
                               edgecolor='blue', linewidth=2, alpha=0.6)
        ax.add_patch(trapezoid)

        water = plt.Polygon([(1, 2), (1, 2+shallow*0.9), (6, 2+deep*0.9), (6, 2)],
                           fill=True, facecolor='cyan',
                           edgecolor='darkblue', linewidth=1, alpha=0.7)
        ax.add_patch(water)

        ax.plot([0, 7], [2, 2], 'brown', linewidth=3)

        ax.plot([0.7, 0.7], [2, 2+shallow], 'r-', linewidth=2)
        ax.text(0.2, 2+shallow/2, f'{shallow} m', fontsize=10, rotation=90,
                va='center', color='red', fontweight='bold')

        ax.plot([6.3, 6.3], [2, 2+deep], 'r-', linewidth=2)
        ax.text(6.8, 2+deep/2, f'{deep} m', fontsize=10, rotation=90,
                va='center', color='red', fontweight='bold')

        ax.annotate('', xy=(1, 1.5), xytext=(6, 1.5),
                    arrowprops=dict(arrowstyle='<->', color='black', lw=2))
        ax.text(3.5, 1, f'{length} m', fontsize=11, ha='center', fontweight='bold')

        ax.text(3.5, 2+max(shallow, deep)+0.8, f'Width: {width} m', fontsize=11,
                ha='center', fontweight='bold',
                bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.8))

        if not title:
            title = 'Swimming pool (side view)'
        setup_axes(ax, (-0.5, 7.5), (0.5, 2+max(shallow, deep)+1.5), title)

    save_diagram(fig, output_path)


# =============================================================================
# DIAGRAM REGISTRY - Maps diagram types to functions
# =============================================================================

DIAGRAM_REGISTRY = {
    # Circle diagrams
    'circle_inscribed': create_circle_inscribed,
    'circle_segment': create_circle_segment,
    'circle_theorem': create_circle_theorem,

    # 3D Solids
    'solid_similar': create_solid_similar,
    'solid_composite': create_solid_composite,

    # Composite areas
    'area_composite': create_area_composite,

    # Prisms
    'prism': create_prism,
}


def generate_diagram(diagram_type, config):
    """
    Generate a diagram by type.

    Args:
        diagram_type: Key from DIAGRAM_REGISTRY
        config: Configuration dict for the diagram
    """
    if diagram_type not in DIAGRAM_REGISTRY:
        raise ValueError(f"Unknown diagram type: {diagram_type}. "
                        f"Available: {list(DIAGRAM_REGISTRY.keys())}")

    DIAGRAM_REGISTRY[diagram_type](config)


# =============================================================================
# CLI INTERFACE
# =============================================================================

def main():
    parser = argparse.ArgumentParser(description='Generate geometry diagrams')
    parser.add_argument('--type', '-t', required=True,
                       choices=list(DIAGRAM_REGISTRY.keys()),
                       help='Type of diagram to generate')
    parser.add_argument('--config', '-c', type=str,
                       help='JSON configuration string or path to JSON file')
    parser.add_argument('--output', '-o', type=str,
                       help='Output path (overrides config)')

    args = parser.parse_args()

    # Parse config
    config = {}
    if args.config:
        if os.path.exists(args.config):
            with open(args.config) as f:
                config = json.load(f)
        else:
            config = json.loads(args.config)

    if args.output:
        config['output_path'] = args.output

    generate_diagram(args.type, config)


if __name__ == "__main__":
    # If run without arguments, generate example diagrams
    import sys
    if len(sys.argv) == 1:
        print("\n" + "="*60)
        print("GEOMETRY DIAGRAM GENERATOR - EXAMPLES")
        print("="*60 + "\n")

        # Example: Circle with inscribed square
        generate_diagram('circle_inscribed', {
            'outer_shape': 'circle',
            'inner_shape': 'square',
            'dimension': 9,
            'output_path': 'new_images/example_circle_inscribed_square.png'
        })

        # Example: Minor segment
        generate_diagram('circle_segment', {
            'radius': 8,
            'angle': 120,
            'output_path': 'new_images/example_segment.png'
        })

        # Example: Two secants
        generate_diagram('circle_theorem', {
            'theorem_type': 'two_secants',
            'segments': {'pa': 3, 'ab': 5, 'pc': 'x', 'cd': 4},
            'output_path': 'new_images/example_two_secants.png'
        })

        # Example: Similar cones
        generate_diagram('solid_similar', {
            'solid_type': 'cone',
            'dim1': {'height': 4},
            'dim2': {'height': 6},
            'output_path': 'new_images/example_similar_cones.png'
        })

        # Example: Lighthouse
        generate_diagram('solid_composite', {
            'components': [
                {'type': 'cylinder', 'radius': 2.5, 'height': 18},
                {'type': 'cone', 'radius': 2.5, 'height': 5}
            ],
            'title': 'Lighthouse',
            'output_path': 'new_images/example_lighthouse.png'
        })

        # Example: Annulus
        generate_diagram('area_composite', {
            'shape_type': 'annulus',
            'dimensions': {'inner_radius': 4, 'outer_radius': 5.5},
            'output_path': 'new_images/example_annulus.png'
        })

        # Example: Trapezoidal pool
        generate_diagram('prism', {
            'cross_section': 'trapezoid',
            'dimensions': {'shallow': 0.9, 'deep': 1.8, 'length': 30, 'width': 12},
            'output_path': 'new_images/example_pool.png'
        })

        print("\n" + "="*60)
        print("EXAMPLES GENERATED - see new_images/ folder")
        print("="*60 + "\n")
    else:
        main()
