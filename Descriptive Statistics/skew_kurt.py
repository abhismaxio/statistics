import numpy as np
from scipy.stats import skew, kurtosis # type: ignore

# Dataset
data = [2, 3, 4, 5, 100]

# Calculate Skewness
data_skewness = skew(data)

# Calculate Kurtosis
data_kurtosis = kurtosis(data, fisher=False)  # fisher=False gives Pearson kurtosis (adds 3)

# Results
print(f"Skewness: {data_skewness}")
print(f"Kurtosis: {data_kurtosis}")
