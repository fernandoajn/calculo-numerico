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
