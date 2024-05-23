import os

#Função sem retorno
def logoSenai():
    print("=== Senai ===")
    print("=== ===== ===")

#Solicitando dados para o usuário.
logoSenai()
nome = input("Digite seu nome: ")

logoSenai()
idade = int(input("Digite sua idade: "))

logoSenai()
peso = float(input("Digite seu peso: "))

#Exibindo dados para o usuário.
logoSenai()
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Peso: {peso}")