import matplotlib.pyplot as plt
import numpy as np
import os

# Create new_images directory if it doesn't exist
os.makedirs('new_images', exist_ok=True)

def create_blank_grid(filename, x_range, y_range, figsize=(8, 6), x_label='x', y_label='y'):
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
    ax.annotate('', xy=(x_range[1], 0), xytext=(x_range[1]-0.3, 0),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
    ax.annotate('', xy=(0, y_range[1]), xytext=(0, y_range[1]-0.3),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5))

    # Labels
    ax.set_xlabel(x_label, fontsize=12, loc='right')
    ax.set_ylabel(y_label, fontsize=12, loc='top', rotation=0)

    # Set integer ticks
    x_step = 1
    y_step = 1
    x_span = x_range[1] - x_range[0]
    y_span = y_range[1] - y_range[0]

    if x_span > 12:
        x_step = 2
    if y_span > 20:
        y_step = 5
    elif y_span > 12:
        y_step = 2

    x_ticks = np.arange(int(x_range[0]), int(x_range[1])+1, x_step)
    y_ticks = np.arange(int(y_range[0]), int(y_range[1])+1, y_step)

    ax.set_xticks(x_ticks)
    ax.set_yticks(y_ticks)

    # Make tick labels smaller
    ax.tick_params(axis='both', labelsize=10)

    # Remove spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    plt.tight_layout()
    plt.savefig(filename, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()
    print(f"Created: {filename}")


def create_points_only_grid(filename, points, x_range, y_range, figsize=(8, 6)):
    """Create a coordinate grid with only labeled points (no curve)."""
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
    ax.annotate('', xy=(x_range[1], 0), xytext=(x_range[1]-0.3, 0),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
    ax.annotate('', xy=(0, y_range[1]), xytext=(0, y_range[1]-0.3),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5))

    # Plot points only
    for px, py in points:
        ax.plot(px, py, 'ro', markersize=10)
        ax.annotate(f'({px}, {py})', (px, py), textcoords="offset points",
                   xytext=(10, 5), fontsize=11, fontweight='bold')

    # Labels
    ax.set_xlabel('x', fontsize=12, loc='right')
    ax.set_ylabel('y', fontsize=12, loc='top', rotation=0)

    # Set integer ticks
    y_step = 1
    y_span = y_range[1] - y_range[0]
    if y_span > 12:
        y_step = 2

    x_ticks = np.arange(int(x_range[0]), int(x_range[1])+1, 1)
    y_ticks = np.arange(int(y_range[0]), int(y_range[1])+1, y_step)

    ax.set_xticks(x_ticks)
    ax.set_yticks(y_ticks)

    ax.tick_params(axis='both', labelsize=10)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    plt.tight_layout()
    plt.savefig(filename, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()
    print(f"Created: {filename}")


# Q5: Blank grid for sketching y = (x-1)(x+2)(x-5)
# x-intercepts at -2, 1, 5; y-intercept at (0, 10)
# Need range to cover these
create_blank_grid(
    'new_images/q5.png',
    x_range=(-4, 7),
    y_range=(-15, 15),
    figsize=(8, 6)
)

# Q10: Points-only diagram showing (-2, 6), (0, 2), (1, -2)
# Student must find the cubic equation passing through these points
create_points_only_grid(
    'new_images/q10.png',
    points=[(-2, 6), (0, 2), (1, -2)],
    x_range=(-4, 4),
    y_range=(-6, 10),
    figsize=(7, 6)
)

# Q12b: Blank grid for sketching y = 3(x+2)(x-1)(x-4)
# x-intercepts at -2, 1, 4; y-intercept at y = 3*2*(-1)*(-4) = 24
create_blank_grid(
    'new_images/q12.png',
    x_range=(-4, 6),
    y_range=(-30, 35),
    figsize=(8, 7)
)

# Q14e: Blank grid for sketching H(x) = (1/3)x(x-6)(x-10)
# x-intercepts at 0, 6, 10
# Need to show the curve shape
create_blank_grid(
    'new_images/q14e.png',
    x_range=(-2, 12),
    y_range=(-10, 15),
    figsize=(9, 6)
)

print("\nAll blank grids created successfully!")
print("Now recompile the LaTeX file.")
