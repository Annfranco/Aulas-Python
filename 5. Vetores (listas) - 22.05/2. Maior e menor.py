import os
import sys

os.system("cls||clear")

QUANTIDADE_NUMEROS = 5

numeros = []

for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Informe {i + 1}º número: "))
    numeros.append(numero)

maiorNumero = max(numeros)
menorNumero = min(numeros)

for i, numero in enumerate(numeros):
    print(f"{i + 1}º Número: {numero}")

print(f"Maior número: {maiorNumero}")
print(f"Menor número: {menorNumero}")
