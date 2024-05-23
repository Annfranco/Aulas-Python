import os 

def logoSenai():
    os.system("cls||clear")
    print("=== Senai ===")

def calcular_media(n1, n2):
    resultado = (n1 + n2) / 2
    return resultado

logoSenai()
primeiroNumero = int(input("Informe o primeiro número: "))
logoSenai()
segundoNumero = int(input("Informe o segundo número: "))

media = calcular_media(primeiroNumero, segundoNumero)

print(f"Média: {media}")
