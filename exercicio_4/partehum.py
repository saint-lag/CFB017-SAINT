


'''
1 - Faça um programa que leia um número indeterminado de valores e armazene numa lista, 
correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 
(que não deve ser armazenado). Após esta entrada de dados, faça:

a) Uma função que mostre a quantidade de valores que foram lidos;
b) Uma função que mostre todos os valores na ordem em que foram informados, um ao lado do outro;
c) Uma função que mostre todos os valores na ordem inversa à que foram informados, um abaixo do outro;
d) Uma função que calcule e mostre a soma dos valores;
e) Uma função que calcule e mostre a média dos valores;
f) Uma função que calcule e mostre a quantidade de valores acima da média calculada;
'''


from partehum_functions import *


class Notas():
	def __init__(self, valores, label):
		'''Inicializa a classe'''
		'''Só retorna o que foi fornecido'''
		self._label = label
		self._valores = LeitorParaLista(valores)
		self._quantvalores = QuantidadeDeValores(self._valores)
		self._soma = Soma(self._valores)
		self._media = Media(self._valores)
		self._quantacima = QuantAcimaMedia(self._valores, self._media)


	print("\nCarregando...")


	def __str__(self):
		return f'\n[Label]: {self._label}\n[Valores]: {self._valores}\n[Soma]: {self._soma}\n[Media]: {self._media}\n[QuantAcimaMedia]: {self._quantacima}'
		return f'\n[Valores na ordem]: {Mostrador(self._valores)}\n[Valores na ordem inversa]: {MostradorInvertido(self._valores)}'

	print('\nFim.')

### Faltam os mostradores funcionarem corretamente !!!

### TEST ### 

primeiro_trimestre = Notas([10,2,5,6,-1], 'primeiro_trimestre')

print(primeiro_trimestre)
