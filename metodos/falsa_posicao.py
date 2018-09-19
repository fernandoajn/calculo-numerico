import math

print("Método da Falsa Posição")

def funcao(x):
    fx = math.exp(-x**2+1)+math.sin(x**2)-x
    return fx

print("Qual o intervalo [a,b] da raiz e a precisão e?")
a =float(input("Digite a: "))
b =float(input("Digite b: "))
e =float(input("Digite e: "))
i = 0

while True:
    i+=1
    fxa=funcao(a)
    fxb=funcao(b)
    x=(a*fxb-b*fxa)/(fxb-fxa)
    fx=funcao(x)
    if abs(fxa) < e:
        x=a
        break
    elif abs(fxb) < e:
        x=b
        break
    elif abs(fx) < e:
        break
    elif fxa*fx<0:
        b=x
    elif fxa*fx >0:
        a=x
    elif b-a<e:
        x=(b+a)/2

print("Raiz =",x)
print("Iterações = ",i)