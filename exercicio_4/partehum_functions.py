
import statistics


def LeitorParaLista(valores):
	'''Lê os valores e armazena em uma lista até ser informado de um valor igual a -1'''
	notas = []
	for i in valores:
		if i != -1:
			notas.append(i)
		if i == -1:
			break

	return notas


def QuantidadeDeValores(lista):
	'''Quantidade de valores que foram lidos'''
	
	return len(lista)


def Mostrador(lista):
	'''Mostra todos os valores na ordem em que foram informados, um ao lado do outro'''

	for num in lista:
		print(num)


def MostradorInvertido(lista):
	'''Mostre todos os valores na ordem inversa à que foram informados, um abaixo do outro'''
	
	lista.reverse()

	for num in lista:
		print(num) 

	
def Soma(lista):
	'''Calcula e mostra a soma dos valores'''
	
	soma = sum(lista)

	return soma

def Media(lista):
	'''Calcula e mostra a media dos valores'''

	media = statistics.mean(lista)

	return media


def QuantAcimaMedia(lista, media):
	'''Calcula e mostra a quantidade de valores acima da media'''
	
	acima = []
	for num in lista:
		if num > media:
			acima.append(num)
		else:
			pass

	quant_acima = len(acima)

	return quant_acima	
