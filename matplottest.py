import matplotlib.pyplot as plt
import numpy as np

t = np.arange(1, 100)
print(t)

plt.plot(t, t**3)
plt.ylabel('beer')
plt.xlabel('time')
plt.show()
