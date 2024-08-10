import matplotlib.pyplot as plt
import numpy as np

def sin_devide_by_x_tylor_series_at_pi(x):
    return 2 - 3 * x / np.pi + x*x / np.pi**2

def exp_of_three_tylor_series(x, a):
    return 3**a + np.log(3) * 3**a * (x - a) + np.log(3)**2 * 1/2 * 3**a * (x - a)**2 # + O(x^3)

start = -5
stop = 5
a = 0
dx = 0.01
x = np.arange(start, stop, dx)

# plt.plot(x, np.sin(x) / x, label="$sin(x) / x$")
# plt.plot(x, sin_devide_by_x_tylor_series_at_pi(x), label = "taylor series")
plt.plot(x, 3**x, label="$3^x$")
plt.plot(x, exp_of_three_tylor_series(x, a), label = "taylor series")
plt.legend(loc="upper left")
plt.show()