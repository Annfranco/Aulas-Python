import os
os.system("cls|| clear")

nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))
primeiraNota = int(input("Informe sua 1º nota: "))
segundaNota = int(input("Informe sua 2º nota: "))

soma = primeiraNota + segundaNota
media = soma / 2

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"1º Nota: {primeiraNota}")
print(f"2º Nota: {segundaNota}")
print(f"Média: {media}")