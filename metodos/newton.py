from numpy.polynomial import Polynomial as P
from numpy import polynomial

print("Interpolação de Newton")

pontos = []
k = 0
while True:
    k += 1
    while True:
        print("Digite as coordenadas do ", k, "º ponto separados por espaço:", end="\nf para finalizar \n")
        l = input()  
        if l == "f".lower():  
            break
        l = l.split()  
        if len(l) == 2: 
            break
        else:
            print("Entrada inválida, tente novamente!")
    if l == "f".lower():
        break
    for i in range(len(l)):
        l[i] = float(l[i])
    pontos.append(l)

l = []
for i in range(len(pontos)):
    l.append(pontos[i][1])
tabela = []  
tabela.append(l)
for i in range(len(pontos) - 1):
    l = []  
    for j in range(len(pontos) - i - 1):        
        dif = (tabela[i][j + 1] - tabela[i][j]) / (pontos[j + 1 + i][0] - pontos[j][0])
        l.append(dif)
    tabela.append(l)  
difdiv = []  
for i in range(len(tabela)):
    difdiv.append(tabela[i][0])
somatorio = 0
for i in range(1, len(pontos)):
    produtorio = 1
    for k in range(i):  
        produtorio *= (P([-pontos[k][0], 1])) 
    somatorio += difdiv[i] * produtorio
Pn = difdiv[0] + somatorio
funcao = list(Pn)  

texto = ""
for i in range(len(funcao)):
    if funcao[i] == 0:
        continue
    elif i == 0:
        texto += str(funcao[i])
    else:
        texto += " + " + str(funcao[i])
        texto += ("*x^%o" % (i))
print("Pn(x) :")
print(texto)
s = input(
    "Deseja calcular Pn(x) dado um valor de x? \n [S/N]").lower() 
if s == "s":
    print("Pn(x) em qual ponto?")
    p = float(input())
    print("Pn(%a) é igual a %a" % (p, Pn(p)))
print("Raízes de Pn(x): ", polynomial.polynomial.polyroots(list(Pn)))
s = input(
    "Encontrar os valores de x dado um valor de Pn(x)? \n [S/N]")  
if s == "s":
    print("Valores de x para qual valor de Pn(x)")
    p = float(input())
    print("para Pn(x)=%a temos: " % p, polynomial.polynomial.polyroots(list(Pn - P([p]))),
          "Obs: Se houver, j = raiz de menos 1")
print("(x,Pn(x))")
for i in range(len(pontos)):
    print("(%a,%a)" % (pontos[i][0], round(Pn(pontos[i][0]), 4)))