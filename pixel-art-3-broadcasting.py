import numpy as np
import matplotlib.pyplot as plt

x = np.arange(16)
y = np.arange(16)[:, None]

pattern = (x + y) % 2

plt.imshow(pattern)
plt.axis('off')
plt.show()