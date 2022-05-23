import numpy as np
from numpy import random
import matplotlib.pyplot as plt

a = int(input('A='))
b = int(input('B='))
n = int(input('N='))
K = int(input('dn='))

R = np.linspace(float(a), float(b), num=int(K+1))
rng = np.random.default_rng()

vals = (rng.uniform(a, b, n))

plt.hist(vals, bins=R)
plt.show()
