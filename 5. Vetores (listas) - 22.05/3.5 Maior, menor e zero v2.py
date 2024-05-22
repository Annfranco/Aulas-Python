import os

os.system("cls||clear")

numeros = []

while True:
    numero = int(input("Informe o número: "))
    if numero == 0:
        break
    numeros.append(numero)

maiorNumero = max(numeros)
menorNumero = min(numeros)
    
for i, numero in enumerate(numeros):
    print(f"{i + 1}º Número: {numero}")

print(f"Maior número: {maiorNumero}")
print(f"Menor número: {menorNumero}")