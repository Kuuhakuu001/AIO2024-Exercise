# Question 3
import numpy as np


def compute_mean(X):
    return sum(X) / len(X)


def compute_std(X):
    mean = compute_mean(X)
    variance = sum((x - mean) ** 2 for x in X) / len(X)
    return np.sqrt(variance)


X = [171 , 176 , 155 , 167 , 169 , 182]
print (compute_std(X))

# Answer: C