import numpy as np
import matplotlib.pyplot as plt
img = np.zeros((5, 5))
img[1:4, 1:4] = 1
print(img)
img[4:6, 4:6] = 0
plt.imshow(img)
plt.axis('off')
plt.show()