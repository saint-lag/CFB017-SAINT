
import pandas as pd 
from Bio.Seq import Seq
from Bio.SeqUtils import nt_search, GC
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Blast.Applications import NcbiblastxCommandline


def proteinas(DNA):
	''' Escreva um programa Python que peça ao usuário 
		uma sequência de DNA e imprima a sequência de mRNA 
		e a sequência de proteína correspondentes.'''

	# estruturas 
	dna_seq = Seq(DNA)

	pairing_RNA = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C'}

	RNA_Codon_Table = {'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
                   'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
                   'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
                   'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
                   'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
                   'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
                   'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
                   'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
                   'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
                   'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
                   'UAA': '_', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
                   'UAG': '_', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
                   'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
                   'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
                   'UGA': '_', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
                   'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'}

	# código
	'''percebi depois que havia feito sem biopython, 
	achei interessante demonstrar meu raciocínio'''

	#mRNA = ''.join([pairing_RNA[nuc] for nuc in DNA])
	mRNA = dna_seq.transcribe()

	#tmp_ptn = [RNA_Codon_Table[mRNA[pos:pos + 3]] for pos in range(0, len(mRNA) - 2, 3)]
	#ptn = ''.join(tmp_ptn)
	ptn = mRNA.translate()

	return mRNA, ptn


def fatiador(seq_fasta):
	'''Escreva um programa Python que pegue o arquivo sequencias.fasta
	e escreva N arquivos FASTA contendo em cada arquivo apenas
	uma sequência de sequencias.fasta, chamados de sequência_i.fasta
	(onde i varia de 1 a N).
'''	
	#seq_fasta = str(input('Insira sequencias FASTA: '))
	
	# arquivo 
	refArquivoEntrada = SeqIO.parse(open(seq_fasta, 'r'), 'fasta')
		
	# recebe i e cria um arquivo novo para cada ID e sequencia (coloquei um limite de 10 arquivos)
	n = 1
	for i in refArquivoEntrada:
		if n < 10:
			record = SeqRecord(i.seq, i.id)
			SeqIO.write(record, 'Sequencia_%d.fasta'% n,'fasta')

		if n > 10:
			break

		n += 1
		

def blast(seq_path, multi_fasta_path):
	'''Considerando o arquivo FASTA sequenciaDesconhecida.fasta,
	 faça um código em Python que:
	* Lê do usuário o caminho para o arquivo FASTA sequenciaDesconhecida.fasta;
	* Lê do usuário o caminho para o arquivo multi-fasta de proteínas de Trypanosoma cruzi cepa CL Brener Esmeraldo-like TriTrypDB-47_TcruziCLBrenerEsmeraldo-like_AnnotatedProteins.fasta;
	* Executa BLAST da sequência desconhecida de DNA contra as sequências de aminoácidos usando formato de saída nº 6 e e-valor igual à 0,05
	* Imprima somente o hit com o maior score.'''
	
	# recebe os paths
	#seq_path, multi_fasta_path = str(input('Caminho para o arquivo FASTA, multi-fasta: '))

	# BLAST

	
	tac3_blast = '/Users/maias/Documents/GitHub/CFB017-SAINT/TAC3/tac3_blast.txt'

	tcruzi_blast = NcbiblastxCommandline(query = seq_path, subject = multi_fasta_path, evalue = 0.05, outfmt = 6, out = tac3_blast)

	stdout, stdeer = tcruzi_blast()

	result = pd.read_csv('/Users/maias/Documents/GitHub/CFB017-SAINT/TAC3/tac3_blast.txt', sep='\t')

	max_score = result.sort_values('bitscore')

	print(max_score.iloc[[-1]])

# TESTE:
print(blast('/Users/maias/Documents/GitHub/CFB017-SAINT/TAC3/sequenciaDesconhecida.fasta', '/Users/maias/Documents/GitHub/CFB017-SAINT/TAC3/TriTrypDB-47_TcruziCLBrenerEsmeraldo-like_AnnotatedProteins(1).fasta'))