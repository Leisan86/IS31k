import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-100, 10)

y = 5 + np.exp(x) - np.sin(x) + x

fig, ax = plt.subplots()
ax.plot(x, y)

plt.show()
