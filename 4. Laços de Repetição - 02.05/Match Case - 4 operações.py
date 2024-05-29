import os

os.system("cls||clear")

# False = 0
resultado = False

a = int(input("Digite primeiro número: "))
operador = input("Digite um operador (+, -, * e /): ") 
b = int(input("Digite segundo número: "))

match(operador):
    case '+':
        resultado = a + b
    case '-':
        resultado = a - b
    case '*': 
        resultado = a * b
    case '/':
        resultado = a / b
    case _:
        print("Operador Inválido!Informe novamente. ")
                
print(f"Resultado: {resultado}")