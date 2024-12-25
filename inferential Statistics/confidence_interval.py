import numpy as np
from scipy.stats import sem, t

# Sample data
data = [23, 21, 25, 30, 28]

# Calculate the 95% CI
confidence = 0.95
mean = np.mean(data)
std_err = sem(data)
h = std_err * t.ppf((1 + confidence) / 2, len(data) - 1)
ci = (mean - h, mean + h)

print(f"95% Confidence Interval: {ci}")
