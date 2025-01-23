import numpy as np
import matplotlib.pyplot as plt

# Define the x range
x = np.linspace(-10, 10, 1000)

# Define the functions
y1 = x**2
y2 = x * np.sin(2 * x)
y3 = np.arctan(x)

# Plot the functions
plt.figure(figsize=(10, 6))
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

# Show the plot
plt.show()
