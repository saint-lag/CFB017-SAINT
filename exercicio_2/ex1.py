from Bio.Seq import Seq

from main import GCcontent


dna_seq = str(input('Insert a DNA sequence: '))
gccontent = GCcontent(dna_seq)

print("GC-content: %s" % gccontent)

