
from functions import *
from Bio import SeqIO
from Bio.Seq import Seq
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

tabela_1 = input('Tabela xlsx: ')
arquivo_1 = input('multi-FASTA dos genes da espécie alvo: ')
arquivo_2 = input('multi-FASTA dos AA da espécie parente (próxima): ')


### CLASSE ###

class EspecieAlvo():
	def __init__(self, table, kdna_seq, familiar_aa, label):
		self._label = label
		self._table = table
		self._kdna_seq = kdna_seq
				
	def __str__(self):
		return f'\nT1: {self._table}\nA1: {self._kdna_seq}\nA2: {self._familiar_aa}, L:{self._label}'


### TODO ###
'''1. Separar por módulos de desenvolvimento, a fim de não perder muito tempo numa
etapa do algorítmo

2. Entender todos objetivos de trabalho_final/readme.txt'''


### BUG ###
'''Na criação do objeto, EspecieAlvo(r_desconhecidus): 
TypeError: __init__() missing 3 required positional arguments:
'kdna_seq', 'familiar_aa', and 'label'
'''

### TESTE ###

r_desconhecidus = EspecieAlvo(tabela_1, arquivo_1, arquivo_2, 'R.desconhecidus')
print(EspecieAlvo(r_desconhecidus))

