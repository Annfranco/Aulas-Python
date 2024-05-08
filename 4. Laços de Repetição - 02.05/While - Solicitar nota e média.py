import os 

os.system("cls||clear")

QUANTIDADE_NOTAS = 2
soma = 0

for i in range(QUANTIDADE_NOTAS):
    while True: 
        nota = float(input(f"Digite a {i+1}º (entre 0 e 10): "))

        if nota < 0 or nota > 10:
         print(f"Nota inválida. A nota deve estar entre 0 e 10. Por Favor, tente novamente.")
        else:
            soma += nota
        break

media = soma / QUANTIDADE_NOTAS


print(f"Média: {media}")