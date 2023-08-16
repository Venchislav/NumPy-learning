import numpy as np


a = np.array(range(99))
# print(a)
c = a.copy()
# print(c)

a = a.tolist()
print(type(a))  # turns np ndarray to python list object

a = np.array([1, 2, 3], float)
s = a.tobytes()
print(s)  # b'\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x08@'

print(np.frombuffer(s))  # [1. 2. 3.]
