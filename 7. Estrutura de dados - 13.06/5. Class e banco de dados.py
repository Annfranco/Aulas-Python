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

alunos = []

# Solicitando dados.
for i in range(QUANTIDADE_ALUNOS):
    aluno = Aluno(
        nome = input("Digite seu nome: "),
        idade = int(input("Digite sua idade: "))
    )
    alunos.append(aluno)

# Nome do arquivo.
arquivo = 'alunos.txt'

# Grava os dados no arquivo.
with open(arquivo, 'w') as arquivo:
    for aluno in alunos:
        arquivo.write(f"{aluno.nome},{aluno.idade}\n")

# Nome do arquivo
arquivoDeOrigem = 'alunos.txt'

# Lista para armazenar os alunos lidos.
listaAlunos = []

# Lê os dados do arquivo.
with open(arquivoDeOrigem, 'r') as arquivo:
    for linha in arquivo:
        nome, idade = linha.strip().split(',')
        listaAlunos.append(Aluno(nome=nome, idade=int(idade)))

# Exibe os dados.
print("Exibindo dados.")
for i in listaAlunos:
    print(f"Nome: {i.nome}")
    print(f"Idade: {i.idade}")

print(f"Dados Gravados com Sucesso.")