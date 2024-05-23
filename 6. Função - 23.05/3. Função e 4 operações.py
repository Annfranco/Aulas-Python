import os

def logoSenai():
    os.system("cls||clear")
    print("=== ===== ===")
    print("=== Senai ===")
    print("=== ===== ===")

def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    return n1 / n2

logoSenai()
primeiroNumero = int(input("Digite o primeiro número: "))
logoSenai()
segundoNumero = int(input("Digite o segundo número: "))

soma = somar(primeiroNumero, segundoNumero)
subtracao = subtrair(primeiroNumero, segundoNumero)
multiplicacao = multiplicar(primeiroNumero, segundoNumero)
divisao = dividir(primeiroNumero, segundoNumero)

print(f"Soma: {soma}")
print(f"Multiplicação: {multiplicacao}")
print(f"Subtração: {subtracao}")
print(f"Divisão: {divisao}")