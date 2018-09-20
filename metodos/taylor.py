import sympy as sy
import numpy as np
from sympy.functions import sin,cos
import matplotlib.pyplot as plt

plt.style.use("ggplot")

x = sy.Symbol('x')
f = sin(x)

def fatorial(n):
    if n <= 0:
        return 1
    else:
        return n*fatorial(n-1)

def taylor(function,x0,n):
    i = 0
    p = 0
    while i <= n:
        p = p + (function.diff(x,i).subs(x,x0))/(fatorial(i))*(x-x0)**i
        i += 1
    return p

def plot():
    x_lims = [-5,5]
    x1 = np.linspace(x_lims[0],x_lims[1],800)
    y1 = []
    for j in range(1,10,2):
        func = taylor(f,0,j)
        print('n='+str(j),func)
        for k in x1:
            y1.append(func.subs(x,k))
        plt.plot(x1,y1,label='req '+str(j))
        y1 = []
    plt.plot(x1,np.sin(x1),label='seno de x')
    plt.xlim(x_lims)
    plt.ylim([-5,5])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.title('Aproximacao de Taylor')
    plt.show()

plot()