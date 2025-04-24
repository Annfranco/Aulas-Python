#estruturas condicionais

#verificar se o numero é positivo, negativo ou zero.

num = int(input("Insira um número: "))

if num > 0:
    print("O número é positivo.")
elif num < 0:
    print("O número é negativo.")
else:
    print("O número é Zero.")

#verificar se é vogal ou consoante
letra = input("\nInsira uma letra: ").lower()
if letra in "aeiou":
    print("É vogal.")
else:
    print("É consoante.")

#verificar ano bissexto
ano = int(input("\nInsira um ano: "))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"{ano} é bissexto.")
else:
    print(f"{ano} não é bissexto.")