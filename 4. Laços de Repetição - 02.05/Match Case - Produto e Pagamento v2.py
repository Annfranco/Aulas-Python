import os

os.system("cls||clear")

print("Forma de Pagamento.")
print("1. Pagamento à vista.")
print("2. Pagamento à prazo.")

while True:
    forma_de_pagamento = int(input("Informe a opção desejada: "))
    valor_produto = float(input("Valor do Produto: R$ "))

    match(forma_de_pagamento):
        case 1:
            print("Forma de Pagamento: à vista.")
            print("Valor desconto: R$ 10,00.")
            desconto = valor_produto * 0.1
            valor_a_pagar = valor_produto - desconto
            print(f"Total a pagar: {valor_a_pagar:.2f}")
            break
        case 2:
            parcelas = int(input("Informe a quantidade de parcelas: "))
            print("Forma de pagamento: à prazo.")
            print(f"Quantidade parcelas: {parcelas}")
            parcela = valor_produto / parcelas
            print(f"Valor por parcela: R$ {parcela:.2f}")
            print("Total à prazo: R$ 100,00")
            break
        case _:
            print(f"Opção Inválida.")
            os.system("clear")