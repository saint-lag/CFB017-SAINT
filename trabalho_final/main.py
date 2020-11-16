
from functions import *
from Bio import SeqIO
from Bio.Seq import Seq
import pandas as pd
import csv
import xlrd


'''Codigo deve comportar uma classe que receba:

i) uma tabela xlsx com dados de quantificação (tabela 1) para 
quatro bibliotecas de RNA-Seq;

ii) um arquivo multi-fasta contendo as 
sequências de DNA dos genes da espécie alvo (arquivo 1); 

iii) um arquivo multi-fasta contendo sequências de AA da espécie parente 
(arquivo 2)

Dentro da classe, ocorrerá a ação das funções de functions.py

''' 


### INPUT DO USUARIO ###

tabela_1 = '/Users/maias/Documents/GitHub/CFB017-SAINT/trabalho_final/Tabela_1.xlsx'
arquivo_1 = '/Users/maias/Documents/GitHub/CFB017-SAINT/trabalho_final/Rdesconhecidus.fasta'
arquivo_2 = '/Users/maias/Documents/GitHub/CFB017-SAINT/trabalho_final/VectorBase-48_RprolixusCDC_AnnotatedProteins.fasta'
 
### CLASSE ###

class EspecieAlvo():
	def __init__(self, sheet, krna_seq, familiar_aa, label):
		self._label = label
		self._krna_seq = open(krna_seq, 'r')
		self._familiar_aa = open(familiar_aa, 'r')
		self._sheet = ColunasNormalizadasCPM(sheet)
		self._genes_xA, self._genes_xB = GenesMaisExpressos(self._sheet)
		self._blast_result = BlastGenes10(self._genes_xA, self._genes_xB, self._krna_seq, self._familiar_aa)
		#self.bitscore = Bitscore(self._blast_result)

	def __str__(self):
		return f'[Label]: {self._label}\n[Most Expressed Genes]: {self._genes_xA}, {self._genes_xB}\n[Blast]: {self._blast_result}'

### TODO ###
'''1. Separar por módulos de desenvolvimento, a fim de não perder muito tempo numa
etapa do algorítmo

2. Entender todos objetivos de trabalho_final/readme.txt'''


### BUG ###

'''
ALL SOLVED

'''

### TESTE ###

r_desconhecidus = EspecieAlvo(tabela_1, arquivo_1, arquivo_2, 'R.desconhecidus')
print(r_desconhecidus)
