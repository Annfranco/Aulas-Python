import os

os.system("cls || clear")

# Constante.
QUANTIDADE_ALUNOS = 2

# Vetor.
nomes = []
idades = []

# Solicitando dados.
for i in range(QUANTIDADE_ALUNOS):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))

nomes.append(nome)
idades.append(idade)

# Mostrando dados.
# len = descobre qual é o tamanho do vetor
for i in range(len(nomes)):
    print(f"Nome: {nomes[i]}")
    print(f"Idade: {idades[i]}")