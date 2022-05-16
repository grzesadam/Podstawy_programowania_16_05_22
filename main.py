import numpy as np
from matplotlib import pyplot as plt
from math import ceil

"""
The file contains a basic implementation of the problem.
"""

N = 1000
a, b = 0., 1.
K = 10
M = 100


def generate_uniform_data(a, b, N):
    """
    Function returns an array of uniformly distributed data of size N from range (a, b).
    :param a: lower bound
    :param b: upper bound
    :param N: number of items
    :return: uniformly distributed data
    """
    return np.random.uniform(a, b, N)


def get_repeated_histogram(a, b, N, K, M):
    """
    Function returns an MxK array of M histograms, K bins each, calculated over M sets of synthetic, uniformly distributed data of size N from range (a, b).
    :param a: lower bound of data generation
    :param b: upper bound of data generation
    :param N: size of the generated data
    :param K: number of bins
    :param M: number of repeats (histograms)
    :return: MxK array of histograms and bins
    """
    bins = np.linspace(a, b, K + 1)
    histogram_matrix = \
        [np.histogram(generate_uniform_data(a, b, N),
                      bins=bins)[0]
         for _ in range(M)]
    return np.vstack(histogram_matrix), bins


def plot_histograms(histogram_matrix, bins):
    plots = histogram_matrix.shape[1]
    number_of_cols = 4
    number_of_rows = ceil(plots / number_of_cols)
    fig, axs = plt.subplots(number_of_rows, number_of_cols)
    for i in range(number_of_cols):
        for j in range(number_of_rows):
            try:
                current_bin = j * number_of_cols + i
                hist, b = np.histogram(histogram_matrix[:, current_bin])
                current_ax = axs[j, i]
                current_ax.bar(b[:-1], hist, width=1)
                current_ax.legend('adasda')
            except IndexError as ex:
                pass
    plt.show()


if __name__ == '__main__':
    histogram_matrix, bins = get_repeated_histogram(a, b, N, K, M)
    plot_histograms(histogram_matrix, bins)
    print("Problem solved.")
