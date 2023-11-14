import numpy as np
import matplotlib.pyplot as plt

def f(k, x):
    return k * x * (1 - x)

def suitewo(k, x) :
    L = []
    y = x
    for i in range(1000):
        L.append(y)
        y = f(k, y)
    return L

def plot2(k, x):
    L = suitewo(k, x)
    print(L)
    plt.plot(L)

def plot1000(x):
    K = np.linspace(0,4,1000)
    X1000 = []
    for k in K:
        y = suitewo(k, x)[-1]
        X1000.append(y)
    fig, ax = plt.subplots()
    ax.scatter(K, X1000)

if __name__ == '__main__':
    plot1000(0.5)
    plt.show()