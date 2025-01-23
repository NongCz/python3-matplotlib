import numpy as np

points = np.loadtxt("csv_data/points.csv", delimiter=",")  
distances = np.loadtxt("csv_data/distances.csv", delimiter=",")  

print("Points array:")
print(points)

print("\nDistances array:")
print(distances)
