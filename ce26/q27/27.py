import numpy as np

A = np.array([
    [9, 15],
    [15, 50]
])

# Cholesky decomposition
L = np.linalg.cholesky(A)

print("Lower triangular matrix L:")
print(L)

print("|l22| =", abs(L[1, 1]))
