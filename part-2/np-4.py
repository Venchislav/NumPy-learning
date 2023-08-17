import numpy as np

n = np.arange(10)
print(np.sqrt(n))  # sqrt of each elem in np array

n = np.arange(1, 3, 0.3)

print(n)
print(np.floor(n))

print(np.ceil(n))

print(np.rint(n))

print(np.pi)
print(np.e)

n2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], float)

for (x, y, z) in n2:
    print(f'[{x}] [{y}] [{z}]')
