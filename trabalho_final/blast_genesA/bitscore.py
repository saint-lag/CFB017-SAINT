
def Bitscore():
	'''A partir do resultado do BLAST, imprima o melhor 
	hit para cada um dos 10 genes baseado no maior valor 
	de bitscore. Em caso de bitscores iguais, selecione o 
	hit com menor e-value. Caso o empate persista, selecione 
	qualquer um dos hits empatados.
''' 
	import pandas as pd
	import os

	directory_a = '/Users/maias/Documents/GitHub/CFB017-SAINT/trabalho_final/blast_genesA'
	directory_b = '/Users/maias/Documents/GitHub/CFB017-SAINT/trabalho_final/blast_genesB'

	bitscore_fileA = open('/Users/maias/Documents/GitHub/CFB017-SAINT/trabalho_final/blast_genesA/bitscore_fileA.xlsx', 'x')

	for file in os.listdir(directory_a):
		if file.endswith('.txt'):

			result = pd.read_csv(file, sep="\t", names=["qseqid","sseqid","pident","length","mismatch","gapopen","qstart","qend","sstart","send","evalue","bitscore"])

			maximo_score = result.sort_values('bitscore')
			i = maximo_score.iloc[[-1]]

			print(i)

			bitscore_fileA.write(str(i))

Bitscore()



'''A ideia do codigo é criar um novo arquivo que recebe esses dataframes, mas somente com o gene com maior bitscore de cada. 
O ideal é que tambem compare entre os dataframes qual é o mais expresso'''