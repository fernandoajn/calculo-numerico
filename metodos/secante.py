def Secante(x0,x1,tol,N,f):

    print(0,x0,x1)
    i=1
    h= 0.00001   #dx para calcular a derivada de f(x)
    while i<=N:
        x= x1 - (x1-x0)*f(x1)/(f(x1)-f(x0))  

        print(i,x)
        if abs(x-x1)<tol:
            return x
        i=i + 1
        x0=x1    # redefinir x0
        x1=x     #redefinir x1

    print(' %d iteracoes' %N)
    
import math     
    
    
f=lambda x: x**3 + 4*x**2 - 10
x0=1
x1=2
tol=0.0001
N=20
    
x=Secante(x0,x1,tol,N,f)
print()
print('Solucao: ',x)