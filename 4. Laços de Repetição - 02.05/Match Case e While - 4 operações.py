import os

os.system("cls||clear")

# False = 0
resultado = False

while True :

    a = int(input("Digite primeiro número: "))
    operador = input("Digite um operador (+, -, * e /): ")
    b = int(input("Digite segundo número: "))

    match(operador):
        case '+':
            resultado = a + b
            break
        case '-':
            resultado = a - b
            break
        case '*': 
            resultado = a * b
            break
        case '/':
            resultado = a / b
            break
        case _:
           print("Operador Inválido!Informe novamente. ")
                
print(f"Resultado: {resultado}")