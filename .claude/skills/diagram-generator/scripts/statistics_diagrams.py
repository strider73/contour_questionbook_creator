"""
Statistics Diagram Generator

A flexible, extensible diagram generation system for statistics and probability
test questions. Diagrams are organized by CATEGORY so they can be used across
different curriculum topics.

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
- 150 DPI for print quality
- White background
- Clear labels with appropriate font sizes
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
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


def save_diagram(fig, output_path):
    """Save diagram with standard settings."""
    ensure_output_dir(output_path)
    plt.savefig(output_path, bbox_inches='tight', facecolor='white', dpi=150)
    plt.close()
    print(f"✓ Created: {output_path}")


# =============================================================================
# CATEGORY: VENN DIAGRAMS
# =============================================================================

def create_venn(config):
    """
    Venn diagram with 2 or 3 sets.

    Config:
        num_sets: 2 or 3
        values: Dict with region values
            For 2 sets: {'a_only': x, 'b_only': y, 'both': z, 'neither': w}
            For 3 sets: {'a_only': x, 'b_only': y, 'c_only': z, 'ab': ..., 'bc': ..., 'ac': ..., 'abc': ..., 'neither': w}
        labels: Dict with set labels {'a': 'Cat', 'b': 'Dog', ...}
        total: Total number (optional, for verification)
        output_path: Where to save
        title: Optional title
    """
    num_sets = config.get('num_sets', 2)
    values = config.get('values', {})
    labels = config.get('labels', {})
    output_path = config.get('output_path', 'new_images/venn.png')
    title = config.get('title', 'Venn Diagram')

    if num_sets == 2:
        fig, ax = plt.subplots(figsize=(6, 5), dpi=150)

        # Two overlapping circles
        circle_a = plt.Circle((-0.5, 0), 1.5, fill=True, facecolor='lightblue',
                             edgecolor='blue', linewidth=2, alpha=0.5)
        circle_b = plt.Circle((0.5, 0), 1.5, fill=True, facecolor='lightcoral',
                             edgecolor='red', linewidth=2, alpha=0.5)
        ax.add_patch(circle_a)
        ax.add_patch(circle_b)

        # Labels for sets
        label_a = labels.get('a', 'A')
        label_b = labels.get('b', 'B')
        ax.text(-2, 1.5, label_a, fontsize=12, fontweight='bold', color='blue')
        ax.text(1.3, 1.5, label_b, fontsize=12, fontweight='bold', color='red')

        # Values in regions
        a_only = values.get('a_only', '')
        b_only = values.get('b_only', '')
        both = values.get('both', '')
        neither = values.get('neither', '')

        ax.text(-1.3, 0, str(a_only), fontsize=14, ha='center', va='center', fontweight='bold')
        ax.text(1.3, 0, str(b_only), fontsize=14, ha='center', va='center', fontweight='bold')
        ax.text(0, 0, str(both), fontsize=14, ha='center', va='center', fontweight='bold')
        ax.text(2.5, -1.5, f'Neither: {neither}', fontsize=11)

        # Total if provided
        total = config.get('total')
        if total:
            ax.text(2.5, -2, f'Total: {total}', fontsize=10)

        ax.set_xlim(-3, 3.5)
        ax.set_ylim(-2.5, 2.5)
        ax.set_aspect('equal')
        ax.axis('off')
        if title:
            ax.set_title(title, fontsize=11, pad=10, fontweight='bold')

    elif num_sets == 3:
        fig, ax = plt.subplots(figsize=(7, 6), dpi=150)

        # Three overlapping circles
        r = 1.3
        centers = [(-0.6, 0.3), (0.6, 0.3), (0, -0.6)]
        colors = [('lightblue', 'blue'), ('lightcoral', 'red'), ('lightgreen', 'green')]
        set_keys = ['a', 'b', 'c']

        for i, (center, (fc, ec)) in enumerate(zip(centers, colors)):
            circle = plt.Circle(center, r, fill=True, facecolor=fc,
                               edgecolor=ec, linewidth=2, alpha=0.4)
            ax.add_patch(circle)

        # Labels
        label_positions = [(-1.5, 1.3), (1.5, 1.3), (0, -2)]
        for i, pos in enumerate(label_positions):
            label = labels.get(set_keys[i], set_keys[i].upper())
            ax.text(*pos, label, fontsize=12, fontweight='bold', color=colors[i][1])

        # Values - approximate positions for 3-set Venn
        ax.text(-1, 0.5, str(values.get('a_only', '')), fontsize=12, ha='center', fontweight='bold')
        ax.text(1, 0.5, str(values.get('b_only', '')), fontsize=12, ha='center', fontweight='bold')
        ax.text(0, -1.2, str(values.get('c_only', '')), fontsize=12, ha='center', fontweight='bold')
        ax.text(0, 0.8, str(values.get('ab', '')), fontsize=12, ha='center', fontweight='bold')
        ax.text(-0.5, -0.3, str(values.get('ac', '')), fontsize=12, ha='center', fontweight='bold')
        ax.text(0.5, -0.3, str(values.get('bc', '')), fontsize=12, ha='center', fontweight='bold')
        ax.text(0, 0.15, str(values.get('abc', '')), fontsize=12, ha='center', fontweight='bold')

        neither = values.get('neither', '')
        ax.text(2, -1.5, f'Neither: {neither}', fontsize=11)

        ax.set_xlim(-2.5, 3)
        ax.set_ylim(-2.5, 2)
        ax.set_aspect('equal')
        ax.axis('off')
        if title:
            ax.set_title(title, fontsize=11, pad=10, fontweight='bold')

    save_diagram(fig, output_path)


# =============================================================================
# CATEGORY: TREE DIAGRAMS
# =============================================================================

def create_tree(config):
    """
    Probability tree diagram.

    Config:
        branches: List of dicts defining tree structure
            Each level: [{'label': 'R', 'prob': '2/3', 'children': [...]}]
        replacement: True (with replacement) or False (without)
        output_path: Where to save
        title: Optional title
    """
    branches = config.get('branches', [])
    output_path = config.get('output_path', 'new_images/tree.png')
    title = config.get('title', 'Tree Diagram')

    fig, ax = plt.subplots(figsize=(8, 6), dpi=150)

    def draw_branch(x, y, branch, level, y_spread):
        """Recursively draw tree branches."""
        if not branch:
            return

        n_children = len(branch)
        y_positions = np.linspace(y - y_spread/2, y + y_spread/2, n_children)

        for i, (child, y_end) in enumerate(zip(branch, y_positions)):
            x_end = x + 2

            # Draw branch line
            ax.plot([x, x_end], [y, y_end], 'k-', linewidth=1.5)

            # Draw probability label
            mid_x = (x + x_end) / 2
            mid_y = (y + y_end) / 2
            prob = child.get('prob', '')
            ax.text(mid_x, mid_y + 0.15, prob, fontsize=10, ha='center',
                   color='blue', fontweight='bold')

            # Draw outcome label
            label = child.get('label', '')
            ax.text(x_end + 0.1, y_end, label, fontsize=11, va='center', fontweight='bold')

            # Draw final outcome if at leaf
            if 'outcome' in child:
                ax.text(x_end + 0.5, y_end, f"({child['outcome']})", fontsize=10, va='center')

            # Recursively draw children
            if 'children' in child:
                draw_branch(x_end, y_end, child['children'], level + 1, y_spread / 2)

    # Start drawing from root
    ax.plot(0, 0, 'ko', markersize=8)
    draw_branch(0, 0, branches, 0, 4)

    ax.set_xlim(-0.5, 8)
    ax.set_ylim(-3, 3)
    ax.axis('off')
    if title:
        ax.set_title(title, fontsize=11, pad=10, fontweight='bold')

    save_diagram(fig, output_path)


def create_tree_simple(config):
    """
    Simple tree diagram with predefined structure for common scenarios.

    Config:
        items: Dict of items and counts, e.g., {'R': 3, 'B': 2}
        stages: Number of stages (1 or 2)
        replacement: True (with replacement) or False (without)
        output_path: Where to save
        title: Optional title
    """
    items = config.get('items', {'R': 3, 'B': 2})
    stages = config.get('stages', 2)
    replacement = config.get('replacement', True)
    output_path = config.get('output_path', 'new_images/tree_simple.png')
    title = config.get('title', None)

    total = sum(items.values())
    item_list = list(items.keys())

    fig, ax = plt.subplots(figsize=(9, 6), dpi=150)

    # First stage
    y_positions_1 = np.linspace(2, -2, len(items))
    x_start = 0
    x_end_1 = 2.5

    ax.plot(x_start, 0, 'ko', markersize=8)

    second_stage_starts = []

    for i, (item, count) in enumerate(items.items()):
        y_end = y_positions_1[i]

        # Draw branch
        ax.plot([x_start, x_end_1], [0, y_end], 'k-', linewidth=1.5)

        # Probability
        prob = f'{count}/{total}'
        mid_x = (x_start + x_end_1) / 2
        mid_y = y_end / 2
        ax.text(mid_x - 0.3, mid_y + 0.2, prob, fontsize=10, color='blue', fontweight='bold')

        # Outcome
        ax.text(x_end_1 + 0.1, y_end, item, fontsize=12, va='center', fontweight='bold')
        ax.plot(x_end_1, y_end, 'ko', markersize=5)

        second_stage_starts.append((x_end_1, y_end, item, count))

    # Second stage (if requested)
    if stages >= 2:
        x_end_2 = 5.5

        for x1, y1, first_item, first_count in second_stage_starts:
            # Calculate new totals based on replacement
            if replacement:
                new_total = total
                new_items = items.copy()
            else:
                new_total = total - 1
                new_items = items.copy()
                new_items[first_item] = max(0, new_items[first_item] - 1)

            n_second = len([v for v in new_items.values() if v > 0])
            y_spread = 0.8
            y_positions_2 = np.linspace(y1 - y_spread, y1 + y_spread, len(new_items))

            for j, (item2, count2) in enumerate(new_items.items()):
                if count2 == 0:
                    continue

                y_end_2 = y_positions_2[j]

                # Draw branch
                ax.plot([x1, x_end_2], [y1, y_end_2], 'k-', linewidth=1.5)

                # Probability
                prob2 = f'{count2}/{new_total}'
                mid_x2 = (x1 + x_end_2) / 2
                mid_y2 = (y1 + y_end_2) / 2
                ax.text(mid_x2 - 0.2, mid_y2 + 0.15, prob2, fontsize=9, color='blue')

                # Final outcome
                outcome = first_item + item2
                ax.text(x_end_2 + 0.1, y_end_2, f'{item2} ({outcome})', fontsize=10, va='center')

    # Title
    if not title:
        rep_text = "with replacement" if replacement else "without replacement"
        title = f'Tree diagram ({rep_text})'

    ax.set_xlim(-0.5, 7)
    ax.set_ylim(-3, 3)
    ax.axis('off')
    ax.set_title(title, fontsize=11, pad=10, fontweight='bold')

    save_diagram(fig, output_path)


# =============================================================================
# CATEGORY: TABLES
# =============================================================================

def create_two_way_table(config):
    """
    Two-way (contingency) table.

    Config:
        data: 2D list of values (including totals if desired)
        row_labels: List of row labels
        col_labels: List of column labels
        highlight_cell: Optional tuple (row, col) to highlight
        output_path: Where to save
        title: Optional title
    """
    data = config.get('data', [[10, 15, 25], [20, 30, 50], [30, 45, 75]])
    row_labels = config.get('row_labels', ['Row 1', 'Row 2', 'Total'])
    col_labels = config.get('col_labels', ['Col A', 'Col B', 'Total'])
    highlight = config.get('highlight_cell', None)
    output_path = config.get('output_path', 'new_images/two_way_table.png')
    title = config.get('title', '')

    fig, ax = plt.subplots(figsize=(6, 4), dpi=150)
    ax.axis('off')

    # Create table
    n_rows = len(data)
    n_cols = len(data[0]) if data else 0

    # Add column labels
    full_col_labels = [''] + col_labels

    # Add row labels to data
    table_data = []
    for i, row in enumerate(data):
        table_data.append([row_labels[i]] + [str(v) for v in row])

    table = ax.table(
        cellText=table_data,
        colLabels=full_col_labels,
        loc='center',
        cellLoc='center'
    )

    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1.2, 1.5)

    # Style header row
    for j in range(len(full_col_labels)):
        table[(0, j)].set_facecolor('lightgray')
        table[(0, j)].set_text_props(fontweight='bold')

    # Style first column (row labels)
    for i in range(1, n_rows + 1):
        table[(i, 0)].set_facecolor('lightgray')
        table[(i, 0)].set_text_props(fontweight='bold')

    # Highlight cell if specified
    if highlight:
        row_idx, col_idx = highlight
        table[(row_idx + 1, col_idx + 1)].set_facecolor('yellow')

    if title:
        ax.set_title(title, fontsize=11, pad=20, fontweight='bold')

    save_diagram(fig, output_path)


# =============================================================================
# CATEGORY: BOX PLOTS
# =============================================================================

def create_box_plot(config):
    """
    Box-and-whisker plot (single or comparison).

    Config:
        datasets: List of dicts, each with 'min', 'q1', 'median', 'q3', 'max'
            OR list of raw data arrays
        labels: List of labels for each dataset
        outliers: List of lists of outlier values for each dataset
        show_values: True to show five-number summary values
        output_path: Where to save
        title: Optional title
    """
    datasets = config.get('datasets', [])
    labels = config.get('labels', [])
    outliers = config.get('outliers', [])
    show_values = config.get('show_values', False)
    output_path = config.get('output_path', 'new_images/box_plot.png')
    title = config.get('title', 'Box Plot')

    fig, ax = plt.subplots(figsize=(8, 5), dpi=150)

    # Process datasets
    bp_data = []
    positions = list(range(1, len(datasets) + 1))

    for i, ds in enumerate(datasets):
        if isinstance(ds, dict):
            # Five-number summary provided
            # Create dummy data that will produce this box plot
            fns = ds
            bp_data.append([fns['min'], fns['q1'], fns['median'], fns['q3'], fns['max']])
        else:
            # Raw data
            bp_data.append(ds)

    # Create box plot
    if all(isinstance(d, list) and len(d) == 5 for d in bp_data):
        # Manual box plot from five-number summaries
        for i, (pos, fns) in enumerate(zip(positions, bp_data)):
            min_val, q1, median, q3, max_val = fns

            # Box
            box = patches.Rectangle((pos - 0.3, q1), 0.6, q3 - q1,
                                    fill=True, facecolor='lightblue',
                                    edgecolor='blue', linewidth=2)
            ax.add_patch(box)

            # Median line
            ax.plot([pos - 0.3, pos + 0.3], [median, median], 'r-', linewidth=2)

            # Whiskers
            ax.plot([pos, pos], [min_val, q1], 'b-', linewidth=1.5)
            ax.plot([pos, pos], [q3, max_val], 'b-', linewidth=1.5)

            # Whisker caps
            ax.plot([pos - 0.15, pos + 0.15], [min_val, min_val], 'b-', linewidth=1.5)
            ax.plot([pos - 0.15, pos + 0.15], [max_val, max_val], 'b-', linewidth=1.5)

            # Show values if requested
            if show_values:
                ax.text(pos + 0.4, min_val, f'{min_val}', fontsize=9, va='center')
                ax.text(pos + 0.4, q1, f'{q1}', fontsize=9, va='center')
                ax.text(pos + 0.4, median, f'{median}', fontsize=9, va='center', color='red')
                ax.text(pos + 0.4, q3, f'{q3}', fontsize=9, va='center')
                ax.text(pos + 0.4, max_val, f'{max_val}', fontsize=9, va='center')

            # Outliers
            if i < len(outliers) and outliers[i]:
                for o in outliers[i]:
                    ax.plot(pos, o, 'kx', markersize=8, markeredgewidth=2)

        # Set x-axis
        ax.set_xticks(positions)
        ax.set_xticklabels(labels if labels else [f'Dataset {i+1}' for i in range(len(datasets))])

        # Determine y-axis range
        all_vals = [v for fns in bp_data for v in fns]
        if outliers:
            for o_list in outliers:
                if o_list:
                    all_vals.extend(o_list)
        y_min = min(all_vals) - (max(all_vals) - min(all_vals)) * 0.1
        y_max = max(all_vals) + (max(all_vals) - min(all_vals)) * 0.1
        ax.set_ylim(y_min, y_max)

    else:
        # Use matplotlib's boxplot for raw data
        bp = ax.boxplot(bp_data, positions=positions, patch_artist=True)
        for patch in bp['boxes']:
            patch.set_facecolor('lightblue')

        ax.set_xticklabels(labels if labels else [f'Dataset {i+1}' for i in range(len(datasets))])

    ax.set_xlim(0.5, len(datasets) + 0.5)
    ax.grid(True, axis='y', alpha=0.3)

    if title:
        ax.set_title(title, fontsize=11, pad=10, fontweight='bold')

    save_diagram(fig, output_path)


# =============================================================================
# CATEGORY: SCATTER PLOTS
# =============================================================================

def create_scatter(config):
    """
    Scatter plot with optional line of best fit.

    Config:
        x_data: List of x values
        y_data: List of y values
        x_label: Label for x-axis
        y_label: Label for y-axis
        show_lobf: True to show line of best fit
        lobf_points: Optional tuple of 2 points to define LOBF manually
        output_path: Where to save
        title: Optional title
    """
    x_data = config.get('x_data', [])
    y_data = config.get('y_data', [])
    x_label = config.get('x_label', 'x')
    y_label = config.get('y_label', 'y')
    show_lobf = config.get('show_lobf', False)
    lobf_points = config.get('lobf_points', None)
    output_path = config.get('output_path', 'new_images/scatter.png')
    title = config.get('title', 'Scatter Plot')

    fig, ax = plt.subplots(figsize=(7, 5), dpi=150)

    # Plot points
    ax.scatter(x_data, y_data, c='blue', s=50, zorder=5)

    # Line of best fit
    if show_lobf:
        if lobf_points:
            # Manual LOBF from two points
            (x1, y1), (x2, y2) = lobf_points
            m = (y2 - y1) / (x2 - x1)
            c = y1 - m * x1
        else:
            # Calculate LOBF using numpy
            m, c = np.polyfit(x_data, y_data, 1)

        x_line = np.array([min(x_data), max(x_data)])
        y_line = m * x_line + c
        ax.plot(x_line, y_line, 'r-', linewidth=2, label=f'y = {m:.2f}x + {c:.2f}')
        ax.legend()

    ax.set_xlabel(x_label, fontsize=11)
    ax.set_ylabel(y_label, fontsize=11)
    ax.grid(True, alpha=0.3)

    if title:
        ax.set_title(title, fontsize=11, pad=10, fontweight='bold')

    save_diagram(fig, output_path)


# =============================================================================
# CATEGORY: HISTOGRAMS & STEM-LEAF
# =============================================================================

def create_histogram(config):
    """
    Frequency histogram.

    Config:
        data: List of values OR dict with {'bins': [...], 'frequencies': [...]}
        bins: Number of bins or list of bin edges
        x_label: Label for x-axis
        y_label: Label for y-axis (default: 'Frequency')
        output_path: Where to save
        title: Optional title
    """
    data = config.get('data', [])
    bins = config.get('bins', 10)
    x_label = config.get('x_label', 'Value')
    y_label = config.get('y_label', 'Frequency')
    output_path = config.get('output_path', 'new_images/histogram.png')
    title = config.get('title', 'Histogram')

    fig, ax = plt.subplots(figsize=(7, 5), dpi=150)

    if isinstance(data, dict):
        # Pre-computed bins and frequencies
        bin_edges = data['bins']
        frequencies = data['frequencies']
        widths = [bin_edges[i+1] - bin_edges[i] for i in range(len(frequencies))]
        ax.bar(bin_edges[:-1], frequencies, width=widths, align='edge',
               edgecolor='black', facecolor='steelblue', alpha=0.7)
    else:
        # Raw data
        ax.hist(data, bins=bins, edgecolor='black', facecolor='steelblue', alpha=0.7)

    ax.set_xlabel(x_label, fontsize=11)
    ax.set_ylabel(y_label, fontsize=11)
    ax.grid(True, axis='y', alpha=0.3)

    if title:
        ax.set_title(title, fontsize=11, pad=10, fontweight='bold')

    save_diagram(fig, output_path)


def create_stem_leaf(config):
    """
    Stem-and-leaf plot (as an image).

    Config:
        data: List of values
        stem_unit: Unit for stem (default: 10)
        title: Optional title
        output_path: Where to save
    """
    data = config.get('data', [])
    stem_unit = config.get('stem_unit', 10)
    output_path = config.get('output_path', 'new_images/stem_leaf.png')
    title = config.get('title', 'Stem-and-Leaf Plot')

    # Organize data into stems and leaves
    stems = {}
    for val in sorted(data):
        stem = val // stem_unit
        leaf = val % stem_unit
        if stem not in stems:
            stems[stem] = []
        stems[stem].append(leaf)

    # Create figure
    fig, ax = plt.subplots(figsize=(6, max(4, len(stems) * 0.4)), dpi=150)
    ax.axis('off')

    # Draw stem-leaf plot as text table
    y_pos = 0.95
    line_height = 0.08

    ax.text(0.3, y_pos + 0.03, 'Stem', fontsize=11, fontweight='bold', ha='center')
    ax.text(0.5, y_pos + 0.03, '|', fontsize=11, fontweight='bold', ha='center')
    ax.text(0.7, y_pos + 0.03, 'Leaf', fontsize=11, fontweight='bold', ha='center')

    y_pos -= line_height

    for stem in sorted(stems.keys()):
        leaves = ' '.join(str(l) for l in sorted(stems[stem]))
        ax.text(0.3, y_pos, str(stem), fontsize=11, ha='center')
        ax.text(0.5, y_pos, '|', fontsize=11, ha='center')
        ax.text(0.55, y_pos, leaves, fontsize=11, ha='left')
        y_pos -= line_height

    # Key
    ax.text(0.3, y_pos - 0.05, f'Key: stem|leaf = value (stem unit = {stem_unit})',
            fontsize=9, style='italic')

    if title:
        ax.set_title(title, fontsize=11, pad=10, fontweight='bold')

    save_diagram(fig, output_path)


# =============================================================================
# CATEGORY: NORMAL DISTRIBUTION
# =============================================================================

def create_normal_curve(config):
    """
    Normal distribution curve with regions marked.

    Config:
        mean: Mean of distribution
        std: Standard deviation
        show_regions: True to show 68-95-99.7 regions
        shade_region: Optional tuple (lower, upper) to shade a region
        z_marks: List of z-scores to mark on x-axis
        output_path: Where to save
        title: Optional title
    """
    mean = config.get('mean', 0)
    std = config.get('std', 1)
    show_regions = config.get('show_regions', True)
    shade_region = config.get('shade_region', None)
    z_marks = config.get('z_marks', None)
    output_path = config.get('output_path', 'new_images/normal.png')
    title = config.get('title', 'Normal Distribution')

    fig, ax = plt.subplots(figsize=(8, 5), dpi=150)

    # Generate curve
    x = np.linspace(mean - 4*std, mean + 4*std, 1000)
    y = (1 / (std * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std) ** 2)

    ax.plot(x, y, 'b-', linewidth=2)
    ax.fill_between(x, y, alpha=0.1)

    # Show regions
    if show_regions:
        # 68% region
        x_68 = x[(x >= mean - std) & (x <= mean + std)]
        y_68 = y[(x >= mean - std) & (x <= mean + std)]
        ax.fill_between(x_68, y_68, alpha=0.3, color='green', label='68%')

        # Mark standard deviations
        for i in range(-3, 4):
            ax.axvline(mean + i*std, color='gray', linestyle='--', alpha=0.5)
            if i != 0:
                ax.text(mean + i*std, -0.02, f'{i}σ', fontsize=9, ha='center')

    # Shade specific region
    if shade_region:
        lower, upper = shade_region
        x_shade = x[(x >= lower) & (x <= upper)]
        y_shade = y[(x >= lower) & (x <= upper)]
        ax.fill_between(x_shade, y_shade, alpha=0.5, color='red')

    # Mark specific z-scores
    if z_marks:
        for z in z_marks:
            x_val = mean + z * std
            ax.axvline(x_val, color='red', linestyle='-', linewidth=1.5)
            ax.text(x_val, max(y) * 1.05, f'z={z}', fontsize=10, ha='center', color='red')

    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(mean, color='black', linewidth=1)
    ax.text(mean, -0.03, 'μ', fontsize=11, ha='center')

    ax.set_xlabel('Value', fontsize=11)
    ax.set_ylabel('Probability Density', fontsize=11)

    if title:
        ax.set_title(title, fontsize=11, pad=10, fontweight='bold')

    save_diagram(fig, output_path)


# =============================================================================
# DIAGRAM REGISTRY
# =============================================================================

DIAGRAM_REGISTRY = {
    # Venn diagrams
    'venn': create_venn,

    # Tree diagrams
    'tree': create_tree,
    'tree_simple': create_tree_simple,

    # Tables
    'two_way_table': create_two_way_table,

    # Box plots
    'box_plot': create_box_plot,

    # Scatter plots
    'scatter': create_scatter,

    # Histograms
    'histogram': create_histogram,
    'stem_leaf': create_stem_leaf,

    # Normal distribution
    'normal': create_normal_curve,
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
    parser = argparse.ArgumentParser(description='Generate statistics diagrams')
    parser.add_argument('--type', '-t', required=True,
                       choices=list(DIAGRAM_REGISTRY.keys()),
                       help='Type of diagram to generate')
    parser.add_argument('--config', '-c', type=str,
                       help='JSON configuration string or path to JSON file')
    parser.add_argument('--output', '-o', type=str,
                       help='Output path (overrides config)')

    args = parser.parse_args()

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
    import sys
    if len(sys.argv) == 1:
        print("\n" + "="*60)
        print("STATISTICS DIAGRAM GENERATOR - EXAMPLES")
        print("="*60 + "\n")

        # Example: Venn diagram
        generate_diagram('venn', {
            'num_sets': 2,
            'values': {'a_only': 17, 'b_only': 12, 'both': 8, 'neither': 13},
            'labels': {'a': 'Cat', 'b': 'Dog'},
            'total': 50,
            'output_path': 'new_images/example_venn.png'
        })

        # Example: Tree diagram
        generate_diagram('tree_simple', {
            'items': {'R': 2, 'B': 1},
            'stages': 2,
            'replacement': True,
            'output_path': 'new_images/example_tree.png'
        })

        # Example: Two-way table
        generate_diagram('two_way_table', {
            'data': [[135, 15, 150], [45, 30, 75], [180, 45, 225]],
            'row_labels': ['Grade 9', 'Grade 10', 'Total'],
            'col_labels': ['Present', 'Absent', 'Total'],
            'output_path': 'new_images/example_table.png'
        })

        # Example: Box plot comparison
        generate_diagram('box_plot', {
            'datasets': [
                {'min': 45, 'q1': 52, 'median': 58, 'q3': 65, 'max': 78},
                {'min': 50, 'q1': 60, 'median': 68, 'q3': 75, 'max': 85}
            ],
            'labels': ['Class A', 'Class B'],
            'show_values': True,
            'output_path': 'new_images/example_boxplot.png'
        })

        # Example: Scatter plot
        generate_diagram('scatter', {
            'x_data': [18, 20, 22, 24, 26, 28, 30],
            'y_data': [40, 50, 55, 70, 75, 85, 95],
            'x_label': 'Temperature (°C)',
            'y_label': 'Ice creams sold',
            'show_lobf': True,
            'output_path': 'new_images/example_scatter.png'
        })

        # Example: Normal curve
        generate_diagram('normal', {
            'mean': 100,
            'std': 15,
            'show_regions': True,
            'title': 'IQ Distribution',
            'output_path': 'new_images/example_normal.png'
        })

        print("\n" + "="*60)
        print("EXAMPLES GENERATED - see new_images/ folder")
        print("="*60 + "\n")
    else:
        main()
