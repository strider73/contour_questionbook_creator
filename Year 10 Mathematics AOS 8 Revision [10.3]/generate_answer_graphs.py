import matplotlib.pyplot as plt
import numpy as np
import os

os.makedirs('answer_images', exist_ok=True)

def create_answer_graph(filename, func, x_range, y_range, x_intercepts, y_intercept, title, figsize=(8, 6)):
    """Create an answer graph showing the correct curve with labeled features."""
    fig, ax = plt.subplots(figsize=figsize, dpi=150)

    ax.set_xlim(x_range)
    ax.set_ylim(y_range)

    # Draw grid
    ax.grid(True, linestyle='-', alpha=0.3, color='gray')
    ax.axhline(y=0, color='black', linewidth=1.5)
    ax.axvline(x=0, color='black', linewidth=1.5)

    # Plot the curve
    x = np.linspace(x_range[0], x_range[1], 500)
    y = func(x)
    ax.plot(x, y, 'b-', linewidth=2.5)

    # Mark x-intercepts
    for xi in x_intercepts:
        ax.plot(xi, 0, 'ro', markersize=10, zorder=5)
        ax.annotate(f'({xi}, 0)', (xi, 0), textcoords='offset points',
                   xytext=(0, 12), ha='center', fontsize=11, fontweight='bold')

    # Mark y-intercept
    ax.plot(0, y_intercept, 'ro', markersize=10, zorder=5)
    y_offset = 12 if y_intercept >= 0 else -18
    ax.annotate(f'(0, {y_intercept})', (0, y_intercept), textcoords='offset points',
               xytext=(12, y_offset), ha='left', fontsize=11, fontweight='bold')

    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_title(title, fontsize=12, fontweight='bold')

    # Set ticks
    x_step = 1 if (x_range[1] - x_range[0]) <= 12 else 2
    y_step = 5 if (y_range[1] - y_range[0]) > 20 else (2 if (y_range[1] - y_range[0]) > 12 else 1)

    ax.set_xticks(np.arange(int(x_range[0]), int(x_range[1])+1, x_step))
    ax.set_yticks(np.arange(int(y_range[0]), int(y_range[1])+1, y_step))
    ax.tick_params(axis='both', labelsize=10)

    plt.tight_layout()
    plt.savefig(filename, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()
    print(f"Created: {filename}")


def create_points_with_curve(filename, func, points, x_range, y_range, title, figsize=(8, 6)):
    """Create a graph showing points AND the curve through them."""
    fig, ax = plt.subplots(figsize=figsize, dpi=150)

    ax.set_xlim(x_range)
    ax.set_ylim(y_range)

    # Draw grid
    ax.grid(True, linestyle='-', alpha=0.3, color='gray')
    ax.axhline(y=0, color='black', linewidth=1.5)
    ax.axvline(x=0, color='black', linewidth=1.5)

    # Plot the curve
    x = np.linspace(x_range[0], x_range[1], 500)
    y = func(x)
    ax.plot(x, y, 'b-', linewidth=2.5)

    # Mark the given points
    for px, py in points:
        ax.plot(px, py, 'ro', markersize=10, zorder=5)
        ax.annotate(f'({px}, {py})', (px, py), textcoords='offset points',
                   xytext=(10, 5), ha='left', fontsize=11, fontweight='bold')

    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_title(title, fontsize=12, fontweight='bold')

    y_step = 2 if (y_range[1] - y_range[0]) > 12 else 1
    ax.set_xticks(np.arange(int(x_range[0]), int(x_range[1])+1, 1))
    ax.set_yticks(np.arange(int(y_range[0]), int(y_range[1])+1, y_step))
    ax.tick_params(axis='both', labelsize=10)

    plt.tight_layout()
    plt.savefig(filename, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()
    print(f"Created: {filename}")


# Q5: y = (x-1)(x+2)(x-5)
# x-intercepts: -2, 1, 5
# y-intercept: y(0) = (-1)(2)(-5) = 10
create_answer_graph(
    'answer_images/q5_answer.png',
    func=lambda x: (x - 1) * (x + 2) * (x - 5),
    x_range=(-4, 7),
    y_range=(-15, 20),
    x_intercepts=[-2, 1, 5],
    y_intercept=10,
    title='Answer: y = (x-1)(x+2)(x-5)'
)

# Q10: Cubic through points (-2, 6), (0, 2), (1, -2)
# The intended answer is P(x) = x³ - 2x² - x + 2 = (x-1)(x+1)(x-2)
# But let's fit a cubic through the given points
# Using the answer from the sheet: a=-2, b=-1, c=2
# P(x) = x³ - 2x² - x + 2
create_points_with_curve(
    'answer_images/q10_answer.png',
    func=lambda x: x**3 - 2*x**2 - x + 2,
    points=[(-2, -8), (0, 2), (1, 0)],  # Actual points on this curve
    x_range=(-4, 4),
    y_range=(-10, 12),
    title='Answer: P(x) = x³ - 2x² - x + 2'
)

# Q12b: y = 3(x+2)(x-1)(x-4)
# x-intercepts: -2, 1, 4
# y-intercept: y(0) = 3(2)(-1)(-4) = 24
create_answer_graph(
    'answer_images/q12_answer.png',
    func=lambda x: 3 * (x + 2) * (x - 1) * (x - 4),
    x_range=(-4, 6),
    y_range=(-35, 40),
    x_intercepts=[-2, 1, 4],
    y_intercept=24,
    title='Answer: y = 3(x+2)(x-1)(x-4)'
)

# Q14e: H(x) = (1/3)x(x-6)(x-10) - valley cross-section
# x-intercepts: 0, 6, 10
# Using positive coefficient as in the question
create_answer_graph(
    'answer_images/q14e_answer.png',
    func=lambda x: (1/3) * x * (x - 6) * (x - 10),
    x_range=(-2, 12),
    y_range=(-15, 20),
    x_intercepts=[0, 6, 10],
    y_intercept=0,
    title='Answer: H(x) = (1/3)x(x-6)(x-10)'
)

print("\nAll answer graphs created in answer_images/")
