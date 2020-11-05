
### Nota, escrevi algumas partes em inglês a fim de praticar ###


'''
1 - Escreva um código em Python que leia um número 
não determinado de valores (podendo ser positivos e negativos) 
e calcule e escreva a média aritmética dos valores lidos, 
a quantidade de valores positivos, a quantidade de valores 
negativos e o percentual de valores negativos e positivos. 

2 - Faça um algoritmo para ler o nome, as três notas 
e o número de faltas de um aluno e escrever qual a sua 
situação final: Aprovado, Reprovado por Falta ou Reprovado por Média. 
A média para aprovação é 7,0 e o limite de faltas é 25% do total de aulas. 
O número de aulas ministradas no semestre foi de 80. Caso seja reprovado por 
falta e por média, prevalece a reprovação por falta. 

3 -  O IMC – Indice de Massa Corporal é um critério da 
Organização Mundial de Saúde para dar uma indicação sobre 
a condição de peso de uma pessoa adulta. A fórmula é IMC = peso/(altura)²

Elabore um algoritmo que leia o peso e a altura de um adulto 
e mostre sua condição de acordo com a tabela abaixo.

IMC em adultos	Condição
Abaixo de 18,5	Abaixo do peso
Entre 18,5 e 25	Peso normal
Entre 25 e 30	Acima do peso
Acima de 30		obeso 
'''

def AprovAluno(nome, nota1, nota2, nota3, faltas):

	# Valores fixos:
	num_aulas = 80

	# Variaveis:
	soma_das_notas = int(nota1) + int(nota2) + int(nota3)

	media_das_notas = soma_das_notas/3

	porcentagem_de_faltas = (int(faltas) * 100)/num_aulas	


	# Situação final
	situacao = ''
	if media_das_notas < 7.0 or porcentagem_de_faltas > 25.0:
		situacao = situacao.join('Reprovado')

	else:
		situacao = situacao.join('Aprovado')


	print('Alune:',nome,'Notas:',nota1,'',nota2,'',nota3,'Faltas:',faltas,
		'Média:',media_das_notas,'Porcentagem de faltas:',
		porcentagem_de_faltas,'Situação:',situacao,'Soma das notas', 
		soma_das_notas)


def IMC(w, h):
	'''Insert weight in kilograms and height in meters, example: 
	'60 1.66' ... which means 60kg weight and 1.66m height'''

	IMC = w/(h**2)

	if IMC < 18.5:
		print('Below weight')
	elif 18.5 < IMC < 25:
		print('Normal weight')
	elif 25 < IMC < 30:
		print('Above weight')
	elif IMC > 30:
		print('Obese')
	else:
		print('Not valid')
	print(IMC)


def NumQuant():
	'''Números são recebidos com vígulas'''
	#user_input = input('Insira números separados por vírgulas:')

	import statistics 

	# num_list receberá os numeros de user_input sem vírgula
	num_list = ['10','-200','1000','23','0']

	temp_list = []
	for i in num_list:
		temp_list.append(int(i))

	num_list = temp_list
	num_mean = statistics.mean(num_list)
	num_sum = sum(num_list)

	num_pos = 0 
	num_neg = 0
	num_zero = 0
	num_len = len(num_list) 
	for num in num_list:
		if num > 0:
			num_pos += 1
		elif num < 0:
			num_neg += 1
		else:
			num_zero += 1

	# porcentagem dos negativos e positivos
	num_neg_percent = (num_neg * 100)/num_len
	num_pos_percent = (num_pos * 100)/num_len


	print('Average:', num_mean, 'Sum:', num_sum, 'Number list:', num_list, 
		'Positive numbers:', num_pos, 'Negative numbers:', 
		num_neg, 'Zeros:', num_zero,'Total numbers:',num_len, 'Negative percentual:', 
		num_neg_percent, 'Positive percentual:', num_pos_percent)


