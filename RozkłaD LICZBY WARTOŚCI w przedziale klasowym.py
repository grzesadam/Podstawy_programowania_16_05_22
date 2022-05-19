import numpy as np
import matplotlib.pyplot as plt
import math


rng = np.random.default_rng()
n = 100
# number of numbers
m = 10
# number of function calls
a = -10
# edge min
b = 10
# edge max
k = 21
# number of class_interval


def number_generator(a, b, n):
    distribution = np.random.uniform(a, b, n)

    return distribution


def class_interval(a, b, k):
    bins = np.linspace(a, b, k)
    return bins


distribution = number_generator(a, b, n)
bins = class_interval(a, b, k)
arr_of_zeros = np.zeros((10, k - 1))


def matrix(m):
    for i in range(m):
        y = number_generator(a, b, n)
        h, _ = np.histogram(y, bins=bins)
        arr_of_zeros[i] += h
    c = np.vstack(arr_of_zeros)
    s = c.T
    return s


s = matrix(m)

co = math.ceil((k - 1) / 4)
# number of rows


fig, ax = plt.subplots(nrows=co, ncols=4, sharex='col', sharey='row', figsize=(7, 7), dpi=300, squeeze=True)
fig.suptitle('Histogram of the values for each column')

ax = ax.ravel()

for idx, axi in enumerate(ax):
    bins1 =np.linspace(0,max(s[idx]),len([i for i in s[idx] if i!=1]))
    axi.hist(s[idx],bins=bins1)
    plt.xlabel('number')
    plt.ylabel('numbers of number')

plt.tight_layout()
plt.show()
