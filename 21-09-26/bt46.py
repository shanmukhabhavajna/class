import numpy as np
import matplotlib.pyplot as plt

# 1. Theoretical calculations
# For f(x) to be differentiable at x = 0:
# Continuity: lim_{x->0+} sin(2x) = a + b(0) => a = 0
# Differentiability: d/dx[sin(2x)]|_{x=0} = d/dx[a + bx]|_{x=0} => 2*cos(0) = b => b = 2
a = 0
b = 2
sum_ab = a + b

print("=" * 45)
print(f"Calculated Value of 'a': {a}")
print(f"Calculated Value of 'b': {b}")
print(f"Value of (a + b)       : {sum_ab}  (Option C)")
print("=" * 45)

# 2. Define domain ranges
x_neg = np.linspace(-1.5, 0, 200)
x_pos = np.linspace(0, np.pi, 300)

# Evaluate function segments
y_neg = a + b * x_neg
y_pos = np.sin(2 * x_pos)

# 3. Create the Plot
plt.figure(figsize=(9, 5))
plt.plot(x_neg, y_neg, label='f(x) = 2x  (x <= 0)', color='#1f77b4', linewidth=2.5)
plt.plot(x_pos, y_pos, label='f(x) = sin(2x)  (x > 0)', color='#ff7f0e', linewidth=2.5)

# Highlight point of differentiability at origin (0, 0)
plt.plot(0, 0, 'ro', markersize=7, label='Point of differentiability (0, 0)')

# Formatting and Grid setup
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.title('Graph of f(x) [a = 0, b = 2 => a + b = 2]', fontsize=13, fontweight='bold')
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(fontsize=11, loc='upper left')

# 4. Save image directly WITHOUT using plt.show()
output_filename = 'differentiable_function_graph.png'
plt.savefig(output_filename, dpi=300, bbox_inches='tight')
plt.close()  # Clear plot memory

print(f"Graph successfully created and saved as '{output_filename}'!")

