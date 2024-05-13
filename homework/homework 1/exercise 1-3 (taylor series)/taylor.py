import matplotlib.pyplot as plt
import numpy as np

def sin_devide_by_x_tylor_series_at_pi(x):
    return 2 - 3 * x / np.pi + x*x / np.pi**2

start = -5
stop = 5
a = np.pi
dx = 0.01
x = np.arange(start, stop, dx)

plt.plot(x, np.sin(x) / x, label="$sin(x) / x$")
plt.plot(x, sin_devide_by_x_tylor_series_at_pi(x), label = "taylor series")
plt.legend(loc="upper left")
plt.show()