import numpy as np
from numpy import random
import matplotlib.pyplot as plt

# a = int(input('A='))
# b = int(input('B='))
# n = int(input('N='))
# k = int(input('K='))
# m = int(input('M='))

a = 0
b = 1
n = 1000
k = 9
m = 4

bins = np.linspace(float(a), float(b), num=int(k+1))
rng = np.random.default_rng()

vals = []
z = []

for _ in range(m):
    hist_vals, bins = np.histogram(rng.uniform(a, b, n), k)
    z.append(hist_vals)

mattrix = np.array(z).T
print(mattrix)

f, c = plt.subplots(2, 2)
c = c.ravel()
q = a-(b-a)/k

for idx, cx in enumerate(c):
    q += (b-a)/k
    p = 0
    cx.hist(mattrix[:, idx])
    cx.set_title('from ' + str(round(q, 2)) + ' too ' + str(round((q + (b-a)/k), 2)))
    for i in range(m):
        p += mattrix[idx, i]
    p = p/m
    cx.set_xlabel('average value ' + str(round(p, 2)))

    cx.set_ylabel('6')

plt.tight_layout()
plt.show()
