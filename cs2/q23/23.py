import numpy as np
import matplotlib.pyplot as plt

# 1. Take input k from user
k = float(input("Enter value for k: "))

# 2. Build Coefficient Matrix A and Augmented Matrix [A|b]
A = np.array([[1.0, k], 
              [k, 1.0]])

b = np.array([[1.0], 
              [-1.0]])

Aug = np.hstack((A, b))

# 3. Calculate ranks using matrix algebra (No Determinants used)
rank_A = np.linalg.matrix_rank(A)
rank_Aug = np.linalg.matrix_rank(Aug)

print("\n--- MATRIX ANALYSIS ---")
print(f"Rank of A: {rank_A}")
print(f"Rank of Augmented Matrix [A|b]: {rank_Aug}")

# Determine solution type using Rouché–Capelli theorem
if rank_A == rank_Aug == 2:
    sol = np.linalg.solve(A, b)
    x_sol, y_sol = sol[0][0], sol[1][0]
    print(f"Result: UNIQUE SOLUTION at x = {x_sol:.2f}, y = {y_sol:.2f}")
elif rank_A < rank_Aug:
    x_sol, y_sol = None, None
    print("Result: NO SOLUTION (Parallel Lines)")
else:
    x_sol, y_sol = None, None
    print("Result: INFINITELY MANY SOLUTIONS (Coincident Lines)")

# 4. Plotting the lines
x_vals = np.linspace(-10, 10, 400)
plt.figure(figsize=(8, 6))

# Line 1: x + ky = 1
if k != 0:
    y1_vals = (1 - x_vals) / k
    plt.plot(x_vals, y1_vals, label=f"Line 1: x + {k}y = 1", color="blue")
else:
    plt.axvline(x=1, label="Line 1: x = 1", color="blue")

# Line 2: kx + y = -1
y2_vals = -1 - k * x_vals
plt.plot(x_vals, y2_vals, label=f"Line 2: {k}x + y = -1", color="red", linestyle="--")

# Plot intersection point if unique solution exists
if x_sol is not None and y_sol is not None:
    plt.plot(x_sol, y_sol, 'ro', markersize=8, label=f'Intersection ({x_sol:.2f}, {y_sol:.2f})')

plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.grid(True, linestyle=':', alpha=0.6)
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'System of Equations for k = {k}')
plt.legend()
plt.show()

