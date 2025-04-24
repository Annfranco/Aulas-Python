#entrada de dados
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
print(f"{nome} tem {idade} anos e pesa {peso:.2f} kg.")

#colocar uma variavel dentro do input
nome = input("Digite seu nome: ")
idade = int(input(f"Digite a idade de {nome}: "))
print(f"{nome} tem {idade} anos de idade.")
