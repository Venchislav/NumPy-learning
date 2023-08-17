import numpy as np


# matrix of size 1st arg with ones diagonally
n1 = np.identity(10, dtype=int)
print(n1)

# matrix of size 1st arg with ones diagonally from k column
n2 = np.eye(5, k=1, dtype=int)
print(n2)
