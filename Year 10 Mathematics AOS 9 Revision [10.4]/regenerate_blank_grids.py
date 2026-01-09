import matplotlib.pyplot as plt
import numpy as np
import os

# Create new_images directory if it doesn't exist
os.makedirs('new_images', exist_ok=True)

def create_blank_grid(filename, x_range, y_range, title="", figsize=(6, 5)):
    """Create a blank coordinate grid for students to sketch on."""
    fig, ax = plt.subplots(figsize=figsize, dpi=150)

    # Set axis ranges
    ax.set_xlim(x_range)
    ax.set_ylim(y_range)

    # Draw grid
    ax.grid(True, linestyle='-', alpha=0.3, color='gray')
    ax.set_axisbelow(True)

    # Draw axes through origin
    ax.axhline(y=0, color='black', linewidth=1.5)
    ax.axvline(x=0, color='black', linewidth=1.5)

    # Add arrows to axes
    ax.annotate('', xy=(x_range[1], 0), xytext=(x_range[1]-0.5, 0),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
    ax.annotate('', xy=(0, y_range[1]), xytext=(0, y_range[1]-0.5),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5))

    # Labels
    ax.set_xlabel('x', fontsize=12, loc='right')
    ax.set_ylabel('y', fontsize=12, loc='top', rotation=0)

    # Set integer ticks
    x_ticks = np.arange(int(x_range[0]), int(x_range[1])+1, 1)
    y_ticks = np.arange(int(y_range[0]), int(y_range[1])+1, 1)

    # Filter out too many ticks if range is large
    if len(x_ticks) > 15:
        x_ticks = np.arange(int(x_range[0]), int(x_range[1])+1, 2)
    if len(y_ticks) > 15:
        y_ticks = np.arange(int(y_range[0]), int(y_range[1])+1, 2)

    ax.set_xticks(x_ticks)
    ax.set_yticks(y_ticks)

    # Make tick labels smaller
    ax.tick_params(axis='both', labelsize=9)

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    plt.tight_layout()
    plt.savefig(filename, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()
    print(f"Created: {filename}")


# Q8: Blank grid for cubic sketch y = -(x-1)^2(x+3)
# Need range to show x from about -5 to 3, y from about -10 to 10
create_blank_grid(
    'new_images/q8_cubic_graph.png',
    x_range=(-5, 4),
    y_range=(-10, 10),
    figsize=(6, 5)
)

# Q11: Blank grid for quartic sketch y = -(x+2)^4 + 1
# Turning point at (-2, 1), y-intercept at -15
# Need range to show the important features
create_blank_grid(
    'new_images/q11_quartic_graph.png',
    x_range=(-6, 4),
    y_range=(-16, 4),
    figsize=(6, 6)
)

# Q13: Blank grid for rational function y = 2/(x-1) - 3
# Vertical asymptote at x=1, horizontal asymptote at y=-3
create_blank_grid(
    'new_images/q13_rational_graph.png',
    x_range=(-6, 8),
    y_range=(-10, 6),
    figsize=(6, 5)
)

# Q18d: Blank grid for circle and tangent line
# Circle centered at (4, 2) with radius 3√2 ≈ 4.24
# Need to show circle and tangent lines
create_blank_grid(
    'new_images/q18d_coordinate_grid.png',
    x_range=(-2, 12),
    y_range=(-4, 10),
    figsize=(7, 6)
)

print("\nAll blank grids regenerated successfully!")
