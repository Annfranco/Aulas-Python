#Formatação de saida de dados no Python

nome = "Monkey D. Luffy"
idade = 19
peso = 60.0

nome1 = "Angélina Bailarina"
idade1 = 14
peso1 = 46.0

nome2 = "Gwen Tennyson"
idade2 = 30
peso2 = 64.0

print("Bem vindo ao meu primeiro programa")

#forma antiga
print("%s tem %d anos e pesa %.2f kilos" % (nome, idade, peso))

#forma mais nova
print("{} tem {} anos e pesa {:.2f} kilos".format(nome1, idade1, peso1))

#forma mais fácil
print(f"{nome2} tem {idade2} anos e pesa {peso2:.2f} kilos")