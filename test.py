

from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord


def ArmazenadorDeMotivos(arquivo_de_genes):
	''' Pegue a sequencia FASTA que contenha o motivo e 
	armazene em um arquivo FASTA individual. P.ex.: se a 
	sequencia gene_123 contem o motivo, voce vai criar um 
	arquivo chamado "gene_123.fasta" e dentro dele vai ter 
	o cabeçalho e a sequencia do gene_123 em formato FASTA
'''	
	
	# arquivo de entrada que já contenhas os motivos
	refArquivoEntrada = SeqIO.parse(open(arquivo_de_genes, 'r'), 'fasta')

	# cria um arquivo novo para cada ID e sequencia
	count = 1
	for i in refArquivoEntrada:
		record = SeqRecord(i.seq, i.id)
		SeqIO.write(record, 'gene_%d.fasta'%count, 'fasta')

		count += 1


