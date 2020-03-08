import numpy as np
import scipy.interpolate as spi

x = np.linspace(-2 * np.pi, 2 * np.pi, num=11)
f = lambda x: np.sin(x) + 0.5 * x
print(f(x))

tck = spi.splrep(x, f(x), k=1)
print(tck)

pp = spi.PPoly.from_spline(tck)
print(pp.c.T)

iy = spi.splev(x, tck)

print(np.allclose(f(x), iy))
print(np.sum((f(x) - iy) ** 2) / len(x))
