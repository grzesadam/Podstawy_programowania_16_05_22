import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()
n = 10000
m = 100
a=-10
b=10

def generator(n,a,b):

    sums_of_vals = np.random.uniform(a,b,n)

    return sums_of_vals

def przedzial_klasowy(n, sums_of_vals):
    k=int(n**0.5)
    xmax=max(sums_of_vals)
    xmin=min(sums_of_vals)
    x=xmax-xmin
    bins=np.linspace(a,b,k)
    print(k)
    return(bins)



o=np.vstack([generator(n,a,b) for i in range(m) ])


generator(n,a,b)

sums_of_vals=generator(n,a,b)
przedzial_klasowy(n, sums_of_vals)
bins=przedzial_klasowy(n, sums_of_vals)
h=np.histogram(o,bins=bins)
w=h[1]
c=h[0]
matrix=np.vstack(w)
matrix1=np.concatenate(w,c)
print(matrix1)