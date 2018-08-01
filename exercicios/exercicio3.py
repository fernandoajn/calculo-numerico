# Numeros primos
n = input("Entre com um numero positivo: ")

while n<=0:
    n = input("Apenas numeros positivos! Tente novamente: ")

d = 2

while d<n:
    if n%d==0:
        print n,("eh divisivel por"),d
        break
    else:
        d = d+1
        if d==n:
            print n,("eh primo")