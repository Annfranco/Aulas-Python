import os

os.system("cls || clear")

nomeProduto = input("Produto: ")
quantidadeAdquirida = int(input("Quantidade do Produto: "))
precoUnitario = float(input("Preço do Produto: "))

total = quantidadeAdquirida * precoUnitario

if quantidadeAdquirida <= 5:
    desconto = total * 0.02
elif quantidadeAdquirida > 10:
    desconto = total * 0.05
else:
    desconto = total * 0.03

precoTotal = total - desconto

os.system("cls || clear")
print(f"Produto: {nomeProduto}")
print(f"Quantidade de Produto: {quantidadeAdquirida}")
print(f"Preço do Produto: {precoUnitario}")
print(f"Preço Total: {precoTotal}")