
import sys


def main():
    i = True
    estoque = {}
    while i is True:
        produto = str(input("Nome do produto: "))
        preco = float(input("Preço: "))
        quant = int(input("Quantidade:"))
        if produto == '-1' or preco == -1 or quant == -1:
            break
        else:
            estoque[produto] = [preco, quant]

    print(estoque)


print(main())
