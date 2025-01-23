import numpy as np
import matplotlib.pyplot as plt

points = np.loadtxt("csv_data/points.csv", delimiter=",")  
distances = np.loadtxt("csv_data/distances.csv", delimiter=",")  

plt.figure(figsize=(10, 6))
scatter = plt.scatter(points[:, 0], points[:, 1], c=distances, cmap="viridis", edgecolor="k")

plt.colorbar(scatter, label="Distance")

plt.title("Scatter Plot of Points Colored by Distance")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.grid(True, linestyle="--", alpha=0.6)

plt.show()
