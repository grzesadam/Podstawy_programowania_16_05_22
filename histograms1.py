import numpy as np
from numpy import random
import matplotlib.pyplot as plt

# n = int(input('N='))
# m = int(input('M='))
n = 4
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
x = []

for i in range(K):
    x.append(i)

def aretmetic(p):
    q = 0
    for j in range(K):
        q += A[p, j]
    return q

fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, A[:, 0])
axs[0, 0].set_title('1 ' + str(aretmetic(0)))
axs[1, 0].plot(x, A[:, 1])
axs[1, 0].set_title('2 ' + str(aretmetic(1)))
axs[1, 0].sharex(axs[0, 0])
axs[0, 1].plot(x, A[:, 2])
axs[0, 1].set_title('3 ' + str(aretmetic(2)))
axs[1, 1].plot(x, A[:, 3])
axs[1, 1].set_title('4 ' + str(aretmetic(3)))
fig.tight_layout()
plt.show()
