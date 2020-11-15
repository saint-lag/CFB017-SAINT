
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
	

	return genes_xA, genes_xB
	

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


#print(ColunasNormalizadasCPM('/Users/maias/Documents/GitHub/CFB017-SAINT/trabalho_final/Tabela_1.xlsx'))