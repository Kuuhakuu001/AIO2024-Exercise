# Question 2

import numpy as np


def compute_median(X):
    X = np.sort(X)
    print(X)
    N = len(X)
    median = 0
    if N % 2 == 1:
        median = X[N // 2]
    else:
        median = (X[(N // 2) - 1] + X[N // 2]) / 2
    return median


X = [1 , 5 , 4 , 4 , 9, 13]
print("Median: ", compute_median(X))

# Answer: B
