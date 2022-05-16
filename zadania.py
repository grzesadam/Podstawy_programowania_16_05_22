import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng()
b = np.linspace(1, 10, 10)


def generate(N, a, b):
    return rng.uniform(low=a, high=b, size=N)


def summarize(N, M):
    result = np.zeros((N, M))
    for i in range(N):
        result += generate(M, 0, 10)
    return result


def histogram(f):
    plt.hist(f)
    plt.show()


def function(M, K):
    a = np.zeros((M, K))
    for i in range(M):
        a[i - 1] = generate(M, 0, 10)
    return a


def multihist(ff):
    a = []
    for i in range(len(ff)):
        a.append(ff[:, i - 1])
    plt.subplot()
    for f in a:
        histogram(10, f)
    plt.show()


y = summarize(100, 100)
x = histogram(y)
print(x)
