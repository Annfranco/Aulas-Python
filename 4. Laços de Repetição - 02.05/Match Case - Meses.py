import os

os.system("cls||clear")

resultado = 0

while True:
    mes = int(input("Escolha uma opção: "))

    match(mes):
        case 1:
            resultado = "Janeiro"
            break
        case 2:
            resultado = "Fevereiro"
            break
        case 3:
            resultado = "Março"
            break
        case 4:
            resultado = "Abril"
            break
        case 5:
            resultado = "Maio"
            break
        case 6:
            resultado = "Junho"
            break
        case 7:
            resultado = "Julho"
            break
        case 8: 
            resultado = "Agosto"
            break
        case 9:
            resultado = "Setembro"
            break
        case 10:
            resultado = "Outubro"
            break
        case 11:
            resultado = "Novembro"
            break
        case 12:
            resultado = "Dezembro"
            break
        case _:
            input("Opção Inválida.")
            os.system("clear")

print(f"Mês: {resultado}")