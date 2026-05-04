import numpy as np
# Arithmetic operations on arrays
arr1 = np.array([1,2,3])
print(arr1 + 1) # [2 3 4]
print(arr1 - 2) # [-1 0 1]
print(arr1 * 2) # [2 4 6] 
print(arr1 / 2) # [0.5 1.  1.5]
print(arr1 ** 2) # [1 4 9]

# Universal functions (ufuncs)
arr2 = np.array([4,5,6])
print(np.sqrt(arr2))
print(np.round(arr2))
print(np.floor(arr2))
print(np.ceil(arr2))
print(np.pi)

# vectorized operations

raddi = np.array([1,2,3])
print(np.pi * raddi ** 2)

# elementwise operations

array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

print(array1 + array2) # [5 7 9]
print(array1 - array2) # [-3 -3 -3]
print(array1 * array2) # [4 10 18]
print(array1 / array2) # [0.25 0.4 0.5]
print(array1 ** array2) # [1 32 729]

# comparison operations
scores = np.array([85, 90, 78, 92, 88])
print(scores > 90)
for score in scores:
    if score > 90:
        print("Excellent!: ", score)
    elif score < 80:
        print("Needs improvement.: ", score)
    else:
        print("Good job!: ", score)