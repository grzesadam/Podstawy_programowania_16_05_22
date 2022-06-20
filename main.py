import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()
N = 10000
a = 0
b = 5
K = 10 #liczba wykresów i kolumn
m = 5000 #liczba wywołań i wierszy



def wywolanie(m):
    bins = np.linspace(a, b, K + 1, endpoint=True)
    c = rng.uniform(low=a, high=b, size=N)
    first_hist, _ = np.histogram(c, bins)
    for i in range(m - 1):
        c = rng.uniform(a, b, N)
        second_hist, _ = np.histogram(c, bins)
        first_hist = np.vstack([first_hist,second_hist])
    return first_hist

d = wywolanie(m).T
print(d)

if K > 4:
    fig , axs = plt.subplots((K -1) // 5 + 1, 5, figsize=(15, 3 * ((K -1) // 5 + 1)))
for i in range(K):
    x = (i - 1) // 5
    y = i % 5
    label = f'Deviation: {np.std(d[i]):.3f}\naverage: {np.mean(d[i])}'
    axs[x, y].hist(d[i], label=label, bins='auto')
    axs[x, y].legend(loc='upper right', fontsize= 7)
# for idx, axi in enumerate(axs):
#     axs.hist(d[idx])

plt.show()
