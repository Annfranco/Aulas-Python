import os

os.system("cls||clear")

print("Código |     Prato      | Valor")
print("   1   |    Picanha     | R$ 25,00")
print("   2   |    Lasanha     | R$ 20,00")
print("   3   |   Strogonoff   | R$ 18,00")
print("   4   | Bife Acebolado | R$ 15,00")
print("   5   |   Pão com Ovo  | R$ 5,00")

resultado = 0

while True:
    opcao = int(input("Informe a opção desejada do menu: "))
    
    match(opcao):
        case 1:
            resultado = "Picanha - R$ 25,00"
            break
        case 2:
            resultado = "Lasanha - R$ 20,00"
            break
        case 3:
            resultado = "Strogonoff - R$ 18,00"
            break
        case 4:
            resultado = "Bife Acebolado - R$ 15,00"
            break
        case 5:
            resultado = "Pão com Ovo - R$ 5,00"
            break
        case _:
            resultado = "Opção Inválida."

print(f"Opção: {resultado}")
