import numpy as np
import matplotlib.pyplot as plt

a = 2
b = 123
N = 1000
M = 100
K = 12


def matrix():
    hists = []
    bins = np.linspace(a, b, K + 1)
    for i in range(M):
        data = np.random.uniform(a, b, N)
        hist = np.histogram(data, bins)[0]
        hists.append(hist)
    return hists, bins


def plots():
    num_of_cols = 4
    num_of_rows = 3
    array = np.array(hist_data)
    fig, axs = plt.subplots(num_of_rows, num_of_cols)
    for i in range(num_of_rows):
        for j in range(num_of_cols):
            hist, bins = np.histogram(array[:, num_of_cols * i + j])
            axs[i, j].bar(bins[:-1], hist, label=bins)
            axs[i, j].set_ylabel('number')
            axs[i, j].set_xlabel('bins')
    fig.legend(loc='upper left', fontsize='x-small')
    plt.show()



hist_data, bins_data = matrix()
plots()