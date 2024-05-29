import os

os.system("cls||clear")

dia_da_semana = 0
resultado = 0

while True:
    dia = int(input("Informe um dia da semana: "))

    match(dia):
        case 1:
            dia_da_semana = "Domingo"
            resultado = "Final de Semana."
            break
        case 2:
            dia_da_semana = "Segunda"
            resultado = "Dia útil."
            break
        case 3:
            dia_da_semana = "Terça"
            resultado = "Dia útil."
            break
        case 4:
            dia_da_semana = "Quarta"
            resultado = "Dia útil."
            break
        case 5:
            dia_da_semana = "Quinta"
            resultado = "Dia útil."
            break
        case 6:
            dia_da_semana = "Sexta"
            resultado = "Dia útil."
            break
        case 7:
            dia_da_semana = "Sábado"
            resultado = "Final de Semana."
            break
        case _:
            print("Número Inválido.")

print(f"Dia da Semana: {dia_da_semana}")
print(f"Resultado: {resultado}")