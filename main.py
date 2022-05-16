import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()


def generator():
    return rng.uniform(0, 1, 30)


m = 5
bin = 6


def wywolanie(n):
    a = generator()
    for b in range(n + 1):
        print(np.array(a))


z = wywolanie(5)

