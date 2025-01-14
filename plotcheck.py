import numpy as np
import matplotlib.pyplot as plt

# Generate random data
data = np.random.randn(1000)  # 1000 random numbers from a normal distribution

# Plot
plt.hist(data, bins=30, color='blue', alpha=0.7)
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()


df = pd.DataFrame(data)
print(df.head(5))
