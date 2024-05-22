import os

os.system("cls||clear")

numeros = []

while True:
    numero = int(input("Informe o número: "))
    numeros.append(numero)

    if numero > 0:
        maiorNumero = max(numeros)
        menorNumero = min(numeros)
    else:
        numero == 0
        break

for i, numero in enumerate(numeros):
    print(f"{i + 1}º Número: {numero}")

print(f"Maior número: {maiorNumero}")
print(f"Menor número: {menorNumero}")