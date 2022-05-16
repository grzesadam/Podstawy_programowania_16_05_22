import numpy as np
from numpy import random
import matplotlib.pyplot as plt

# n = int(input('N='))
# m = int(input('M='))
n = 20
m = 10
K = int(input('K='))

z = []

for _ in range(K):
    rng = np.random.default_rng()
    vals = []
    sum_of_vals = np.zeros(n)

    for _ in range(m):
        vals = (rng.uniform(0, 1, n) - 0.5)
        sum_of_vals += vals

    sum_of_vals *= 1 / (m ** 0.5 / (2 * 3 ** 0.5))

    z.append(sorted(sum_of_vals.tolist()))

A = np.array(z)
print(A)

def aretmetic(p):
    q = 0
    for j in range(K):
        q += A[p, j]
    return q

f, a = plt.subplots(3, 3)
a = a.ravel()
for idx, ax in enumerate(a):
    ax.hist(A[:, idx])
    ax.set_title(str(aretmetic(int(idx))))
plt.tight_layout()
plt.show()
