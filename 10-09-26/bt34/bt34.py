import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)

y1 = (6 - 2*x) / 3
y2 = (12 - 4*x) / 6

plt.plot(x, y1, label='2x + 3y = 6')
plt.plot(x, y2, '--', label='4x + 6y = 12')

plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()

plt.savefig('plot.png')
