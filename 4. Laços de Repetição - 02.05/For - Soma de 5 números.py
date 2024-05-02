import os

os.system("cls||clear")

soma = 0

for i in range(5):
    numero = int(input(f"Informe o {i+1}º números: "))
    soma = soma + numero

"""for i in range(1, 6):
    numero = int(input(f"Informe o {i}º números: "))
    soma = soma + numero"""

print(f"Soma: {soma}")