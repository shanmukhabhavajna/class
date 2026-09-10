import matplotlib.pyplot as plt
import numpy as np

# Define the function and its derivative
def f(x):
    return np.exp(x) - 2

def df(x):
    return np.exp(x)

# Newton-Raphson initial values
x0 = 1.0
f_x0 = f(x0)
df_x0 = df(x0)
x1 = x0 - f_x0 / df_x0  # x1 ≈ 0.7358... -> 0.74

# Data for plotting the curve
x = np.linspace(0.2, 1.3, 400)
y = f(x)

# Tangent line at x0 = 1
y_tangent = f_x0 + df_x0 * (x - x0)

# Create plot
plt.figure(figsize=(8, 6))

# Plot axes
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

# Plot function and tangent line
plt.plot(x, y, label=r'$f(x) = e^x - 2$', color='blue', linewidth=2)
plt.plot(x, y_tangent, label=r'Tangent line at $x_0 = 1$', color='orange', linestyle='--', linewidth=1.5)

# Highlight key points
plt.scatter([x0], [f_x0], color='red', zorder=5, label=r'Initial Point $(1, e - 2)$')
plt.scatter([x1], [0], color='green', zorder=5, label=r'First Iteration $x_1 \approx 0.74$')

# Dashed lines connecting points to axes
plt.plot([x0, x0], [0, f_x0], color='gray', linestyle=':')

# Formatting
plt.title('Newton-Raphson Method for $e^x - 2 = 0$', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.xlim(0.2, 1.3)
plt.ylim(-1.5, 2.0)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=10)

# Save plot to file instead of using plt.show()
plt.savefig('newton_raphson_plot.png', dpi=300, bbox_inches='tight')

