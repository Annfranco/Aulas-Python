import os 

os.system("cls || clear")

nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))
primeiraNota = float(input("Informe 1º Nota: "))
segundaNota = float(input("Informe 2º Nota: "))
terceiraNota = float(input("Informe 3º Nota: "))

media = (primeiraNota + segundaNota + terceiraNota) / 3

os.system("cls || clear")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Média: {media}")
      
if media >= 7:
    print("Aprovado!")
else:
    print("Reprovado.")