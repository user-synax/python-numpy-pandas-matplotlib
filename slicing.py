import numpy as np
# Slicing and indexing
arr = np.array([[1,2,3], 
                [4,5,6],
                [7,8,9],
                [10,11,12]])
# Basic slicing
print(arr[0]) # [1 2 3]
# Slicing with steps
print(arr[::2]) # [[ 1  2  3]
print(arr[::-1]) # [[10 11 12]]
print(arr[:,0]) # [ 1  4  7 10]
print(arr[1:3, 1:3]) # [[5 6]]