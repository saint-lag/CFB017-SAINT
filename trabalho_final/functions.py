
import pandas as pd 
import xlrd
from Bio import SeqIO
from Bio.Seq import Seq
import csv


'''Arquivo destinado para as funções que serão utilizadas em main.py'''

### Pandas ###

def ColunasNormalizadasCPM(sheet):
	'''Critério 'c)' e 'd)': Crie colunas adicionais 
	para adicionar os níveis de expressão normalizados por CPM de cada réplica. 
	Nomeie essas colunas como Rep1_A_CPM, Rep2_A_CPM, Rep1_B_CPM e Rep2_B_CPM;
	Crie colunas adicionais que vão armazenar a expressão normalizada
	(CPM) média por condição. Nomeia as colunas como Cond_A_CPM_media e
	Cond_B_CPM_media '''

	# TERMINADO #
	
	tabela = pd.read_excel(sheet)
	
	coluna1 = tabela.iloc[:,1]
	coluna2 = tabela.iloc[:,2]
	coluna3 = tabela.iloc[:,3]
	coluna4 = tabela.iloc[:,4]

	soma1 = sum(coluna1)
	soma2 = sum(coluna2)
	soma3 = sum(coluna3)
	soma4 = sum(coluna4)

	coluna_nova1 = pd.DataFrame()
	coluna_nova1["Rap_1A_CPM"] = (coluna1*1000000)/soma1
	coluna_nova2 = pd.DataFrame()
	coluna_nova2["Rap_2A_CPM"] = (coluna2*1000000)/soma2
	coluna_nova3 = pd.DataFrame()
	coluna_nova3["Rap_1B_CPM"] = (coluna3*1000000)/soma3
	coluna_nova4 = pd.DataFrame()
	coluna_nova4["Rap_2B_CPM"] = (coluna4*1000000)/soma4

	tabela_nova1 = pd.concat([tabela,coluna_nova1, coluna_nova2, coluna_nova3, coluna_nova4], axis=1)
	
	coluna5 = tabela_nova1.iloc[:,5]
	coluna6 = tabela_nova1.iloc[:,6]
	coluna7 = tabela_nova1.iloc[:,7]
	coluna8 = tabela_nova1.iloc[:,8]

	media_A = pd.DataFrame()
	media_A["Cond_A_CPM_media"] = (coluna5 + coluna6)/2
	media_B = pd.DataFrame()
	media_B["Cond_B_CPM_media"] = (coluna7 + coluna8)/2
	tabela_nova2 = pd.concat([tabela_nova1,media_A, media_B], axis=1)

	return tabela_nova2


def GenesMaisExpressos(new_sheet):
	'''Selecione os cinco genes mais expressos de cada 
	condição baseado na expressão média.'''


	genes_xA = new_sheet['Cond_A_CPM_media'].nlargest()
	genes_xB = new_sheet['Cond_B_CPM_media'].nlargest() 	
	
	genes_xA = genes_xA.index.values.tolist()
	genes_xB = genes_xB.index.values.tolist()

	genes_xA=[str(int) for int in genes_xA]
	genes_xB=[str(int) for int in genes_xB]


	return genes_xA, genes_xB


### BLAST ###

def BlastTest(genes_xA, genes_xB, krna_seq, familiar_aa):

	from Bio.Blast.Applications import NcbiblastxCommandline

	sequencia = familiar_aa
	blastx = 'C:/Program Files/NCBI/blast-2.11.0+/bin/blastx.exe'
	meuOutPut = 'blast_test.txt'
	q = '/Users/maias/Documents/GitHub/CFB017-SAINT/trabalho_final/teste.fasta'
	meu_comando = NcbiblastxCommandline(query = q, subject = sequencia, outfmt = 6, out = meuOutPut, evalue = 0.05, cmd = blastx)
	stdout, stderr = meu_comando()

	return meuOutPut


def ArchiveGenes(genes_xA, genes_xB, krna_seq):
	

	# Lista para testar o codigo
	lst=[]

	# Listas que recebem os i.seq de cada gene
	genes_seq_a = []
	genes_seq_b = []

	# Procura as sequencias
	for i in SeqIO.parse(krna_seq, 'fasta'):
		for y in genes_xA:
			if i.id == 'gene_%s'%y:
				genes_seq_a.append(i.seq)
		for y in genes_xB:
			if i.id == 'gene_%s'%y:
				genes_seq_b.append(i.seq)


	# Transforma as sequências em Fasta
	count = 0
	for i in genes_seq_a:
		y = genes_xA[count]
		if count < len(genes_xA):
			file = open('/Users/maias/Documents/GitHub/CFB017-SAINT/trabalho_final/blast_genesA/gene_%s.fasta'%y, 'x')
			file.write(str(i))
			file.close()
			count += 1
		else:
			break

	count = 0
	for i in genes_seq_b:
		y = genes_xB[count]
		if count < len(genes_xB):
			file = open('/Users/maias/Documents/GitHub/CFB017-SAINT/trabalho_final/blast_genesB/gene_%s.fasta'%y, 'x')
			file.write(str(i))
			count += 1
			file.close()
		else:
			break 
	
	return True


def BlastGenes10(genes_xA, genes_xB, krna_seq, familiar_aa):
	'''Realize uma busca BLAST da sequência de DNA dos 
	10 genes selecionados anteriormente contra as 
	sequências de aminoácidos de R. prolixus.'''

	from Bio.Blast.Applications import NcbiblastxCommandline


	# Blast dos arquivos
	sequencia = familiar_aa
	blastx = 'C:/Program Files/NCBI/blast-2.11.0+/bin/blastx.exe'
	
	# Arquivos alocados em pastas
	import os
	directory_a = '/Users/maias/Documents/GitHub/CFB017-SAINT/trabalho_final/blast_genesA'
	directory_b = '/Users/maias/Documents/GitHub/CFB017-SAINT/trabalho_final/blast_genesB'

	#for file in os.listdir(directory_a):
	import pathlib
	
	count = 0
	for file in os.listdir(directory_a):
		y = genes_xA[count]
		meuOutPut = 'blast_a%s.txt'%y
		file_path = pathlib.Path(file).parent.absolute()
		file_path = str(file_path).join(file)
		meu_comando = NcbiblastxCommandline(query = file_path, subject = sequencia, outfmt = 6, out = meuOutPut, evalue = 0.05, cmd = blastx)
		stdout, stderr = meu_comando()
		count += 1

	count = 0
	for file in os.listdir(directory_b):
		y = genes_xB[count]
		meuOutPut = 'blast_b%s.txt'%y
		file_path = pathlib.Path(file).parent.absolute()
		file_path.join(file)
		meu_comando = NcbiblastxCommandline( query = file_path, subject = sequencia, outfmt = 6, out = meuOutPut, evalue = 0.05, cmd = blastx)
		stdout, stderr = meu_comando()
		count += 1



def Bitscore(blast):
	'''A partir do resultado do BLAST, imprima o melhor 
	hit para cada um dos 10 genes baseado no maior valor 
	de bitscore. Em caso de bitscores iguais, selecione o 
	hit com menor e-value. Caso o empate persista, selecione 
	qualquer um dos hits empatados.
'''
	
