from tkinter import *
menu_inicial = Tk()
menu_inicial.title ("Sistema de Controle de Estoque")
# menu_inicial.geometry("500x500") #define o tamanho da janela
menu_inicial.geometry("500x500+500+100") #define o tamanho e a posição da janela
# menu_inicial.minsize("350, 350") #define o tamanho minimo da janela 
# menu_inicial.maxsize("500, 500") #define o tamanho maximo da janela
menu_inicial.resizable(False, False) #define se a janela pode ser redimensionado
# menu_inicial.state("iconic") #começa minimizada
# menu_inicial.state("zoomed") #começa maximizada
# menu_inicial.configure(bg="pink") #define a cor de fundo
menu_inicial['bg'] = "purple" #define cor de fundo
menu_inicial.iconbitmap("icone.ico") #define o icone




menu_inicial.mainloop()