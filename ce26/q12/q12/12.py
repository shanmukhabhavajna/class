import sys
sys.path.insert(0, '/sdcard/github/matgeo/codes/CoordGeo')

import numpy as np
import matplotlib.pyplot as plt

# if using termux
import subprocess
import shlex

# --------------------------------------------------
# Given equations:
#
# x1 + x2 + x3 = 0
# x1 + 2*x3 = 0
#
# Plane 1: x + y + z = 0
# Plane 2: x + 2z = 0
# --------------------------------------------------

# Create figure and 3D axes
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# --------------------------------------------------
# Generate grid points
# --------------------------------------------------

x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)

X, Y = np.meshgrid(x, y)

# --------------------------------------------------
# Plane 1
# x + y + z = 0
# z = -x - y
# --------------------------------------------------

Z1 = -X - Y

ax.plot_surface(X, Y, Z1, alpha=0.5)

# --------------------------------------------------
# Plane 2
# x + 2z = 0
# z = -x/2
# --------------------------------------------------

Z2 = -X / 2

ax.plot_surface(X, Y, Z2, alpha=0.5)

# --------------------------------------------------
# Intersection line
#
# x + 2z = 0
# => x = -2z
#
# Put in first equation:
# x + y + z = 0
# -2z + y + z = 0
# y = z
#
# Therefore:
# (x,y,z) = (-2t,t,t)
# --------------------------------------------------

t = np.linspace(-5, 5, 100)

x_line = -2 * t
y_line = t
z_line = t

ax.plot(x_line, y_line, z_line, linewidth=3)

# --------------------------------------------------
# Origin
# --------------------------------------------------

ax.scatter(0, 0, 0, s=50)

ax.text(0, 0, 0, ' O', fontsize=12)

# --------------------------------------------------
# Axes limits
# --------------------------------------------------

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(-5, 5)

ax.set_box_aspect([1, 1, 1])

# Labels
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_zlabel('$x_3$')

plt.grid()

# --------------------------------------------------
# Save figure
# --------------------------------------------------

plt.savefig('q12.pdf')

# if using Termux
subprocess.run(shlex.split("termux-open q12.pdf"))
