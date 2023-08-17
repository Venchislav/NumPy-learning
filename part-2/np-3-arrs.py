import numpy as np


n1 = np.array([1, 2, 3, 4, 5])
n2 = np.arange(5)
print(n1 + n2)  # [1 3 5 7 9]

# code above is similar to print([sum(i) for i in zip(n1, n2)])
# P.S we have to apply tolist() to np arrays before

print(n1 * n2)  # [ 0  2  6 12 20]

a = np.array([[1, 2], [3, 4]], float)
b = np.array([[2, 0], [1, 3]], float)
print(a * b)  # but it's not mathematical matrix multiplication

a = np.array([[1, 2], [3, 4], [5, 6]], float)
b = np.array([-1, 3], float)

print(a + b)

"""
[[0. 5.]
 [2. 7.]
 [4. 9.]]
"""


