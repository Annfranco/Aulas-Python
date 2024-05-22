import os

os.system("cls||clear")

QUANTIDADE_NOTAS = 3

totalNotas = []
# soma = 0 

for i in range(QUANTIDADE_NOTAS):
    notas = float(input(f"Informe sua {i + 1}º nota:"))
    totalNotas.append(notas)
    # soma = soma + notas

# media = soma / QUANTIDADE_NOTAS
media = sum(totalNotas) / QUANTIDADE_NOTAS

for i in range(QUANTIDADE_NOTAS):
    print(f"Notas: {totalNotas[i]}")

#ForEach
"""for nota in totalNotas:
    print(f"Nota: {totalNotas}")"""

print(f"Média: {media}")
