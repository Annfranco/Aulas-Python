#salvar usuario e senha em arquivo txt
from tkinter import messagebox

def guardar (usuario, senha):
    with open("dados.txt", "a") as arquivo:
        arquivo.write(f"{usuario},{senha}\n")
    messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")
  