import numpy as np
import matplotlib.pyplot as plt

values_for_hist = np.loadtxt("csv_data/values_for_hist.csv", delimiter=",")  

plt.figure(figsize=(8, 6))
plt.hist(values_for_hist, bins=20, color='lightcoral', edgecolor='black')

plt.title("Histogram of Real Numbers")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True, linestyle="--", alpha=0.6)

plt.show()
