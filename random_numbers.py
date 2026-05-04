import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(seed=1)
a = rng.integers(low=100, high=999, size=(10, 10))
print(a)
# print(rng.uniform(low=100, high=999, size=(10, 10)))

plt.title('Random Integers between 100 and 999')
plt.imshow(a)
plt.colorbar()
plt.show()
