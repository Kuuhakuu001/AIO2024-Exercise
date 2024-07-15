
import numpy as np
arr = np.arange(0, 10, 1)
print(arr)
# Q1: Answer A

import numpy as np
arr1 = np.ones((3, 3)) > 0
arr2 = np.ones((3, 3), dtype=bool)
arr3 = np.full((3, 3), fill_value=True, dtype=bool)
print(arr1)
print(arr2)
print(arr3)
# Q2: Answer D

import numpy as np
arr = np.arange(0, 10)
print(arr[arr % 2 == 1])
# Q3: Answer A

import numpy as np
arr = np.arange(0, 10)
arr[arr%2 == 1] = -1
print(arr)
# Q4: Answer B

import numpy as np
arr = np.arange(10)
arr_2d = arr.reshape(2, -1)
print(arr_2d)
# Q5: Answer B

import numpy as np
arr1 = np.arange(10).reshape(2, -1)
arr2 = np.repeat(1, 10).reshape(2, -1)
c = np.concatenate([arr1, arr2], axis=0)
print("Result: \n", c)
# Q6: Answer A

import numpy as np
arr1 = np.arange(10).reshape(2, -1)
arr2 = np.repeat(1, 10).reshape(2, -1)
c = np.concatenate([arr1, arr2], axis=1)
print("C = ", c)
# Q7: Answer C

import numpy as np
arr = np.array([1, 2, 3])
print(np.repeat(arr, 3))
print(np.tile(arr, 3))
# Q8: Answer A

import numpy as np
a = np.array([2,6,1,9,10,3,27])
index = np.where((a >= 5) & (a <= 10))
print(a[index])
# Q9: Answer C

import numpy as np

def maxx(x, y):
    """Get the maximum of two items"""
    if x >= y:
        return x
    else:
        return y

a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])

pair_max = np.vectorize(maxx, otypes=[float])
print(pair_max(a, b))
# Q10: Answer C

import numpy as np

a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
print("Result ", np.where(a<b, b, a))