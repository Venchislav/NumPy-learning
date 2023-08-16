import numpy as np


a = np.array([1, 2, 3, 4, 5, 6])
a.fill(0)
print(a)

print(np.zeros(5))

a = np.array([[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]])
print(a.flatten())  # flattens array. From multidimensional to 1d arr

b = np.array([7, 8, 9, 10, 11, 12])
a = np.array([1, 2, 3, 4, 5, 6])
print(np.concatenate((a, b)))  # [ 1  2  3  4  5  6  7  8  9 10 11 12]


