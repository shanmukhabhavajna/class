# Code modified for:
# 2x + 3y = 6
# 4x + 6y = 3k

import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt


# Rotation matrix by 90 degrees
omat = np.array([[0, -1],
                 [1,  0]])


# Unit vectors
e1 = np.array([[1],
               [0]])

e2 = np.array([[0],
               [1]])


# Direction vector between two points
def dir_vec(A, B):
    return B - A


# Normal vector
def norm_vec(A, B):
    return omat @ dir_vec(A, B)


# Generate line points
def line_gen_num(A, B, num):
    dim = A.shape[0]
    x_AB = np.zeros((dim, num))

    lam_1 = np.linspace(0, 1, num)

    for i in range(num):
        temp1 = A + lam_1[i] * (B - A)
        x_AB[:, i] = temp1.T

    return x_AB


# Generate line using normal form
def line_norm(n, c, k1, k2):

    c = c / LA.norm(n)
    n = n / LA.norm(n)

    if c == 0:
        A = np.zeros((2, 1))

    elif np.array_equal(n, e1):
        A = np.array(([c, 0])).reshape(-1, 1)

    elif np.array_equal(n, e2):
        A = np.array(([0, c])).reshape(-1, 1)

    else:
        A = np.array(([c / n[0][0], 0])).reshape(-1, 1)

    # Direction vector perpendicular to normal
    m = omat @ n

    return line_dir_pt(m, A, k1, k2)


# Generate line using direction vector and point
def line_dir_pt(m, A, k1, k2):

    length = 100
    dim = A.shape[0]

    x_AB = np.zeros((dim, length))

    lam_1 = np.linspace(k1, k2, length)

    for i in range(length):
        temp1 = A + lam_1[i] * m
        x_AB[:, i] = temp1.T

    return x_AB


# Intersection of two lines
def line_isect(n1, c1, n2, c2):

    # Create coefficient matrix using np.block
    N = np.block([n1, n2]).T

    # Right-hand side vector
    p = np.zeros((2, 1))

    p[0] = c1
    p[1] = c2

    # Solve Nx = p
    P = np.linalg.solve(N, p)

    return P


# Intersection using points on lines
def line_intersect(n1, A1, n2, A2):

    # Create coefficient matrix using np.block
    N = np.block([n1, n2]).T

    p = np.zeros((2, 1))

    p[0] = n1.T @ A1
    p[1] = n2.T @ A2

    P = np.linalg.solve(N, p)

    return P


# --------------------------------------------------
# OUR PROBLEM
# --------------------------------------------------

# First equation:
# 2x + 3y = 6

n1 = np.array([[2],
               [3]])

c1 = 6


# Second equation:
# 4x + 6y = 3k

n2 = np.array([[4],
               [6]])


# --------------------------------------------------
# Print coefficient matrix using np.block
# --------------------------------------------------

A = np.block([n1, n2]).T

print("Coefficient matrix A:")
print(A)

print("\nDeterminant of A:")
print(LA.det(A))


# --------------------------------------------------
# k = 2
# --------------------------------------------------

k = 2

c2 = 3 * k

print("\nFor k =", k)

print("Second equation:")
print("4x + 6y =", c2)

# Generate first line
line1 = line_norm(n1, c1, -10, 10)

# Generate second line
line2 = line_norm(n2, c2, -10, 10)


# --------------------------------------------------
# k = 4
# --------------------------------------------------

k = 4

c2 = 3 * k

print("\nFor k =", k)

print("Second equation:")
print("4x + 6y =", c2)

# Generate second line for k = 4
line3 = line_norm(n2, c2, -10, 10)


# --------------------------------------------------
# PLOT
# --------------------------------------------------

plt.figure(figsize=(8, 6))

# First equation
plt.plot(line1[0, :],
         line1[1, :],
         label="2x + 3y = 6")

# k = 2
plt.plot(line2[0, :],
         line2[1, :],
         "--",
         label="4x + 6y = 6  (k=2)")

# k = 4
plt.plot(line3[0, :],
         line3[1, :],
         ":",
         linewidth=3,
         label="4x + 6y = 12  (k=4)")


plt.xlabel("x")
plt.ylabel("y")

plt.title("Lines for k = 2 and k = 4")

plt.axhline(0)
plt.axvline(0)

plt.grid()
plt.legend()

plt.savefig("lines_k2_k4.png", dpi=300)


