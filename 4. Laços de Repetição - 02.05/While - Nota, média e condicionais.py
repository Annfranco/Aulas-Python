import os 

os.system("cls||clear")

QUANTIDADE_NOTAS = 3
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

if media >= 7:
   resultado = "Aprovado!"
elif media >= 5:
   resultado = "Em Recuperação."
else:
   resultado = "Reprovado."

print(f"Média: {media}")
print(f"Resultado: {resultado}")