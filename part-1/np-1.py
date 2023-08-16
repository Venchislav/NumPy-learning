import numpy as np

# array in numpy

n_arr = np.array([1, 2, 3, 4, 5, 6], float)
print(n_arr)
print([type(i) for i in n_arr])


# we can apply slices

print(n_arr[1:7:2])
print(n_arr[:2])
print(n_arr[::-1])
x = n_arr[:]
print(x)


n_arr_sub = np.array([[1, 2, 3], [1, 2, 3]], float)
print(n_arr_sub)
print(n_arr_sub[0, 1:3])  # [2. 3.]
