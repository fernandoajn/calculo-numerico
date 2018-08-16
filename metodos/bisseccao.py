# Author: @ffaneto
import math

print("Método da Bissecção")
print("--------------------")

eq = input("Digite a equação: <notação em python> ")
f = eval(eq) # validar função

a = input("Ponto A: ")
b = input("Ponto B: ")
E = input("Tolerancia: ")

i = 1 # iteração