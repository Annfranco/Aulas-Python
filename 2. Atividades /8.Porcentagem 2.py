import os

os.system("cls || clear")

quantidadeMorango = int(input("Quantidade Morangos: "))
quantidadeMacas = int(input("Quantidade de Maçãs: "))

if quantidadeMorango <= 5:
    precoMorango = quantidadeMorango * 2.5
elif quantidadeMorango > 5:
    precoMorango = quantidadeMorango * 2.2

if quantidadeMacas <= 5:
    precoMacas = quantidadeMacas * 1.8
elif quantidadeMacas > 5:
    precoMacas = quantidadeMacas * 1.5

precoTotal = precoMorango + precoMacas
quantidadeFrutas = quantidadeMorango + quantidadeMacas

if quantidadeFrutas > 8 or precoTotal > 25:
    desconto = precoTotal * 0.1
    valorPago =precoTotal - desconto

    print(f"Quantidade Morangos: {quantidadeMorango}")
    print(f"Preço Morangos: {precoMorango}")
    print(f"Quantidade Maçãs: {quantidadeMacas}")
    print(f"Preço Maçãs: {precoMacas}")
    print(f"Preço Total: {precoTotal}")
    print(f"Quantidade de Frutas: {quantidadeFrutas}")
    print(f"Valor desconto: {desconto:.2f}")
    print(f"Valor pago: {valorPago}")
else:
    valorPago = precoTotal
    print(f"Quantidade Morangos: {quantidadeMorango}")
    print(f"Preço Morangos: {precoMorango}")
    print(f"Quantidade Maçãs: {quantidadeMacas}")
    print(f"Preço Maçãs: {precoMacas}")
    print(f"Preço Total: {precoTotal}")
    print(f"Quantidade de Frutas: {quantidadeFrutas}")
    print(f"Valor pago: {valorPago}")