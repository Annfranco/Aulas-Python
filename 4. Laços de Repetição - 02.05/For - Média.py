import os

os.system("cls||clear")

soma = 0
media = 0

for i in range(1,5):
    notas = int(input(f"Informe sua {i}º Nota: "))
    soma = soma + notas
    media = soma / i

print(f"Média: {media}")