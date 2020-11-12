
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

	# dataframe
	df = pd.read_excel(sheet)
	
	# Adicionando colunas com os níveis de expressão normalizados(CPM)
	df_q = df
	df_q[['Rep1_A_CPM','Rep1_B_CPM','Rep2_A_CPM','Rep2_B_CPM']] 

	# CPM média por condição, aplicar formular de CPM media em cada Cond.
	df_q['Cond_A_CPM_media', 'Cond_B_CPM_media'] 

	# df + df_q == df_final 
	df_final = pd.merge(df,df_q)
	df_final.to_excel('Users/maias/Documents/GitHub/CFB017-SAINT/trabalho_final', sheet_name = 'TabelaNormalizada.xlrd')

	# retorna a nova tabela
	with open('Users/maias/Documents/GitHub/CFB017-SAINT/trabalho_final/TabelaNormalizada.xlrd') as tabela:
		#return tabela
	
	pass
	
def GenesMaisExpressos(sheet):
	'''Selecione os cinco genes mais expressos de cada 
	condição baseado na expressão média.'''
	genes = []
	tabela = pd.read_excel(sheet)

	# usando pandas para encontrar os mais expressos em CondA e CondB

	'''os genes mais expressos foram guardados numa lista.
	Para trabalhar com eles, será necessário uma pesquisa com Biopython no
	arquivo multi-FASTA (arquivo_1); assim, guardando-os em um novo 
	arquivo multi-FASTA'''

	#genes_xA = ''
	#genes_xB = ''

	#return genes_xA, genes_xB
	pass


### Funções que envolvem a aplicação de BLAST ###

def BlastGenes10(genes_xA, genes_xB, familiar_aa):
	'''Realize uma busca BLAST da sequência de DNA dos 
	10 genes selecionados anteriormente contra as 
	sequências de aminoácidos de R. prolixus.'''
	
	# Legenda: 'genes_xA'/'genes_xB' são os genes mais expressos em formato de multifasta
	

	pass
	
	
def Bitscore(blast):
	'''A partir do resultado do BLAST, imprima o melhor 
	hit para cada um dos 10 genes baseado no maior valor 
	de bitscore. Em caso de bitscores iguais, selecione o 
	hit com menor e-value. Caso o empate persista, selecione 
	qualquer um dos hits empatados.
'''
	
	pass