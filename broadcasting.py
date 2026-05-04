import numpy as np

# Broadcasting allows operations to be performed on arrays of different shapes and sizes
# Example of broadcasting with different shapes
arr1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
arr2 = np.array([[1], [2], [3], [4]])
print(arr1.shape) # (4, 4)
print(arr2.shape) # (4, 1)

print(arr1 * arr2)

array1 = np.array([[1,2,3,4,5,6,7,8,9,10]])
array2 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
print(array1.shape) # (1, 10)
print(array2.shape) # (10, 1)

print(array1 - array2)