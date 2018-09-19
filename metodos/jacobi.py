import numpy as np

print("Método de Gauss Jacobi")

def max(A):
    max=A[0][0]
    for i in range(len(A)):
        for j in range(len(A[0])):
            if abs(A[i][j]) >max:
                max=abs(A[i][j])
    return max

while True:
    n =(input("Tamanho da Matriz:\n"))
    if n.isdigit():
        n=int(n)
        break
    else:
        print("Entrada inválida, tente novamente!")
e=float(input("Qual a precisão desejada?"))

A=np.zeros((n,n))
B=np.zeros((n, 1))
C=np.zeros((n,n))
G=np.zeros((n,1))
X=np.zeros((n, 1))

for i in range(n):
        while True:
            print("Digite os elementos da linha ", i + 1, " da matriz A separados por espaço:", end="")
            l = input().split()
            if len(l) == n:
                break
            else:
                print("Entrada inválida, tente novamente!")
        for j in range(len(l)):
            A[i][j] = float(l[j])

while True:
    print("Digite os elementos do vetor B de Ax=b separados por espaço:", end=" ")
    l = input().split()
    if len(l) == n:
        break
    else:
        print("Entrada inválida, tente novamente!")
for k in range(len(l)):
    B[k][0]=float(l[k])


while True:
    print("Digite os elementos do vetor inicial X0 separados por espaço:", end=" ")
    l = input().split()
    if len(l) == n:
        break
    else:
        print("Entrada inválida, tente novamente!")
for k in range(len(l)):
    X[k][0]=float(l[k])

D=np.zeros((n,1))
for i in range(n):
    soma=0
    l = list(range(n))
    l.remove(i) 
    for j in l:
        soma+=A[i][j]
    D[i][0]=abs(soma/A[i][i])

if max(D) <1:
    print("A matriz atende ao critério de convergência")
else:
    print("A matriz não atende ao critério de convergencia mas não necessarimente não convergirá")

for i in range(n):
    for j in range(n):
        if i == j:
            C[i][j]=0
        else:
            if A[i][i]!=0:
                C[i][j]=-A[i][j]/A[i][i]
            else:
                print("Divisão por zero!")
                break
    if A[i][i]!=0:
        G[i][0]=B[i][0]/A[i][i]

ni=0
while True:
    ni+=1
    Xk=np.dot(C,X) + G
    d=max(Xk-X)/max(Xk)
    if d <e:
        break
    else:
        X=Xk

print("Matriz A")
for i in range(n):
    print(A[i])


print("Matriz C")
for i in range(n):
    print(C[i])

print("Vetor G")
for i in range(n):
    print(G[i])

print('solução do sistema linear dado:')
for i in range(n):
    print('x%o = ' % (i + 1), Xk[i][0])
print("Numero de iterações = ",ni)