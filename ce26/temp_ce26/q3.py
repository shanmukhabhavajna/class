import matplotlib.pyplot as plt
import numpy as np

# Generate x values ranging from -3 to 2
x = np.linspace(-3, 2, 400)

# Define the two quadratic equations
y1 = x**2
y2 = -x**2 - 2 * x - 1

# Create plot
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label=r"$y = x^2$", color="blue", linewidth=2)
plt.plot(x, y2, label=r"$y = -x^2 - 2x - 1$", color="red", linewidth=2)

# Graph formatting
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
plt.grid(True, linestyle=":", alpha=0.6)

plt.title("Intersection of $y = x^2$ and $y = -x^2 - 2x - 1$", fontsize=14)
plt.xlabel("$x$", fontsize=12)
plt.ylabel("$y$", fontsize=12)
plt.legend(fontsize=12)

plt.tight_layout()

# Save the plot directly as an image file
plt.savefig("quadratic_intersection.png", dpi=300)
plt.close()  # Clean up memory after saving

print("Graph successfully saved to 'quadratic_intersection.png'")

