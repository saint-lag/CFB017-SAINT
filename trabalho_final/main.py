
from functions import *
from Bio import SeqIO
from Bio.Seq import Seq
import pandas as pd
import csv


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

tabela_1 = pd.read_excel('/Users/maias/Documents/GitHub/CFB017-SAINT/trabalho_final/Tabela_1.xlsx')
temp_arq1 = open('/Users/maias/Documents/GitHub/CFB017-SAINT/trabalho_final/Rdesconhecidus.fasta', 'r')
arquivo_1 = temp_arq1.read()
arquivo_2 = open('/Users/maias/Documents/GitHub/CFB017-SAINT/trabalho_final/VectorBase-48_RprolixusCDC_AnnotatedProteins.fasta', 'r')


### CLASSE ###

class EspecieAlvo():
	def __init__(self, table, kdna_seq, familiar_aa, label):
		self._label = label
		self._table = table
		self._kdna_seq = kdna_seq.read()
		self._familiar_aa = familiar_aa.read()



### TODO ###
'''1. Separar por módulos de desenvolvimento, a fim de não perder muito tempo numa
etapa do algorítmo

2. Entender todos objetivos de trabalho_final/readme.txt'''


### BUG ###
'''
ALL SOLVED

'''

### TESTE ###

#r_desconhecidus = EspecieAlvo(tabela_1, arquivo_1, arquivo_2, 'R.desconhecidus')
#print(r_desconhecidus)

print(arquivo_1)