import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()

# Podawane na początku wartości:
# N = liość liczb losowych
# [a, b] = przedział liczb losowych
# K = wartości przedziałów klasowych (bins), według których tworzony będzie histogram

N = 100  # ilosć liczb losowych
A = 0  # początek przedizału
B = 1  # koniec przedziału
K = 5  # liczba kolumn
M = 5  # liczba wierszy


def polecenie_3(m):
    bins = np.linspace(A, B, K + 1, endpoint=True)
    for i in range(m):
        if i == 0:
            generated = rng.uniform(low=A, high=B, size=N)
            result, _ = np.histogram(generated, bins)
        else:
            generated = rng.uniform(low=A, high=B, size=N)
            histogram, _ = np.histogram(generated, bins)
            result = np.vstack([result, histogram])

    return result

matrix = polecenie_3(M)

fig, axs = plt.subplots(M, K)
for i in range(K):
    axs[0,i].hist(matrix[i, :])


plt.show()
