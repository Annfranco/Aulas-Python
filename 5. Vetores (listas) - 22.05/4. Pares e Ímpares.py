import os

os.system("cls||clear")

QUANTIDADE_NUMEROS = 6
numeros = []
impares = 0
pares = 0 

for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Informe {i+1}º número: "))
    numeros.append(numero)

    if numero % 2 == 0:
       pares += 1
    else:
       impares += 1

for i, numero in enumerate(numeros):
    print(f"{i+1}º Números: {numero} ")

print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números impares: {impares}")
    
