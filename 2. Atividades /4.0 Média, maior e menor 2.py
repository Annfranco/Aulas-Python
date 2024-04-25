import os

os.system("cls || clear")

primeiroValor = float(input("Informe 1º Valor: "))
segundoValor = float(input("Informe 1º Valor: "))

produto = primeiroValor * segundoValor
soma = primeiroValor + segundoValor
media = soma / 2

maiorValor = max(primeiroValor, segundoValor)
menorValor = min(primeiroValor, segundoValor)

os.system("cls || clear")
print(f"1º Valor: {primeiroValor}")
print(f"2º Valor: {segundoValor}")
print(f"Produto: {produto}")
print(f"Soma: {soma}")
print(f"Média: {media}")
print(f"Maior Valor: {maiorValor}")
print(f"Menor Valor: {menorValor}")