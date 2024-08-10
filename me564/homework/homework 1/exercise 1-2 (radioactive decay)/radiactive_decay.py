import matplotlib.pyplot as plt
import numpy as np

start = 0
stop = 5
x_0 = 2
lambdas = [ -5, -1, 0, 0.01, 0.1]
dt = 0.01
t = np.arange(start, stop, dt)
for l in lambdas:
    x = x_0 * np.exp(t*l)
    plt.plot(t, x, label="$\lambda$ = {0}".format(l))
plt.legend(loc="upper left")
plt.show()
