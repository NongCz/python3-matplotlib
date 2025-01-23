import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 50)

y1 = x**2
y2 = x * np.sin(2 * x)
y3 = np.arctan(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y1, label="f(x) = x^2", color="green", linestyle="-", marker="o")  
plt.plot(x, y2, label="f(x) = x * sin(2x)", color="red", linestyle="--", marker="s")  
plt.plot(x, y3, label="f(x) = arctan(x)", color="purple", linestyle=":", marker="^")  

plt.title("Graphs of Functions with Custom Styles")
plt.xlabel("x-axis")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)

plt.show()