#interface usando gridLayout do Tkinter
from tkinter import *
import model
from tkinter import messagebox

def sair():
    resposta = messagebox.askyesno("Sair", "Você realmente deseja sair?")
    if resposta:
        menu_inicial.destroy()

def guardar_usuario():
    usuario = txtUsuario.get()
    senha = txtSenha.get()
    model.guardar(usuario, senha)  # Chama a função guardar do módulo model
    # print(usuario)
    # print(senha)

menu_inicial = Tk()
menu_inicial.title("Tela login")
menu_inicial.geometry("400x300+500+150")
menu_inicial.resizable(False, False)
# Criação de widgets

#rotulos
label1 = Label(menu_inicial, text="Usuário:", fg= "#000000", font= "Arial 12 bold")
label1.grid(row=0, column=0, padx=10, pady=10)
label2 = Label(menu_inicial, text="Senha:", fg= "#000000", font= "Arial 12 bold")
label2.grid(row=1, column=0, padx=10, pady=10, sticky=W)

#entrada (caixas de texto)
txtUsuario = Entry(menu_inicial, width=30, font="Arial 12")
txtUsuario.grid(row=0, column=1, padx=10, pady=10)
txtSenha = Entry(menu_inicial, width=30, font="Arial 12", show="*")
txtSenha.grid(row=1, column=1, padx=10, pady=10)

#botões
btEntrar = Button(menu_inicial, text = "Entrar", width=10, font="Arial 12 bold", 
                  bg="#008000", fg="#FFFFFF", command=guardar_usuario)
btEntrar.grid(row=2, column=1, pady=20, sticky=W)

btCancelar = Button(menu_inicial, text = "Cancelar", width=10, font="Arial 12 bold", 
                    bg="#FF0000", fg="#FFFFFF", command=sair)
btCancelar.grid(row=2, column=1, pady=10, sticky=E)

menu_inicial.mainloop()