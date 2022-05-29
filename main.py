import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()

# Podawane na początku wartości:
# N = liość liczb losowych
# [a, b] = przedział liczb losowych
# K = wartości przedziałów klasowych (bins), według których tworzony będzie histogram

N = 10000  # ilosć liczb losowych
A = 0  # początek przedizału
B = 1  # koniec przedziału
K = 20  # liczba kolumn
M = 10000  # liczba wierszy


def polecenie_3(m):
    bins = np.linspace(A, B, K + 1, endpoint=True)
    generated = rng.uniform(low=A, high=B, size=N)
    result, _ = np.histogram(generated, bins)
    for _ in range(m - 1):
        generated = rng.uniform(low=A, high=B, size=N)
        histogram, _ = np.histogram(generated, bins)
        result = np.vstack([result, histogram])

    return result

matrix = polecenie_3(M)

# print(matrix)

histograms_array = matrix.T
# histograms_array = matrix

# print(histograms_array)


# print((K - 1) // 4 + 1)

if K > 4:
    fig, axs = plt.subplots((K - 1) // 4 + 1, 4)

    for i in range(K):
        x = (i - 1) // 4
        y = i % 4
        label = f"Deviation = {np.std(histograms_array[i])}\nAverage = {np.average(histograms_array[i])}"
        axs[x, y].hist(histograms_array[i], label=label)
        axs[x, y].legend(loc='upper left', fontsize=7)
else:
    fig, axs = plt.subplots(1, 4)

    for i in range(K):
        label = f"Deviation = {np.std(histograms_array[i])}\nAverage = {np.average(histograms_array[i])}"
        axs[i].hist(histograms_array[i], label=label)
        axs[i].legend(loc='upper left', fontsize=7)

plt.show()
