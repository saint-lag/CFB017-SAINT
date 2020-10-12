
from Bio.Seq import Seq

from main import DnaExons


dna_seq = input('Please, insert dna sequence: ')
start1, end1 = input('Enter exon start and end, please: ').split()
start2, end2 = input('Enter exon start and end, please: ').split()
result = DnaExons(dna_seq, start1, end1, start2, end2)


print('Result: %s' % result)