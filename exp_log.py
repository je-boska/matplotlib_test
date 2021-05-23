import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

x_values = np.array([0, 1, 2, 3])
y_values = np.array([1, 4, 16, 64])

xnew = np.linspace(x_values.min(), x_values.max(), 100)
spl = make_interp_spline(x_values, y_values, k=2)
y_smooth = spl(xnew)
plt.plot(xnew, y_smooth)

x_log_values = np.array([1, 4, 16, 64])
y_log_values = np.array([0, 1, 2, 3])

xnew_log = np.linspace(x_log_values.min(), x_log_values.max(), 100)
spl = make_interp_spline(x_log_values, y_log_values, k=2)
y_smooth_log = spl(xnew_log)
plt.plot(xnew_log, y_smooth_log)

# plt.plot(x_values, y_values)
# plt.plot(x_log_values, y_log_values)

plt.ylabel('y')
plt.xlabel('x')

plt.grid(b=True)
plt.xlim(0, 20)
plt.ylim(0, 20)

plt.show()
