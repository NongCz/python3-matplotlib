import numpy as np
import matplotlib.pyplot as plt

values_for_bars = np.loadtxt("csv_data/values_for_bars.csv", delimiter=",")  

unique_values, counts = np.unique(values_for_bars, return_counts=True)

plt.figure(figsize=(8, 6))
plt.bar(unique_values, counts, color='skyblue', edgecolor='black')

plt.title("Bar Plot of Value Frequencies")
plt.xlabel("Unique Values")
plt.ylabel("Frequency")
plt.grid(True, linestyle="--", alpha=0.6)

plt.show()