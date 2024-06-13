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
    aluno = Aluno( 
        nome = input("\nDigite seu nome: "),
        idade = int(input("Digite sua idade: ")),
        altura = float(input("Digite sua altura: ")),
        peso = float(input("Digite seu peso: "))
    )
    alunos.append(aluno)

# Mostrando dados.
os.system("clear")
for aluno in alunos:
    print(f"\nNome: {aluno.nome}")
    print(f"Idade: {aluno.idade}")
    print(f"Altura: {aluno.altura} metros")
    print(f"Peso: {aluno.peso} quilogramas")