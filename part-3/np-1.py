import numpy as np


a = np.array([1, 3, 0], float)
b = np.array([0, 3, 2], float)

print(a > b)
print(a < b)
print(a == b)
print(a > 1)

print(np.any(a))  # returns True if any element is True
print(np.all(a))  # returns True if all elements are True

print(np.logical_and(a > 0, a < 3))  # similar to if statement with and
print(np.logical_not(a > 0))  # similar to if statement with not
print(np.logical_or(a > 0, a < 3))  # similar to if statement with not


