#salvar usuario e senha em arquivo txt

def guardar (usuario, senha):
    with open("dados.txt", "a") as arquivo:
        arquivo.write(f"{usuario},{senha}\n")
    print("Usuario e senha salvos com sucesso!")