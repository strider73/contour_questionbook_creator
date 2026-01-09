#!/usr/bin/env python3
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

# Create output directory
os.makedirs('new_images', exist_ok=True)

# Q1: Number line for interval intersection (-∞, 5] ∩ [0, ∞)
def create_q1():
    fig, ax = plt.subplots(1, 1, figsize=(10, 2))
    ax.set_xlim(-3, 8)
    ax.set_ylim(-0.5, 2.5)

    # First interval: (-∞, 5]
    ax.plot([-3, 5], [1.5, 1.5], 'b-', linewidth=4)
    ax.plot(5, 1.5, 'bo', markersize=10)
    ax.plot(-3, 1.5, 'b>', markersize=10)

    # Second interval: [0, ∞)
    ax.plot([0, 8], [0.5, 0.5], 'r-', linewidth=4)
    ax.plot(0, 0.5, 'ro', markersize=10)
    ax.plot(8, 0.5, 'r>', markersize=10)

    # Number line markings
    for i in range(-2, 8):
        ax.plot([i, i], [0.2, 0.8], 'k-', linewidth=1)
        ax.plot([i, i], [1.2, 1.8], 'k-', linewidth=1)
        ax.text(i, 2.2, str(i), ha='center', fontsize=11)

    ax.text(-2.8, 1.5, r'$(-\infty, 5]$', fontsize=12, va='center', color='blue')
    ax.text(-2.8, 0.5, r'$[0, \infty)$', fontsize=12, va='center', color='red')

    ax.axis('off')
    plt.tight_layout()
    plt.savefig('new_images/q1_number_line.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ Q1 diagram created")

# Q3: Function graph - coordinate plane
def create_q3():
    fig, ax = plt.subplots(1, 1, figsize=(6, 6))
    ax.set_xlim(-4, 5)
    ax.set_ylim(-2, 5)
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, color='k', linewidth=1)
    ax.axvline(x=0, color='k', linewidth=1)

    # Plot points: {(3, 1), (-2, 4), (3, -1)}
    points = [(3, 1), (-2, 4), (3, -1)]
    for p in points:
        ax.plot(p[0], p[1], 'bo', markersize=10)
        ax.text(p[0]+0.3, p[1]+0.3, f'({p[0]}, {p[1]})', fontsize=10)

    ax.set_xlabel('x', fontsize=11)
    ax.set_ylabel('y', fontsize=11)
    ax.set_title('Relation: {(3, 1), (-2, 4), (3, -1)}', fontsize=11)
    plt.tight_layout()
    plt.savefig('new_images/q3_function_graph.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ Q3 diagram created")

# Q8: Cubic graph y = (x + 2)^2(x - 2)
def create_q8():
    fig, ax = plt.subplots(1, 1, figsize=(7, 7))
    ax.set_xlim(-4, 4)
    ax.set_ylim(-10, 10)
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, color='k', linewidth=1)
    ax.axvline(x=0, color='k', linewidth=1)

    x = np.linspace(-3.5, 3, 300)
    y = (x + 2)**2 * (x - 2)

    ax.plot(x, y, 'b-', linewidth=2)

    # Mark intercepts
    ax.plot(-2, 0, 'ro', markersize=10)
    ax.text(-2, -1.2, '(-2, 0)', ha='center', fontsize=10)
    ax.plot(2, 0, 'ro', markersize=10)
    ax.text(2, -1.2, '(2, 0)', ha='center', fontsize=10)
    ax.plot(0, -8, 'ro', markersize=10)
    ax.text(0.5, -8, '(0, -8)', ha='left', fontsize=10)

    ax.set_xlabel('x', fontsize=11)
    ax.set_ylabel('y', fontsize=11)
    ax.set_title(r'$y = (x + 2)^2(x - 2)$', fontsize=12)
    plt.tight_layout()
    plt.savefig('new_images/q8_cubic_graph.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ Q8 diagram created")

# Q11: Quartic graph y = (x - 1)^4 - 2
def create_q11():
    fig, ax = plt.subplots(1, 1, figsize=(7, 7))
    ax.set_xlim(-2, 4)
    ax.set_ylim(-3, 8)
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, color='k', linewidth=1)
    ax.axvline(x=0, color='k', linewidth=1)

    x = np.linspace(-1.5, 3.5, 300)
    y = (x - 1)**4 - 2

    ax.plot(x, y, 'b-', linewidth=2)

    # Mark turning point
    ax.plot(1, -2, 'ro', markersize=10)
    ax.text(1.3, -2, '(1, -2)', ha='left', fontsize=10)

    # Y-intercept
    y_int = (0 - 1)**4 - 2
    ax.plot(0, y_int, 'go', markersize=10)
    ax.text(0.3, y_int, f'(0, {y_int})', ha='left', fontsize=10)

    ax.set_xlabel('x', fontsize=11)
    ax.set_ylabel('y', fontsize=11)
    ax.set_title(r'$y = (x - 1)^4 - 2$', fontsize=12)
    plt.tight_layout()
    plt.savefig('new_images/q11_quartic_graph.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ Q11 diagram created")

# Q13: Hyperbola y = -3/(x+2) + 1
def create_q13():
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    ax.set_xlim(-8, 4)
    ax.set_ylim(-5, 7)
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, color='k', linewidth=1)
    ax.axvline(x=0, color='k', linewidth=1)

    # Asymptotes
    ax.axvline(x=-2, color='r', linestyle='--', linewidth=1.5)
    ax.axhline(y=1, color='r', linestyle='--', linewidth=1.5)

    # Plot hyperbola in two parts
    x1 = np.linspace(-7.5, -2.1, 200)
    y1 = -3/(x1 + 2) + 1
    ax.plot(x1, y1, 'b-', linewidth=2)

    x2 = np.linspace(-1.9, 3.5, 200)
    y2 = -3/(x2 + 2) + 1
    ax.plot(x2, y2, 'b-', linewidth=2)

    # Y-intercept: x=0
    y_int = -3/(0 + 2) + 1
    ax.plot(0, y_int, 'go', markersize=10)
    ax.text(0.5, y_int, f'(0, {y_int:.1f})', ha='left', fontsize=10)

    # X-intercept: y=0, x=1
    ax.plot(1, 0, 'go', markersize=10)
    ax.text(1.3, 0.3, '(1, 0)', ha='left', fontsize=10)

    ax.text(-2.5, 6, 'x = -2', color='red', fontsize=11)
    ax.text(2.5, 1.5, 'y = 1', color='red', fontsize=11)

    ax.set_xlabel('x', fontsize=11)
    ax.set_ylabel('y', fontsize=11)
    ax.set_title(r'$y = \frac{-3}{x+2} + 1$', fontsize=12)
    plt.tight_layout()
    plt.savefig('new_images/q13_rational_graph.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ Q13 diagram created")

# Q18b: Circle with tangent line
def create_q18b():
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    ax.set_xlim(-5, 8)
    ax.set_ylim(0, 10)
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, color='k', linewidth=1)
    ax.axvline(x=0, color='k', linewidth=1)
    ax.set_aspect('equal')

    # Circle center and radius (will be calculated in answer)
    # From A(-2,3) and B(4,7): center = (1, 5), r = sqrt(13)
    center = (1, 5)
    radius = np.sqrt(13)

    circle = patches.Circle(center, radius, fill=False, edgecolor='blue', linewidth=2)
    ax.add_patch(circle)

    # Mark center
    ax.plot(center[0], center[1], 'ro', markersize=8)
    ax.text(center[0]+0.3, center[1]+0.3, f'C{center}', fontsize=10)

    # Mark diameter endpoints
    ax.plot(-2, 3, 'go', markersize=8)
    ax.text(-2.5, 3, 'A(-2, 3)', fontsize=10)
    ax.plot(4, 7, 'go', markersize=8)
    ax.text(4.2, 7, 'B(4, 7)', fontsize=10)

    # Draw a sample tangent line (one of the solutions)
    x_line = np.linspace(-4, 7, 100)
    y_line = -x_line + 6  # One tangent solution
    ax.plot(x_line, y_line, 'r--', linewidth=1.5, alpha=0.7, label='Tangent line')

    ax.set_xlabel('x', fontsize=11)
    ax.set_ylabel('y', fontsize=11)
    ax.set_title('Circle with Tangent Line', fontsize=12)
    ax.legend()
    plt.tight_layout()
    plt.savefig('new_images/q18b_circle_tangent.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ Q18b diagram created")

# Q18d: Blank coordinate grid
def create_q18d():
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    ax.set_xlim(-5, 8)
    ax.set_ylim(0, 10)
    ax.grid(True, alpha=0.5)
    ax.axhline(y=0, color='k', linewidth=1.5)
    ax.axvline(x=0, color='k', linewidth=1.5)
    ax.set_aspect('equal')

    # Add tick marks
    ax.set_xticks(range(-5, 9))
    ax.set_yticks(range(0, 11))

    ax.set_xlabel('x', fontsize=11)
    ax.set_ylabel('y', fontsize=11)
    ax.set_title('Coordinate Grid for Graphing', fontsize=12)
    plt.tight_layout()
    plt.savefig('new_images/q18d_coordinate_grid.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ Q18d diagram created")

# Run all diagram creation functions
if __name__ == '__main__':
    print("Creating diagrams for Version B...")
    create_q1()
    create_q3()
    create_q8()
    create_q11()
    create_q13()
    create_q18b()
    create_q18d()
    print("\n✓ All diagrams created successfully!")
