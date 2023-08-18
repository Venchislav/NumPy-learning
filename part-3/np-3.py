import numpy as np

a = np.array([[0, 1], [2, 3]], float)
b = np.array([[1, 2, 3], [4, 5, 6]])
print(np.dot(a, b))  # multiplication of matrix

a = np.array([1, 4, 0], float)
b = np.array([2, 2, 1], float)
print(np.outer(a, b))
print(np.inner(a, b))
print(np.cross(a, b))

a = np.array([[0, 1], [2, 3]], float)
b = np.array([[1, 2, 3], [4, 5, 6]])

print(a @ b)  # matrix multiplication in python without numpy
