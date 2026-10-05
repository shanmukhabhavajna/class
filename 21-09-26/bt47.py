import numpy as np

# 1. Given biomass yield and carbon conversion
c = 0.4 * 6  # c = 2.4 moles of biomass

# 2. Define Coefficient Matrix (A) for variables [a, b, d, e]
# Equations order: C-balance, N-balance, H-balance, O-balance
A = np.array([
    [0, 0, 1,  0],  # C: 0*a + 0*b + 1*d + 0*e
    [1, 0, 0,  0],  # N: 1*a + 0*b + 0*d + 0*e
    [3, 0, 0, -2],  # H: 3*a + 0*b + 0*d - 2*e
    [0, 2, -2, -1]   # O: 0*a + 2*b - 2*d - 1*e
], dtype=float)

# 3. Define Constant Vector (B)
B = np.array([
    6 - c,          # C balance right-hand side
    0.2 * c,        # N balance right-hand side
    1.8 * c - 12,   # H balance right-hand side
    0.5 * c - 6     # O balance right-hand side
], dtype=float)

# 4. Solve Matrix Equation Ax = B
x = np.linalg.solve(A, B)
a, b, d, e = x

# Print Results
print("==================================================")
print(f"Biomass produced (c) : {c:.2f} C-mol")
print(f"NH3 consumed (a)     : {a:.2f} mol")
print(f"CO2 produced (d)     : {d:.2f} mol")
print(f"H2O produced (e)     : {e:.2f} mol")
print("--------------------------------------------------")
print(f"Oxygen consumed (b)  : {b:.2f} mol O2 / mol glucose")
print("==================================================")

