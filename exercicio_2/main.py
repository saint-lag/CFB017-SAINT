
from Bio.Seq import Seq


def GCcontent(dna_seq):
    C = 0
    G = 0
    for i in dna_seq:
        if i == 'C':
            C += 1
        elif i == 'G':
            G += 1

    gc_content = ((G + C)*100)/len(dna_seq) 
    return gc_content

def AAPercent(aa_seq):

    lst = []

    amino_acidict = {'A': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0,
     'I': 0, 'K': 0, 'M': 0,'N': 0,'P': 0,'Q': 0,'R': 0,'S': 0,'T': 0,
     'V': 0,'W': 0, 'Y': 0}

    for aa in aa_seq:
        amino_acidict[aa] += 1 
    for counter in amino_acidict:
        lst.append(amino_acidict[counter])
    

    #x = (100(E - y))/E


    print(amino_acidict, lst, aa_frequency)


def ConcComplement(dna_seq1, dna_seq2):
    dna_seq = dna_seq1 + dna_seq2

    transdict = {'A': 'T', 'G': 'C', 
                'T': 'A', 'C': 'G'}

    pass
    


        