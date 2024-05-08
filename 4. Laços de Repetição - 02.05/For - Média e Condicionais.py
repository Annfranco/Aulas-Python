import os 

os.system("cls||clear")

soma = 0
media = 0

for i in range(1,4):
    notas = int(input(f"Informe sua {i}º Nota: "))
    soma += notas
    media = soma/ i

print(f"Média: {media}")

if media >= 7:
    print("Aprovado!")
elif media < 4:
    print("Reprovado.")
else:
    print("Em Recuperação.")