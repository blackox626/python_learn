import numpy as np

a = np.arange(24).reshape((2, 2, 2, 3))
print(a)

print(a.T)
print(a.T.shape)

print(len(a))

b = np.reshape(a, (3, 8))
print(b)

print(dir(b))
