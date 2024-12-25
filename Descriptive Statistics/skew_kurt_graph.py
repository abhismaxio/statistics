import matplotlib.pyplot as plt
import seaborn as sns

data_right_skewed =[2,3,4,5,100]
data_normal =[3,4,5,6,10]
data_heavy_tails = [1,2,3,50,100]
sns.histplot(data_right_skewed, kde=True, color='red', label='Right Skewed')
sns.histplot(data_normal, kde=True, color="green",label ="nomral")
sns.histplot(data_heavy_tails, kde=True, color="yellow",label="heavy tails",)
plt.legend()
plt.title("Skewness and Kurtosis Visualization")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()