import os

os.system("cls||clear")

nome = input("Infome seu Nome: ")
sexo = input("Informe seu Sexo (M ou F): ")
estadoCivil = input("Informe seu Estado Civil: ")

sexo = sexo.lower()
estadoCivil = estadoCivil.lower()

if sexo == "f" and estadoCivil == "casada":
    tempoDeCasada = int(input("Informe seu Tempo de Casada: "))
    
os.system("cls||clear")

print(f"Nome: {nome}")

if sexo == "f":
    print(f"Sexo: Feminino")
else:
    print(f"Sexo: Masculino")
    
print(f"Estado Civil: {estadoCivil}")

if sexo == "f" and estadoCivil == "casada":
    print(f"Tempo de Casada: {tempoDeCasada}")