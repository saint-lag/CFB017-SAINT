
from Bio.Blast.Applications import NcbiblastxCommandline

import os

directory_a = '/Users/maias/Documents/GitHub/CFB017-SAINT/trabalho_final/blast_genesB'
sequencia =  '/Users/maias/Documents/GitHub/CFB017-SAINT/trabalho_final/VectorBase-48_RprolixusCDC_AnnotatedProteins.fasta'
blastx = 'C:/Program Files/NCBI/blast-2.11.0+/bin/blastx.exe'
genes_xA = ['11243','1365','4173','8979','9598']

count = 0
for file in os.listdir(directory_a):
	if file.endswith('.fasta'):
		y = genes_xA[count]
		meuOutPut = 'blast_b%s.txt'%y
		file_path = str(os.path.realpath(file))
		file_path = file_path.replace('\\', '/')
		meu_comando = NcbiblastxCommandline(query = file_path, subject = sequencia, outfmt = 6, out = meuOutPut, evalue = 0.05, cmd = blastx)
		stdout, stderr = meu_comando()
		count += 1
