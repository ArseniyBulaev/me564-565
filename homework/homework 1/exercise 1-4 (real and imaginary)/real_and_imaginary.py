import matplotlib.pyplot as plt
import numpy as np

start = 0
stop = 10
step = 0.01
t = np.arange(start, stop, step)

# a
plt.plot(t, np.cos(t), label="Re")
plt.plot(t, np.sin(t), label="Im")
plt.legend(loc="upper left")
plt.title("a")
plt.show()

# b
plt.plot(t, np.exp(-t) * np.cos(t), label="Re")
plt.plot(t, - np.exp(-t) * np.sin(t), label="Im")
plt.legend(loc="upper left")
plt.title("b")
plt.show()

# c
plt.plot(t, np.exp(1) * np.cos(t), label="Re")
plt.plot(t, - np.exp(1) * np.sin(t), label="Im")
plt.legend(loc="upper left")
plt.title("c")
plt.show()

# d
plt.plot(t, np.exp(-0.2 * t) * np.cos(3*np.pi*t), label="Re")
plt.plot(t, np.exp(-0.2 * t) * np.sin(3*np.pi*t), label="Im")
plt.legend(loc="upper left")
plt.title("d")
plt.show()