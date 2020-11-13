


def imprimeProdutos(estoque):
	lista = []
	for i in estoque:
		 lista.append(i)
	return lista

def imprimeQuantidades(estoque):
	lista = []
	for i in estoque:
		lista.append(i[0])
	return lista

def calculaTotalCompra(estoque):
	total = 0 
	for i in estoque:
		soma = i[0] * i[1]
		total += soma
	
	return total 


