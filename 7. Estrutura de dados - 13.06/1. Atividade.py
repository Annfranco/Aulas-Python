import os
from dataclasses import dataclass

os.system("cls || clear")

QUANTIDADE_DE_LIVROS = 2

@dataclass
class Livro:
    titulo: str
    autor: str
    numero_paginas: int
    preco: float

livros = []

for i in range(QUANTIDADE_DE_LIVROS):
    livro = Livro(
        titulo = input("\nInforme o Título do Livro: "),
        autor = input("Informe o Autor: "),
        numero_paginas = int(input("Informe a quantidade de páginas: ")),
        preco = float(input("Informe o preço do livro: "))
    )
    livros.append(livro)

os.system("clear")
for i in livros:
    print(f"\nTítulo do Livro: {i.titulo}")
    print(f"Autor: {i.autor}")
    print(f"Número de Páginas: {i.numero_paginas}")
    print(f"Preço do Livro: {i.preco:.2}")