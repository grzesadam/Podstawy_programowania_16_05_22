import numpy as np
import matplotlib.pyplot as plt
import math

rng = np.random.default_rng()
n = 100
# number of numbers
m = 100
# number of function calls
a = -10
# edge min
b = 10
# edge max
k = 20


# number of class_interval


def number_generator(a, b, n):
    distribution = np.random.uniform(a, b, n)

    return distribution


def class_interval(a, b, k):
    bins = np.linspace(a, b, k)
    return bins


distribution = number_generator(a, b, n)
bins = class_interval(a, b, k)
arr_of_zeros = np.zeros((m, k - 1))


def matrix(m):
    for i in range(m):
        y = number_generator(a, b, n)
        h, _ = np.histogram(y, bins=bins)
        arr_of_zeros[i] += h
    c = np.vstack(arr_of_zeros)
    s = c.T
    return s


h = matrix(m)
s = matrix(m)

co = int((k - 1) / 4)
print(co)


# number of rows


def historams(co, s):
    fig, ax = plt.subplots(nrows=co, ncols=4, sharex='col', sharey='row', figsize=(10, 10), dpi=300, squeeze=True)
    fig.suptitle('Histogram of the values for each column')
    ax = ax.ravel()
    bins1 = np.linspace(np.min(s), np.max(s), k)
    for x in bins1:
        print(x, end=' ')
    for idx, axi in enumerate(ax):
        print(bins1[idx])
        average = (max(s[idx]) + min(s[idx])) / 2
        standard_deviation = round((max(s[idx]) - min(s[idx])) / (2 * math.sqrt(3)), 1)

        labels = f'stdev={standard_deviation}\n av ={average}\n bin={round(bins1[idx],1)}'

        axi.hist(s[idx], bins=bins1, label=labels)
        axi.legend(loc='upper left')
        plt.xlabel('number')
        plt.ylabel('numbers of number')

    plt.show()


historams(co, s)
