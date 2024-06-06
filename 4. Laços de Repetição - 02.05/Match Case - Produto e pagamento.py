import os

os.system("cls||clear")

print("Forma de Pagamento.")
print("1. Pagamento à vista.")
print("2. Pagamento à prazo.")

while True:
    forma_de_pagamento = int(input("Informe a opção desejada: "))

    match(forma_de_pagamento):
        case 1:
            print("Valor do Produto: R$ 100,00")
            print("Forma de Pagamento: à vista.")
            print("Valor do Desconto: R$ 10,00")
            print("Total a pagar: R$ 90,00")
            break
        case 2:
            print("Valor do Produto: R$ 100,00")
            print("Forma de Pagamento: à prazo.")
            print("Quantidade de Parcelas: 6")
            print("Valor por parcela: R$ 16,66")
            print("Total a pagar: R$ 100,00")
            break
        case _:
            print(f"Opção Inválida.")
            os.system("clear")
