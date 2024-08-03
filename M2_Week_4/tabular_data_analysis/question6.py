# Question 6
import numpy as np
import pandas as pd
from compute_correlation_cofficient import compute_correlation_cofficient

data = pd.read_csv ("advertising.csv")

features = ['TV', 'Radio', 'Newspaper']

for feature_1 in features:
    for feature_2 in features:
        correlation_value = compute_correlation_cofficient(data[feature_1], data[feature_2])
        print(f"Correlation between {feature_1} and {feature_2}: {round(correlation_value, 2)}")

# Answer: D