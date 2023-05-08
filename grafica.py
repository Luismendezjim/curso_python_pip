import matplotlib.pyplot as plt
import numpy as np
def graficar(x,y):
    plt.plot(x,y)
    plt.grid()
    plt.axhline(y=0, color='r', linewidth=0.8)
    plt.axvline(x=0, color='r', linewidth=0.8)
    plt.show()
    
N = 100 # N es la resolucion de una funcion
def f(x):
    return (2*x**7)-(x**4)+(3*x**2)+4

x = np.linspace(-10,10, num=N)
y = f(x)

plt.plot(x,y)
plt.grid()