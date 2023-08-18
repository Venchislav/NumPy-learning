import numpy as np

a = np.array([[0, 1, 9], [3, 0, 8]], float)
print(a.nonzero())

a = np.array([0, np.NaN, np.Inf])

print(np.isnan(a))  # checks if elem is NaN (Not a Number)
print(np.isinf(a))  # checks if elem is Infinite

a = np.array([[0, 1], [2, 3]], float)
b = np.array([0, 0, 1], int)
print(a.take(b, axis=0))
