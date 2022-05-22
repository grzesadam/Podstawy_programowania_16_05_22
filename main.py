import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

rng = np.random.default_rng()
K = 20
N = 1000
a = 0
b = 1
m = 12


# 1
def rozklad(a, b, N):
    dist = rng.uniform(a, b, N)
    return dist


# 2
def histogram(rozklad, K):
    histogram, bins = np.histogram(rozklad, K)
    return histogram


# 3
def suma_rozkladu(m, K):
    func1 = rozklad(a, b, N)
    func2 = (histogram(func1, K))
    sum_of_hist = func2
    for _ in range(m - 1):
        func1 = rozklad(a, b, N)
        func2 = (histogram(func1, K))
        sum_of_hist = np.vstack((sum_of_hist, func2))
    return sum_of_hist

wynik = suma_rozkladu(m, K)
print(wynik)

# 4
def srednia(i):
    suma = wynik.sum(axis=0)
    return suma[i] / K

# 4
def odchylenie(i):
    suma = 0
    for j in range(m):
        suma += (wynik[j][i] - srednia(i)) ** 2
    return sqrt(suma / (K - 1))

# 4, 5
def wykres():
    fig, axs = plt.subplots(4, 5, figsize=(6, 6), layout='constrained')
    func1 = rozklad(a, b, N)
    func2 = (histogram(func1, K))
    p = 0
    q = 0
    for i in range(K):
        axs[p][q].hist(wynik[:, i], label="Kolumna" + str(i))
        axs[p][q].legend(loc='upper right')
        axs[p][q].set_title("Średnia " + str(srednia(i)) + " \ns=" + str(odchylenie(i)))
        axs[p][q].set(xlabel='wartości', ylabel='ilość wartości')
        if q == 4:
            p += 1
            q = 0
        else:
            q += 1

    plt.show()

wykres()
