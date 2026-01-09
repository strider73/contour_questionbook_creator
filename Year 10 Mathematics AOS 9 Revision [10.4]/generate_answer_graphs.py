import matplotlib.pyplot as plt
import numpy as np
import os

os.makedirs('answer_images', exist_ok=True)

# Q8: y = (x+2)²(x-2) - cubic with repeated root
def q8_func(x):
    return (x + 2)**2 * (x - 2)

fig, ax = plt.subplots(figsize=(8, 6), dpi=150)
ax.set_xlim(-5, 4)
ax.set_ylim(-12, 12)
ax.grid(True, linestyle='-', alpha=0.3, color='gray')
ax.axhline(y=0, color='black', linewidth=1.5)
ax.axvline(x=0, color='black', linewidth=1.5)

x = np.linspace(-5, 4, 500)
y = q8_func(x)
ax.plot(x, y, 'b-', linewidth=2.5)

# Mark intercepts
ax.plot(-2, 0, 'ro', markersize=10, zorder=5)
ax.annotate('(-2, 0)\ntouches', (-2, 0), textcoords='offset points', xytext=(-15, 12), ha='center', fontsize=10, fontweight='bold')

ax.plot(2, 0, 'ro', markersize=10, zorder=5)
ax.annotate('(2, 0)\ncrosses', (2, 0), textcoords='offset points', xytext=(15, 12), ha='center', fontsize=10, fontweight='bold')

# Y-intercept
y_int = q8_func(0)
ax.plot(0, y_int, 'ro', markersize=10, zorder=5)
ax.annotate(f'(0, {int(y_int)})', (0, y_int), textcoords='offset points', xytext=(12, -5), ha='left', fontsize=11, fontweight='bold')

ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_title('Answer: y = (x+2)²(x-2)', fontsize=12, fontweight='bold')
ax.set_xticks(range(-5, 5))
ax.set_yticks(range(-12, 14, 2))
plt.tight_layout()
plt.savefig('answer_images/q8_answer.png', bbox_inches='tight', facecolor='white')
plt.close()
print("Created: answer_images/q8_answer.png")


# Q11: y = (x-1)⁴ - 2 - quartic with turning point
def q11_func(x):
    return (x - 1)**4 - 2

fig, ax = plt.subplots(figsize=(8, 6), dpi=150)
ax.set_xlim(-3, 5)
ax.set_ylim(-4, 16)
ax.grid(True, linestyle='-', alpha=0.3, color='gray')
ax.axhline(y=0, color='black', linewidth=1.5)
ax.axvline(x=0, color='black', linewidth=1.5)

x = np.linspace(-3, 5, 500)
y = q11_func(x)
ax.plot(x, y, 'b-', linewidth=2.5)

# Turning point
ax.plot(1, -2, 'ro', markersize=10, zorder=5)
ax.annotate('(1, -2)\nturning point', (1, -2), textcoords='offset points', xytext=(15, -15), ha='left', fontsize=10, fontweight='bold')

# Y-intercept
y_int = q11_func(0)
ax.plot(0, y_int, 'ro', markersize=10, zorder=5)
ax.annotate(f'(0, {int(y_int)})', (0, y_int), textcoords='offset points', xytext=(-25, 5), ha='right', fontsize=11, fontweight='bold')

# X-intercepts (approximate)
x_int1 = 1 - 2**(1/4)
x_int2 = 1 + 2**(1/4)
ax.plot(x_int1, 0, 'ro', markersize=8, zorder=5)
ax.plot(x_int2, 0, 'ro', markersize=8, zorder=5)

ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_title('Answer: y = (x-1)⁴ - 2', fontsize=12, fontweight='bold')
ax.set_xticks(range(-3, 6))
ax.set_yticks(range(-4, 18, 2))
plt.tight_layout()
plt.savefig('answer_images/q11_answer.png', bbox_inches='tight', facecolor='white')
plt.close()
print("Created: answer_images/q11_answer.png")


# Q13: y = -3/(x+2) + 1 - hyperbola
def q13_func(x):
    return -3 / (x + 2) + 1

