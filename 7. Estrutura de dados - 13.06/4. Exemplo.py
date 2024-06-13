import os 

os.system("cls||clear")

# self = passagem de parâmetros.
class Aluno:
    #def __init__(self, nome:str, idade:int):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

QUANTIDADE_ALUNOS = 2
alunos = []

for i in range(QUANTIDADE_ALUNOS):
    nome = input("\nDigite seu nome: ")
    idade = int(input("Digite sua idade: "))
    alunos.append(Aluno(nome,idade))

for i in alunos:
    print(f"\nNome: {i.nome}")
    print(f"Idade: {i.idade}")
    