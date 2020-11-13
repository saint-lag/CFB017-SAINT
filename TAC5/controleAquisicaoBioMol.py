
import sys
from operacoesCompra import *

class controleAquisicaoBioMol():
	def __init__(self, estoque):
		self._estoque = estoque
		self._produtos = imprimeProdutos(self._estoque)
		self._quantidade = imprimeQuantidades(self._estoque)
		self._total = calculaTotalCompra(self._estoque)

	def __str__(self):
		return f'{self._total},\n{type(self._estoque)}'

def main():
    i = True
    estoque = {}
    while i is True:
        produto = str(input("Nome do produto: "))
        preco = float(input("Preço: "))
        quant = int(input("Quantidade:"))
        if produto == '-1' or preco == -1 or quant == -1:
            i = False
        else:
            estoque[produto] = [preco, quant]

    return estoque 
	

estoque = main()
compra = controleAquisicaoBioMol(estoque)