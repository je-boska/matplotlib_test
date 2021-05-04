import matplotlib.pyplot as plt
import numpy as np

point1 = (0, 6)
point2 = (1, 4)
point3 = (2, 2)

x_values = (point1[0], point2[0], point3[0])
y_values = (point1[1], point2[1], point3[1])

plt.plot(x_values, y_values, 'bo-')

plt.ylabel('y')
plt.xlabel('x')

plt.grid(b=True)
plt.xlim(-10, 10)
plt.ylim(-10, 10)

plt.axhline(color='black', lw=1)
plt.axvline(color='black', lw=1)
plt.show()