fig, ax = plt.subplots(figsize=(8, 6), dpi=150)
ax.set_xlim(-8, 6)
ax.set_ylim(-6, 8)
ax.grid(True, linestyle='-', alpha=0.3, color='gray')
ax.axhline(y=0, color='black', linewidth=1.5)
ax.axvline(x=0, color='black', linewidth=1.5)

# Plot in two parts (avoiding asymptote)
x1 = np.linspace(-8, -2.1, 200)
x2 = np.linspace(-1.9, 6, 200)
y1 = q13_func(x1)
y2 = q13_func(x2)
ax.plot(x1, y1, 'b-', linewidth=2.5)
ax.plot(x2, y2, 'b-', linewidth=2.5)

# Asymptotes
ax.axvline(x=-2, color='red', linewidth=1.5, linestyle='--', label='x = -2')
ax.axhline(y=1, color='green', linewidth=1.5, linestyle='--', label='y = 1')

# Y-intercept
y_int = q13_func(0)
ax.plot(0, y_int, 'ro', markersize=10, zorder=5)
ax.annotate(f'(0, {y_int:.1f})', (0, y_int), textcoords='offset points', xytext=(12, -10), ha='left', fontsize=11, fontweight='bold')

# X-intercept
ax.plot(1, 0, 'ro', markersize=10, zorder=5)
ax.annotate('(1, 0)', (1, 0), textcoords='offset points', xytext=(10, 10), ha='left', fontsize=11, fontweight='bold')

# Label asymptotes
ax.annotate('VA: x = -2', (-2, 6), textcoords='offset points', xytext=(10, 0), fontsize=10, color='red')
ax.annotate('HA: y = 1', (4, 1), textcoords='offset points', xytext=(0, 10), fontsize=10, color='green')

ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_title('Answer: y = -3/(x+2) + 1', fontsize=12, fontweight='bold')
ax.set_xticks(range(-8, 7))
ax.set_yticks(range(-6, 9))
plt.tight_layout()
plt.savefig('answer_images/q13_answer.png', bbox_inches='tight', facecolor='white')
plt.close()
print("Created: answer_images/q13_answer.png")


# Q18d: Circle with tangent line
fig, ax = plt.subplots(figsize=(8, 8), dpi=150)
ax.set_xlim(-4, 8)
ax.set_ylim(-2, 12)
ax.grid(True, linestyle='-', alpha=0.3, color='gray')
ax.axhline(y=0, color='black', linewidth=1.5)
ax.axvline(x=0, color='black', linewidth=1.5)
ax.set_aspect('equal')

# Circle: (x-1)² + (y-5)² = 13
theta = np.linspace(0, 2*np.pi, 100)
r = np.sqrt(13)
cx, cy = 1, 5
x_circle = cx + r * np.cos(theta)
y_circle = cy + r * np.sin(theta)
ax.plot(x_circle, y_circle, 'b-', linewidth=2.5)

# Mark center
ax.plot(cx, cy, 'ko', markersize=8)
ax.annotate(f'Centre\n({cx}, {cy})', (cx, cy), textcoords='offset points', xytext=(15, -15), ha='left', fontsize=10)

# Tangent line: y = -x + 6 + sqrt(26)
k = 6 + np.sqrt(26)
x_line = np.linspace(-2, 6, 100)
y_line = -x_line + k
ax.plot(x_line, y_line, 'r-', linewidth=2, label=f'y = -x + {k:.2f}')

# Find and mark tangent point (approximately)
# Tangent point is where line touches circle
# For y = -x + k, tangent to (x-1)² + (y-5)² = 13
# Tangent point approximately at (2.45, 8.65)
tan_x = 2.45
tan_y = -tan_x + k
ax.plot(tan_x, tan_y, 'go', markersize=10, zorder=5)
ax.annotate(f'Tangent point\n({tan_x:.2f}, {tan_y:.2f})', (tan_x, tan_y),
            textcoords='offset points', xytext=(15, 5), ha='left', fontsize=10, fontweight='bold')

ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_title('Answer: Circle (x-1)² + (y-5)² = 13 with tangent', fontsize=12, fontweight='bold')
ax.legend(loc='lower right')
plt.tight_layout()
plt.savefig('answer_images/q18d_answer.png', bbox_inches='tight', facecolor='white')
plt.close()
print("Created: answer_images/q18d_answer.png")

print("\nAll AOS9 answer graphs created!")
