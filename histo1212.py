import numpy as np
from numpy import random
import matplotlib.pyplot as plt

n = int(input('N='))
m = int(input('M='))
r = int(input('dn='))
R = np.linspace(0.0, 2.0, num=int(r+1))
rng = np.random.default_rng()

vals = []
sum_of_vals = np.zeros(n)

for _ in range(m):
    vals = (rng.uniform(0, 1, n)-0.5)
    sum_of_vals += vals

E1 = 0
E2 = 0
q = 0

sum_of_vals *= 1/(m**0.5/(2*3**0.5))

for i in range(n):
    E1 += sum_of_vals[i]
    E2 += (sum_of_vals[i])**2

q = (E2/n - (E1/n)**2)**0.5
print(q)
plt.hist(sum_of_vals, bins='auto')
plt.show()
