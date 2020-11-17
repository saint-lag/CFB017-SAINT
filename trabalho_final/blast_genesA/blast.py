
from /Users/maias/Documents/GitHub/CFB017-SAINT/trabalho_fina/functions import *
import os

directory_a = '/Users/maias/Documents/GitHub/CFB017-SAINT/trabalho_final/blast_genesA'
sequencia =  '/Users/maias/Documents/GitHub/CFB017-SAINT/trabalho_final/VectorBase-48_RprolixusCDC_AnnotatedProteins.fasta'

count = 0
for file in os.listdir(directory_a):
	y = genes_xA[count]
	meuOutPut = 'blast_a%s.txt'%y
	file_path = str(os.path.realpath(file))
	file_path = file_path.replace('\\', '/')
	meu_comando = NcbiblastxCommandline(query = file_path, subject = sequencia, outfmt = 6, out = meuOutPut, evalue = 0.05, cmd = blastx)
	stdout, stderr = meu_comando()
	count += 1


