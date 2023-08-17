import numpy as np


n1 = np.arange(5, dtype=float)
print(n1)  # [0. 1. 2. 3. 4.]

# np.ones is similar to np.zeros
n2 = np.ones((2, 3), dtype=int)
print(n2)

# we even have zeros_like method

n3 = np.zeros_like(n1)  # takes shape of another array, and fills it with zeros (np also has ones_like method)
print(n3)


