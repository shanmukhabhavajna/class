import numpy as np
import matplotlib.pyplot as plt

# Coefficient matrix
A = np.array([[2, 3],
              [4, 6]])

print("Coefficient matrix A:")
print(A)

# Determinant
det_A = np.linalg.det(A)

print("\nDeterminant =", det_A)

# Check k values
for k in [2, 4]:

    b = np.array([6, 3*k])

    augmented = np.column_stack((A, b))

    print("\nFor k =", k)
    print("Augmented matrix:")
    print(augmented)

    rank_A = np.linalg.matrix_rank(A)
    rank_augmented = np.linalg.matrix_rank(augmented)

    print("Rank(A) =", rank_A)
    print("Rank(A|b) =", rank_augmented)

    if rank_A == rank_augmented:
        print("At least one solution")
    else:
        print("No solution")


# ---------------- PLOT ----------------

x = np.linspace(-5, 5, 400)

# First equation: 2x + 3y = 6
y1 = (6 - 2*x) / 3

# k = 2:
# 4x + 6y = 6
y_k2 = (6 - 4*x) / 6

# k = 4:
# 4x + 6y = 12
y_k4 = (12 - 4*x) / 6

plt.figure(figsize=(8, 6))

plt.plot(x, y1, label="2x + 3y = 6")
plt.plot(x, y_k2, label="4x + 6y = 6 (k=2)")
plt.plot(x, y_k4,'--' ,label="4x + 6y = 12 (k=4)")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Lines for k = 2 and k = 4")
plt.axhline(0)
plt.axvline(0)
plt.grid()
plt.legend()

plt.savefig("lines_k2_k4.png", dpi=300)
