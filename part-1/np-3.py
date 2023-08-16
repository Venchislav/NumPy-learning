import numpy as np


a = np.array(range(10), float)
print(a)

print(np.shape(a))
print(a.reshape((5, 2)))
print(a.reshape((10, 1)))

a = a.reshape((1, 10))
print(np.shape(a))
