import os

os.system("cls||clear")

contadorNotas = 0
soma = 0

while True:
    print("=== Menu ===")
    print("S - Inserir mais uma nota;")
    print("P - Ver quantas notas foram inseridas;")
    print("N - Calcular a média aritmética das notas informadas.")
    
    nota = float(input(f"Digite uma nota: "))
    resposta = resposta.upper()
    opcao = input("Digite uma opção: ")

    contadorNotas += 1
    soma += nota
    
    if opcao == "S":
        resposta = input(f"Deseja inserir mais uma nota? ")
        nota = float(input(f"Digite uma nota: "))
    if opcao == "P":
         print(f"Quantidade de notas inseridas: {contadorNotas}")
    if opcao == "N":
        media = soma / contadorNotas
        break

print(f"Média: {media}")