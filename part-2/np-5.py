import numpy as np

n1 = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]], float)
print(sum(n1))  # [3. 6. 9.]
print(n1.sum())  # 18.0

print(n1.prod())  # there's no built-in prod function for product of iterable in python

n = np.array([1, 9, 3])
print(n.mean())  # 4.333333333333333

print(n.min())  # returns min elem
print(n.max())  # returns max elem

print(n.argmin())  # returns index of min elem
print(n.argmax())  # returns index of max elem

a = np.array([6, 2, 5, -1, 0], float)
a = a.clip(0, 5)
print(a)  # [5. 2. 5. 0. 0.]

print(np.unique(a))

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a.T)

"""
[[ 1  5  9]
 [ 2  6 10]
 [ 3  7 11]
 [ 4  8 12]]
"""
