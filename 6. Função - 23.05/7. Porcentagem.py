import os 

def logoSenai():
    os.system("cls||clear")
    print("=== ============ ===")
    print("=== SENAI | FIEB ===")
    print("=== ============ ===")

def inflacionar(preco):
    novoPreco = 0
    if preco < 100:
        novoPreco = preco * 1.0
    else:
        novoPreco = preco * 1.2
    return novoPreco

logoSenai()
preco = float(input("Informe o preço: "))

precoAtual = inflacionar(preco)

logoSenai()
print(f"Preço novo: {precoAtual}")



