import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)

y1 = x**2
y2 = x * np.sin(2 * x)
y3 = np.arctan(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y1, label="f(x) = x^2", color="green")  
plt.plot(x, y2, label="f(x) = x * sin(2x)", color="red")  
plt.plot(x, y3, label="f(x) = arctan(x)", color="purple")  

plt.title("Graphs of Functions")
plt.xlabel("x-axis")
plt.ylabel("f(x)")
plt.legend()

plt.show()