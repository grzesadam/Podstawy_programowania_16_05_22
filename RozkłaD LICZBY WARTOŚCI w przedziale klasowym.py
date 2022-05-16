import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()
n = 1000
m = 10
a=-10
b=10

def generator(n,a,b):

    sums_of_vals = np.zeros(n)

    for _ in range(m):
        sums_of_vals += rng.uniform(0,1, n) - 0.5
    sums_of_vals *= 1 /(b-a)
    return sums_of_vals

def przedzial_klasowy(n, sums_of_vals):
    k=int(n**0.5)
    xmax=max(sums_of_vals)
    xmin=min(sums_of_vals)
    x=xmax-xmin
    bins=np.linspace(a,b,k)
    print(k)
    return(bins)


for i in range(m):
    generator(n,a,b)
    print(generator(n,a,b))





generator(n,a,b)

sums_of_vals=generator(n,a,b)
przedzial_klasowy(n, sums_of_vals)
