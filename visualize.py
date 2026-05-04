import numpy as np
import matplotlib.pyplot as plt

array1 = np.array([[1,2,3,4,5,6,7,8,9,10]])
array2 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])

result = array1 + array2

plt.imshow(result)
plt.colorbar()
plt.title("Broadcasting Result (Outer Sum)")
plt.xlabel("array1 (columns)")
plt.ylabel("array2 (rows)")
plt.show()

