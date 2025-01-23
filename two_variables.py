import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)

f1 = X * Y
f2 = X**2 + Y**2
f3 = np.sin(3 * X) * Y

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, f1, cmap='viridis', edgecolor='k', alpha=0.8)
ax.set_title("Graph of f(x, y) = x * y")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("f(x, y)")
plt.show()

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, f2, cmap='plasma', edgecolor='k', alpha=0.8)
ax.set_title("Graph of f(x, y) = x^2 + y^2")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("f(x, y)")
plt.show()

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, f3, cmap='cividis', edgecolor='k', alpha=0.8)
ax.set_title("Graph of f(x, y) = sin(3x) * y")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("f(x, y)")
plt.show()
