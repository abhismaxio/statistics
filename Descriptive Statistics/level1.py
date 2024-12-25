import numpy as np
from scipy.stats import skew, kurtosis # type: ignore
import matplotlib.pyplot as plt
print("NumPy and SciPy are successfully installed!")

data = [4, 8, 15, 16, 23, 42]

mean = np.mean(data)
print("mean: ",mean)
median = np.median(data)
print("median: ",median)
mode = max(set(data),key=data.count)
print("mode: ",mode)

range = np.max(data) -np.min(data)
print("range: ",range)
variance = np.var(data,ddof=1)
print("variance: ",variance)
std_dev = np.std(data,ddof=1)
print("standard deviation",std_dev)

q1 = np.percentile(data, 25)
q3 = np.percentile(data,75)
iqr = q3-q1
print(f"q1 is {q1} and q3 is {q3} and iqr is {iqr}")


data_skewness = skew(data)
print("data skewness: ",data_skewness)
data_kurtosis = kurtosis(data)
print("data kurtosis: ",data_kurtosis)

plt.hist(data,bins=5,color="skyblue",edgecolor='black')
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()