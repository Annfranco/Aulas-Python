import os

os.system("cls || clear")

class Pet:
    def __init__(self, nome:str, idade:int, raca:str, porte:str, alimentacao:str):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.porte = porte
        self.alimentacao = alimentacao

QUANTIDADE_DE_PETS = 2
pets = []

for i in range(QUANTIDADE_DE_PETS):
    nome = input("\nInforme o nome: ")
    idade = int(input("Informe a idade do pet: "))
    raca = input("Informe a raça: ")
    porte = input("Informe o porte do pet: ")
    alimentacao = input("Informe a alimentação: ")
    pets.append(Pet(nome, idade, raca, porte, alimentacao))

for i in pets:
    print(f"\nNome do pet: {i.nome}")
    print(f"Idade do pet: {i.idade}")
    print(f"Raça do pet: {i.raca}")
    print(f"Porte do pet: {i.porte}")
    print(f"Alimentação do pet {i.alimentacao}")