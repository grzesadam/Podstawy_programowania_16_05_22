import numpy as np
import matplotlib as plt

def matrix():
    a = 2
    b = 123
    N = 100
    M = 100
    K = 10
    row = []
    bins = np.linspace(a, b, K + 1)
    for i in range(M):
        data = np.random.uniform(a, b, N)
        hist = np.histogram(data, bins)[0]
        row.append(hist)
    print(np.array(row).shape)
matrix()
