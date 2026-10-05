import numpy as np

# Define the matrix P
P = np.array([
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
])

print("P =")
print(P)

# Find the eigenvalues of P
eigenvalues = np.linalg.eigvals(P)

print("\nEigenvalues =", eigenvalues)


# ------------------------------------------------
# A: Trace of P = Sum of eigenvalues
# ------------------------------------------------

# Trace is the sum of diagonal elements
trace = np.trace(P)

# Calculate the sum of all eigenvalues
sum_eigenvalues = np.sum(eigenvalues)

print("\nA:")
print("Trace =", trace)
print("Sum of eigenvalues =", sum_eigenvalues)

# Check whether both are equal
print("A is", np.isclose(trace, sum_eigenvalues))


# ------------------------------------------------
# B: P^
