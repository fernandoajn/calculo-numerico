<<<<<<< HEAD
import math
print("Método da Bisseção")
def funcao(x):          
        fx=(1/48)*(693*x**6-945*x**4+315*x**2-15)         
        return fx
print("Qual o intervalo [a,b] da raiz e a precisão e?")
a=float(input("Entre com o inicio do intervalo: "))         
b=float(input("Entre com o fim do intervalo: "))         
e=float(input("Entre com a precisão desejada: "))         
i=0         
k=(math.log10(b-a)-math.log10(e)/math.log10(2))         
k=math.ceil(k)         
print("Numero estimado de iterações: ",k)
if b-a<e:         
    x=(a+b)/2
    print("Raiz:", x)
else:
    while True:
        i+=1        
        x=(a+b)/2    
        fxa=funcao(a)
        fxb=funcao(b)
        fx=funcao(x) 
        if fx==0.0:
            print("Raiz: ",x)
            break
        elif fxa*fx<0: 
            b=x
        elif fxa*fx>0:
            a=x
        if b-a<e: 
            x = (a + b) / 2
            print("Raiz:", x)
            print("Numero de iterações = ",i)
            break
=======
# Author: @fernandoajn
import math

print("Método da Bissecção")
print("--------------------")

def funcao(x):
    eq = input("Digite a equação: <notação em python> ")
    f = eval(eq) # validar função
    return f

a = input("Ponto A: ")
b = input("Ponto B: ")
E = input("Tolerancia: ")

i = 0 # iteração

while True:
    i += 1
    fa = funcao(a)
    fb = funcao(b)
    x = (a*fb-b*fa)/(fb-fa)
    fx = funcao(x)

    if abs(fa) < e:
        x = a
        break
    elif abs(fb) < e:
        x = b
        break
    elif abs(fx) < e:
        break
    elif (fa*fx)<0
        b = x
    elif (fa*fx)>0:
        a = x
    elif (b-a)<e:
        x = (b+a)/2

print("Raiz =",x)
print("Iteracoes = ", i) 
>>>>>>> 2e1745576668e5032ee32f87cede67ad89e7a11c
