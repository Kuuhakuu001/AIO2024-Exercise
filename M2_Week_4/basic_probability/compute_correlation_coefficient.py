# Question 4
import numpy as np


def compute_correlation_cofficient (X , Y ):
    N = len(X)
    numerator = 0
    denominator = 0
    numerator = N * np.sum(X * Y) - np.sum(X) * np.sum(Y)
    denominator = np.sqrt(N * np.sum(X**2) - np.sum(X)**2) * np.sqrt(N * np.sum(Y**2) - np.sum(Y)**2)

    return np.round(numerator / denominator , 2)


X = np.asarray([ -2 , -5 , -11 , 6 , 4 , 15 , 9])
Y = np.asarray([4 , 25 , 121 , 36 , 16 , 225 , 81])
print ("Correlation: ", compute_correlation_cofficient(X , Y))

# Answer: D