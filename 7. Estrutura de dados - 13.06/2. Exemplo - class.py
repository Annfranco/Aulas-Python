import os
from dataclasses import dataclass

os.system("cls || clear")

# Constante.
QUANTIDADE_ALUNOS = 2

# Classe.
@dataclass
class Aluno:
    nome: str
    idade: int
    altura: float
    peso: float

alunos = []

# Solicitando dados.
for i in range(QUANTIDADE_ALUNOS):
    nome_do_aluno = input("\nDigite seu nome: ")
    idade_do_aluno = int(input("Digite sua idade: "))
    altura_do_aluno = float(input("Digite sua altura: "))
    peso_do_aluno = float(input("Digite seu peso: "))

    aluno = Aluno(nome = nome_do_aluno, idade = idade_do_aluno, altura = altura_do_aluno, peso = peso_do_aluno)
    alunos.append(aluno)

# Mostrando dados.
"""for i in alunos:
        print(f"Nome: {i.nome})
        print(f"Idade: {i.idade})"""

os.system("clear")
for aluno in alunos:
    print(f"\nNome: {aluno.nome}")
    print(f"Idade: {aluno.idade}")
    print(f"Altura: {aluno.altura} metros")
    print(f"Peso: {aluno.peso} quilogramas")