
from Bio.Seq import Seq

from main import ConcComplement


dna_seq1, dna_seq2 = input('Enter two dna sequences, please: ').split()
concomplement = ConcComplement(dna_seq1, dna_seq2)

print('Dna reverse complementary: %s' % concomplement)