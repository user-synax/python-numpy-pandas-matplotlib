import numpy as np
import matplotlib.pyplot as plt

img = np.zeros((16, 16, 3), dtype=np.uint8)

img[4:12, 4:12] = [255, 0, 0]

img[0, :] = [0, 0, 255]
img[-1, :] = [0, 0, 255]
img[:, 0] = [0, 0, 255]
img[:, -1] = [0, 0, 255]
print(img)
plt.imshow(img)
plt.axis('off')
plt.show()