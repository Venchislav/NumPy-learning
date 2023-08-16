import numpy as np
# shape

n_arr = np.array([[1, 2, 3, 4, 9], [1, 2, 3, 4, 5]])
print(np.shape(n_arr))

n_arr = np.array([[1, 2, 3, 4, 9]])
print(np.shape(n_arr))

n_arr = np.array([1, 2, 3, 4, 5], float)
print(n_arr.dtype)

n_arr = np.array([[1, 2, 3, 4, 9], [1, 2, 3, 4, 5]], float)
print(n_arr.dtype)
print(n_arr)

print(len(n_arr))  # 2
x = [[1, 2, 3, 4, 9], [1, 2, 3, 4, 5]]
print(len(x))  # 2

print(9 in n_arr)  # True
print(9 in x)  # False
