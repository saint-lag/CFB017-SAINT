




def BlastTest(familiar_aa):

	from Bio.Blast.Applications import NcbiblastxCommandline

	sequencia = familiar_aa
	blastx = 'C:/Program Files/NCBI/blast-2.11.0+/bin/blastx.exe'
	meuOutPut = 'blast_test.txt'
	q = '/Users/maias/Documents/GitHub/CFB017-SAINT/trabalho_final/blast_genesA/gene_14620.fasta'
	meu_comando = NcbiblastxCommandline(query = q, subject = sequencia, outfmt = 6, out = meuOutPut, evalue = 0.05, cmd = blastx)
	stdout, stderr = meu_comando()

	return meuOutPut



print(BlastTest('/Users/maias/Documents/GitHub/CFB017-SAINT/trabalho_final/VectorBase-48_RprolixusCDC_AnnotatedProteins.fasta'))


import pathlib
import os 
def File():
	file_list = []
	directory = '/Users/maias/Documents/GitHub/CFB017-SAINT/trabalho_final/blast_genesA'
	for file in os.listdir(directory):
		file_path = os.path.abspath(file)
		file_list.append(str(file_path))

		print(file)


#print(File())



