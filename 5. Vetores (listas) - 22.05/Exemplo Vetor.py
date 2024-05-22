import os

os.system("cls||clear")

# Criando uma Lista / Vetor.
notas = []

for i in range(3):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)

for i in range(3):
    print(f"Nota: {notas[i]}")