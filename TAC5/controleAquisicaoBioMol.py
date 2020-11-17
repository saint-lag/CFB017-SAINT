
import sys
from operacoesCompra import *


class compraDeProdutos():
	def __init__(self, estoque):
		self._estoque = estoque
		self._produtos = imprimeProdutos(self._estoque)
		self._quantidade = imprimeQuantidades(self._estoque)
		#self._total = calculaTotalCompra(self._estoque)

	def __str__(self):
		return f'[Estoque]: {self._estoque},\n[Produtos]: {self._produtos}'


def main():
	i = True
	estoque = {}
	while i:
		produto = str(input("Nome do produto: "))
		preco = float(input("Preço: "))
		quant = int(input("Quantidade:"))
		if produto == '-1' or preco == -1 or quant == -1:
			i = False
		else:
			estoque[produto] = [preco, quant]




	return estoque 
	

estoque = main()
compra = compraDeProdutos(estoque)


