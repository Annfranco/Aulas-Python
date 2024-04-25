import os 

os.system("cls || clear")

login = input("Login: ")
senha = input("Senha: ")

if login == "abcde" and senha == "1234":
    print("Bem-Vindo!")
else:
    print("Login ou senha inválido.")