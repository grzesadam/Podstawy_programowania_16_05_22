import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng()
# K = np.linspace(1,10,10, dtype=10)
K=20
N=1000
a=0
b=1
m=12

def rozklad(a, b, N):
    dist = rng.uniform(a, b, N)
    return dist

def histogram(func1,K):
    histogram, bins=np.histogram(func1,K)
    return histogram

def suma_rozkladu(func2, m,K):
    sum_of_hist = np.zeros((m,K))
    for _ in range(m):
        sum_of_hist= np.vstack( func2)
    return sum_of_hist

func1=rozklad(a,b,N)
func2=(histogram(func1, K))



print(suma_rozkladu(func2,m,K))



