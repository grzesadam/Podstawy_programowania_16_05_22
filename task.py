import numpy as np
import matplotlib.pyplot as plt

a = 2
b = 123
N = 1000
M = 100
K = 10


def matrix():
    hists = []
    bins = np.linspace(a, b, K + 1)
    for i in range(M):
        data = np.random.uniform(a, b, N)
        hist = np.histogram(data, bins)[0]
        hists.append(hist)
    return hists, bins


def plots():
    array = np.array(hist_data)
    for i in range(K):
        hist, bins = np.histogram(array[:,i])
        plt.bar(bins[:-1], hist)
        plt.show()


hist_data, bins_data = matrix()
plots()