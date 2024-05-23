import os 

os.system("cls||clear")

# Função sem retorno.
def logoSenai():
    os.system("cls||clear")
    print("=== Senai ===")

# Função para calcular.
def mostrar_tabuada(numero):
    for i in range(10):
        print(f"{numero} x {i+1} = {numero * (i+1)}")

# Solicitando dados.
logoSenai()
numero = int(input("Informe um número: "))

logoSenai()
mostrar_tabuada(numero)


