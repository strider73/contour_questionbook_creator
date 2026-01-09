#!/usr/bin/env python3
"""
Polynomial Diagram Generator

Generates polynomial graphs for AOS 8 curriculum:
- Cubic graphs (factorised form for reading intercepts)
- Quartic graphs (turning point form)
- Blank grids for student sketching

Usage:
    python3 polynomial_diagrams.py

    # Generate specific diagram
    python3 polynomial_diagrams.py -t cubic_graph -c '{"x_intercepts": [-4, 2, 5]}' -o output.png
"""

import matplotlib.pyplot as plt
import numpy as np
import json
import argparse
import os


def save_diagram(fig, output_path):
    """Save figure with proper settings."""
    os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else '.', exist_ok=True)
    fig.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close(fig)
    print(f"Saved: {output_path}")


def create_cubic_graph(config):
    """
    Create a cubic graph for reading intercepts.

    Config:
        x_intercepts: List of 3 x-intercept values [a, b, c] - REQUIRED
        leading_coef: Leading coefficient (default 1, use negative to flip)
        x_range: [min, max] for x-axis (auto-calculated if not provided)
        y_range: [min, max] for y-axis (auto-calculated if not provided)
        output_path: Where to save (default: new_images/cubic_graph.png)
        figsize: Tuple (width, height) in inches (default (8, 8))
        show_intercept_dots: Whether to mark intercepts with dots (default True)

    Returns:
        dict with x_intercepts and y_intercept values (for answer key)
    """
    x_ints = config.get('x_intercepts', [-4, 2, 5])
    a = config.get('leading_coef', 1)
    output_path = config.get('output_path', 'new_images/cubic_graph.png')
    figsize = config.get('figsize', (8, 8))
    show_dots = config.get('show_intercept_dots', True)

    # Calculate y-intercept: y = a(x - r1)(x - r2)(x - r3), at x=0
    y_int = a * (-x_ints[0]) * (-x_ints[1]) * (-x_ints[2])

    # Determine axis ranges
    x_min = min(x_ints) - 2
    x_max = max(x_ints) + 2
    if 'x_range' in config:
        x_min, x_max = config['x_range']

    # Generate curve
    x = np.linspace(x_min - 1, x_max + 1, 500)
    y = a * (x - x_ints[0]) * (x - x_ints[1]) * (x - x_ints[2])

    # Auto y-range based on curve values
    y_data_min, y_data_max = y.min(), y.max()
    y_padding = (y_data_max - y_data_min) * 0.1
    y_min = y_data_min - y_padding
    y_max = y_data_max + y_padding

    # Ensure y=0 is visible and y-intercept is visible
    y_min = min(y_min, min(0, y_int) - 5)
    y_max = max(y_max, max(0, y_int) + 5)

    if 'y_range' in config:
        y_min, y_max = config['y_range']

    # Create figure with square aspect
    fig, ax = plt.subplots(figsize=figsize)

    # Plot cubic curve
    ax.plot(x, y, 'b-', linewidth=2)

    # Draw axes
    ax.axhline(y=0, color='k', linewidth=1.2)
    ax.axvline(x=0, color='k', linewidth=1.2)

    # Grid
    ax.grid(True, linestyle='-', alpha=0.3, color='gray')

    # Set limits
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)

    # Mark intercepts with dots (students need to read the values)
    if show_dots:
        ax.plot(x_ints, [0, 0, 0], 'ko', markersize=6)
        ax.plot([0], [y_int], 'ko', markersize=6)

    # Axis labels
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)

    # Tick marks
    x_ticks = range(int(x_min), int(x_max) + 1)
    ax.set_xticks(x_ticks)

    # y-ticks with appropriate spacing
    y_range_size = y_max - y_min
    if y_range_size <= 30:
        y_tick_spacing = 5
    elif y_range_size <= 60:
        y_tick_spacing = 10
    else:
        y_tick_spacing = 20

    y_ticks = np.arange(
        int(y_min // y_tick_spacing) * y_tick_spacing,
        int(y_max // y_tick_spacing + 1) * y_tick_spacing + 1,
        y_tick_spacing
    )
    ax.set_yticks(y_ticks)

    plt.tight_layout()
    save_diagram(fig, output_path)

    return {'x_intercepts': x_ints, 'y_intercept': int(y_int) if y_int == int(y_int) else y_int}


def create_blank_grid(config):
    """
    Create a blank coordinate grid for student sketching.

    Config:
        x_range: [min, max] for x-axis (default [-5, 5])
        y_range: [min, max] for y-axis (default [-20, 20])
        x_tick_spacing: Spacing between x ticks (default 1)
        y_tick_spacing: Spacing between y ticks (default auto: 5 or 10)
        output_path: Where to save (default: new_images/blank_grid.png)
        figsize: Tuple (width, height) in inches (default (8, 8))
        title: Optional title for the grid
    """
    x_min, x_max = config.get('x_range', [-5, 5])
    y_min, y_max = config.get('y_range', [-20, 20])
    x_spacing = config.get('x_tick_spacing', 1)

    # Auto y-spacing based on range
    y_range_size = y_max - y_min
    default_y_spacing = 5 if y_range_size <= 50 else 10
    y_spacing = config.get('y_tick_spacing', default_y_spacing)

    output_path = config.get('output_path', 'new_images/blank_grid.png')
    figsize = config.get('figsize', (8, 8))
    title = config.get('title', None)

    fig, ax = plt.subplots(figsize=figsize)

    # Set limits with small padding
    ax.set_xlim(x_min - 0.5, x_max + 0.5)
    ax.set_ylim(y_min - 2, y_max + 2)

    # Grid lines (light gray like original test papers)
    ax.set_xticks(np.arange(x_min, x_max + 1, x_spacing))
    ax.set_yticks(np.arange(y_min, y_max + y_spacing, y_spacing))
    ax.grid(True, linestyle='-', alpha=0.4, color='lightgray', linewidth=0.8)

    # Axis lines (thicker black)
    ax.axhline(y=0, color='black', linewidth=1.5)
    ax.axvline(x=0, color='black', linewidth=1.5)

    # Arrow heads at axis ends
    arrow_x = x_max + 0.8
    arrow_y = y_max + 3
    ax.annotate('', xy=(arrow_x, 0), xytext=(x_max + 0.3, 0),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
    ax.annotate('', xy=(0, arrow_y), xytext=(0, y_max + 0.5),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5))

    # Axis labels
    ax.text(arrow_x + 0.3, -1.5, 'x', fontsize=14, fontweight='bold')
    ax.text(0.4, arrow_y + 1, 'y', fontsize=14, fontweight='bold')

    # Remove frame (axes spines)
    for spine in ax.spines.values():
        spine.set_visible(False)

    # Tick labels
    ax.tick_params(axis='both', which='major', labelsize=11)

    if title:
        ax.set_title(title, fontsize=14, fontweight='bold', pad=10)

    plt.tight_layout()
    save_diagram(fig, output_path)


def create_quartic_tp(config):
    """
    Create a quartic graph in turning point form y = a(x-h)^4 + k.
    Can show the curve or just provide a blank grid for sketching.

    Config:
        h: horizontal shift - turning point x-coordinate (default -2)
        k: vertical shift - turning point y-coordinate (default -1)
        a: leading coefficient (default 1)
        show_curve: Whether to draw the curve (default False = blank grid only)
        x_range: [min, max] for x-axis (default auto-calculated from h)
        y_range: [min, max] for y-axis (default auto-calculated from k)
        output_path: Where to save (default: new_images/quartic.png)
        figsize: Tuple (width, height) in inches (default (8, 8))

    Returns:
        dict with key points (turning_point, y_intercept, x_intercepts) for answer key
    """
    h = config.get('h', -2)
    k = config.get('k', -1)
    a = config.get('a', 1)
    show_curve = config.get('show_curve', False)
    output_path = config.get('output_path', 'new_images/quartic.png')
    figsize = config.get('figsize', (8, 8))

    # Calculate key points
    # y-intercept: at x=0, y = a(0-h)^4 + k = a*h^4 + k
    y_int = a * (h ** 4) + k

    # x-intercepts: (x-h)^4 = -k/a
    x_intercepts = []
    if a != 0 and -k/a >= 0:
        fourth_root = (-k/a) ** 0.25
        x_intercepts = [h - fourth_root, h + fourth_root]

    # Default ranges centered on turning point
    x_min, x_max = config.get('x_range', [h - 4, h + 4])
    y_min, y_max = config.get('y_range', [k - 5, max(k + 25, y_int + 5)])

    fig, ax = plt.subplots(figsize=figsize)

    if show_curve:
        x = np.linspace(x_min - 0.5, x_max + 0.5, 500)
        y = a * (x - h)**4 + k
        ax.plot(x, y, 'b-', linewidth=2)

        # Mark turning point
        ax.plot([h], [k], 'ko', markersize=6)

    # Grid
    ax.set_xlim(x_min - 0.5, x_max + 0.5)
    ax.set_ylim(y_min - 2, y_max + 2)

    y_range_size = y_max - y_min
    y_spacing = 5 if y_range_size <= 50 else 10

    ax.set_xticks(range(int(x_min), int(x_max) + 1))
    ax.set_yticks(np.arange(y_min, y_max + y_spacing, y_spacing))
    ax.grid(True, linestyle='-', alpha=0.4, color='lightgray', linewidth=0.8)

    # Axes
    ax.axhline(y=0, color='black', linewidth=1.5)
    ax.axvline(x=0, color='black', linewidth=1.5)

    # Arrows
    ax.annotate('', xy=(x_max + 0.8, 0), xytext=(x_max + 0.3, 0),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
    ax.annotate('', xy=(0, y_max + 3), xytext=(0, y_max + 0.5),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5))

    # Labels
    ax.text(x_max + 1, -1.5, 'x', fontsize=14, fontweight='bold')
    ax.text(0.4, y_max + 4, 'y', fontsize=14, fontweight='bold')

    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.tick_params(axis='both', which='major', labelsize=11)

    plt.tight_layout()
    save_diagram(fig, output_path)

    return {
        'turning_point': (h, k),
        'y_intercept': y_int,
        'x_intercepts': x_intercepts if x_intercepts else None
    }


# Registry of diagram types
DIAGRAM_REGISTRY = {
    'cubic_graph': create_cubic_graph,
    'blank_grid': create_blank_grid,
    'quartic_tp': create_quartic_tp,
}


def generate_diagram(diagram_type, config):
    """
    Generate a diagram of the specified type with given config.

    Args:
        diagram_type: One of 'cubic_graph', 'blank_grid', 'quartic_tp'
        config: Dictionary of configuration options

    Returns:
        Result dict with key values (for answer key generation)
    """
    if diagram_type not in DIAGRAM_REGISTRY:
        available = list(DIAGRAM_REGISTRY.keys())
        raise ValueError(f"Unknown diagram type: {diagram_type}. Available: {available}")
    return DIAGRAM_REGISTRY[diagram_type](config)


def main():
    parser = argparse.ArgumentParser(description='Generate polynomial diagrams')
    parser.add_argument('-t', '--type', help='Diagram type: cubic_graph, blank_grid, quartic_tp')
    parser.add_argument('-c', '--config', help='JSON config string')
    parser.add_argument('-o', '--output', help='Output path')
    args = parser.parse_args()

    if args.type:
        config = json.loads(args.config) if args.config else {}
        if args.output:
            config['output_path'] = args.output
        result = generate_diagram(args.type, config)
        if result:
            print(f"Key values: {result}")
    else:
        # Generate examples
        print("Generating example polynomial diagrams...")
        print("-" * 50)

        # Example 1: Cubic graph for reading intercepts
        print("\n1. Cubic graph (for reading intercepts):")
        result = create_cubic_graph({
            'x_intercepts': [-3, 1, 4],
            'leading_coef': 1,
            'output_path': 'new_images/example_cubic.png'
        })
        print(f"   x-intercepts: {result['x_intercepts']}")
        print(f"   y-intercept: {result['y_intercept']}")

        # Example 2: Blank grid for quartic sketching
        print("\n2. Blank grid for quartic y = (x-1)^4 - 16:")
        create_blank_grid({
            'x_range': [-4, 5],
            'y_range': [-20, 20],
            'y_tick_spacing': 5,
            'output_path': 'new_images/example_quartic_grid.png'
        })

        # Example 3: Blank grid for cubic sketching with interval
        print("\n3. Blank grid for cubic on interval [-1, 5]:")
        create_blank_grid({
            'x_range': [-1, 6],
            'y_range': [-20, 60],
            'y_tick_spacing': 10,
            'output_path': 'new_images/example_cubic_grid.png'
        })

        # Example 4: Quartic with curve shown
        print("\n4. Quartic graph with curve shown:")
        result = create_quartic_tp({
            'h': -2,
            'k': -1,
            'show_curve': True,
            'output_path': 'new_images/example_quartic_curve.png'
        })
        print(f"   Turning point: {result['turning_point']}")
        print(f"   y-intercept: {result['y_intercept']}")
        print(f"   x-intercepts: {result['x_intercepts']}")

        print("\n" + "-" * 50)
        print("Done! Check new_images/ folder.")


if __name__ == '__main__':
    main()
