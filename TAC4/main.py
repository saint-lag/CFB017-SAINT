
from Bio import SeqIO
from Bio.Seq import Seq



'''1 - Motivos de DNA ou proteínas são sequências curtas de DNA/aminoácidos
que se repetem um número considerável de vezes no genoma/proteoma que podem
ter ou tem comprovadamente uma função biológica.

1-Escreva um código em Python que leia uma sequência de DNA ou de aminoácidos 
digitada pelo usuário e procure esse motivo em várias sequências de DNA ou 
aminoácidos de um arquivo multi-FASTA;

2-Você deve escrever uma função genérica que busca tanto sequências de DNA 
ou de aminoácidos em um arquivo multi-FASTA;

Você pode usar qualquer arquivo multi-FASTA utilizado até agora na disciplina.

3-Imprima na tela o identificador das sequências que contém este motivo;

4-Escreva uma função que conta quantas vezes o motivo se repete (dica: use a função count de Python);
 
5-Imprima a quantidade de repetições do motivo ao fim da execução;'''




def MotifFinder(sequence, motif):
	id_counter = 0
	for i in SeqIO.parse(sequence, "fasta"):
		i_id = i.id 
		i_seq = i.seq
		count = i_seq.count(motif)

		if count != 0:
			id_counter += 1
			print("ID:", i_id, "\nSequence:", i_seq, "\nCounter:", count)

	print("\nID Counter:", id_counter, sep="")

print(MotifFinder("/Users/maias/Documents/GitHub/CFB017-SAINT/TAC1/TriTrypDB-47_TcruziCLBrenerEsmeraldo-like_AnnotatedProteins.fasta", "LLLLLLLL"))	
