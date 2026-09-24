import numpy as np

P = np.array([
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
])

# Eigenvalues
eigenvalues = np.linalg.eigvals(P)

print("P =")
print(P)

print("\nEigenvalues =", eigenvalues)

# A: Trace = sum of eigenvalues
trace = np.trace(P)
sum_eigenvalues = np.sum(eigenvalues)

print("\nA:")
print("Trace =", trace)
print("Sum of eigenvalues =", sum_eigenvalues)
print("A is", np.isclose(trace, sum_eigenvalues))

# B: P^T P = I
PTP = P.T @ P

print("\nB:")
print("P^T P =")
print(PTP)
print("B is", np.array_equal(PTP, np.eye(3)))

#
