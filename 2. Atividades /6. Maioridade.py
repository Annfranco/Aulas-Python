import os

os.system("cls || clear")

idade = int(input("Digite sua idade: "))

if idade <= 18 and idade >= 65:
    print("Voto é obrigatório.")
else:
    print("Voto é não obrigatório.")