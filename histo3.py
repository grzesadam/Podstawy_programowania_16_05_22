import numpy as np
from numpy import random
import matplotlib.pyplot as plt

n = int(input('N = '))
m = int(input('M = '))
a = int(input('A = '))
b = int(input('B = '))
k = int(input('K = '))

x = 0
bins = np.linspace(a, b, k+1, endpoint=True)

rng = np.random.default_rng()
vals = sorted(rng.uniform(a, b, n))
plt.hist(vals, bins)
plt.show()
