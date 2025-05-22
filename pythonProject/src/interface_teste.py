#SISTEMA DE CONTROLE DE ESTOQUE SIMPLES
import negocios_estoque

def menu():
    while True:
        print ("\n ------ MEU ESTOQUE ------")
        print ("1 - Adicionar item ")
        print ("2 - Listar estoque")
        print ("3 - Alterar item")
        print ("4 - Excluir item")
        print ("0 - Sair")
        opcao = input ("Digite sua opcao: ")
        if opcao == "1":
            print("Adicionando item")
            negocios_estoque.adicionar_item()

        elif opcao == "2":
            print("Listando estoque")
            negocios_estoque.listar_estoque()

        elif opcao == "3":
            print("Alterando item")
            negocios_estoque.alterar_item()

        elif opcao == "4":
            print("Excluir item")
            negocios_estoque.excluir_item()
        elif opcao == "0":
            break
        else:
            print("Opcao invalida")



menu()