# Algarismos romanos
n = input("Entre com um numero: ")

while n<=0:
    n = input("Apenas numeros positivos! Tente novamente: ")

rom = ""

if n>=1000:
    rom = rom+"M"
    n = n-1000
if n>=500:
    rom = rom+"D"
    n = n-500
if n>=100:
    rom = rom+"C"
    n = n-100
if n>=50:
    rom = rom+"L"
    n = n-50
if n>=10:
    rom = rom+"X"
    n = n-10
if n>=9:
    rom = rom+"IX"
    n = n-9
if n>=5:
    rom = rom+"V"
    n = n-5
if n>=4:
    rom = rom+"IV"
    n = n-4
while n>=1:
    rom = rom+"I"
    n = n-1

print rom