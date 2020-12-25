import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z ** 2 + 1
x = np.linspace(-4 * np.pi, 4 * np.pi, 100)
y = 0.8*x-0.2
ax.plot(x, y, z, label='parametric curve')
ax.legend()

plt.show()