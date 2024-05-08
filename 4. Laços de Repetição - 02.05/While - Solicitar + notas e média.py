import os 

os.system("cls||clear")

contadorNotas = 0
soma = 0

while True:
    nota = float(input(f"Digite uma nota: "))
    resposta = input(f"Deseja inserir mais uma nota? ")
    
    #Converte o texto em maiúsculo.
    resposta = resposta.upper()

    contadorNotas += 1
    soma += nota
    
    if resposta != "N":
        break
    
media = soma / contadorNotas

print(f"Média: {media}")