import numpy as np

# System of equations:
# [1  k] [x] = [ 1]
# [k  1] [y]   [-1]

# Test a range of k values (including integers and floating-point values)
k_values = np.linspace(-3, 3, 601)

no_solution_k = []
infinite_solution_k = []

for k in k_values:
    k = round(k, 4) # avoid floating-point precision issues
    
    # Define coefficient matrix A and augmented matrix [A|b]
    A = np.array([[1, k], 
                  [k, 1]], dtype=float)
    
    b = np.array([[1], 
                  [-1]], dtype=float)
    
    Augmented = np.hstack([A, b])
    
    # Calculate matrix ranks using standard linear algebra
    rank_A = np.linalg.matrix_rank(A)
    rank_Aug = np.linalg.matrix_rank(Augmented)
    
    # Check consistency conditions (Rouché–Capelli theorem)
    if rank_A < rank_Aug:
        no_solution_k.append(k)
    elif rank_A == rank_Aug < 2:
        infinite_solution_k.append(k)

print("--- Matrix Verification Results ---")
print(f"Values of k resulting in NO SOLUTION: {no_solution_k}")
print(f"Values of k resulting in INFINITE SOLUTIONS: {infinite_solution_k}")

# Output verdict for Option (A)
if len(no_solution_k) == 1:
    print("\nOption (A) is CORRECT: There is exactly one value of k (k = 1) for which the system has no solution.")

