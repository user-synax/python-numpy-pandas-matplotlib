import numpy as np

# single-dimensional array
arr1 = np.array([1,2,3,4,5])
print(arr1)

# multi-dimensional array
arr2 = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(arr2)

arr = np.array([
                [1,2,3], 
                [4,5,6], 
                [7,8,9], 
                [10,11,12]])

# important attributes of arrays
print(arr)
print(arr.ndim)
print(arr.shape)
print(arr[0])