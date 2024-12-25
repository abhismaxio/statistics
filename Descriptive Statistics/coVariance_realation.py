import numpy as np

X=[2,4,6]
Y=[3,5,7]

cov_matrix = np.cov(X,X,bias=False)
covarance = cov_matrix[0,1]

correlation = np.corrcoef(X,Y)[0,1]

print("as",cov_matrix)
print("covarinace",covarance)
print("correaltion",correlation)