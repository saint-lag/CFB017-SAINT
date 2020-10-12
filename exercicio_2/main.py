
from Bio.Seq import Seq


def GCcontent(dna_seq):
    '''GC content of a dna sequence'''
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
    '''Percentual of every Amino acid of a sequence'''
    
    # Dicionario
    amino_acidict = {'A': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0,
     'I': 0, 'L': 0, 'K': 0, 'M': 0,'N': 0,'P': 0,'Q': 0,'R': 0,'S': 0,'T': 0,
     'V': 0,'W': 0, 'Y': 0}

    # Porcentagem dos amino acidos
    amino_percent = {'A': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0,
     'I': 0, 'L': 0, 'K': 0, 'M': 0,'N': 0,'P': 0,'Q': 0,'R': 0,'S': 0,'T': 0,
     'V': 0,'W': 0, 'Y': 0}

    # Amino acidos da sequência são contados 
    for aa in aa_seq:
        amino_acidict[aa] += 1 

    # lista que receberá os valores 
    lst = list(amino_acidict.values())

    # Soma total doa AA
    E = sum(lst)


    # Formula para percentagem de cada AA: x = (100(E - y))/E
    for aa in amino_acidict:
        y = E - amino_acidict[aa]
        amino_percent[aa] = (100*(E - y))/E
        

    return amino_percent


def ConcComplement(dna_seq1, dna_seq2):
    '''Adds up two dna sequence and returns it's complementary sequence '''
    
    # Concatenação
    dna_seq = dna_seq1 + dna_seq2

    # Dna complementar
    DNA_Reverse_Complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}


    return ''.join([DNA_Reverse_Complement[nuc] for nuc in dna_seq])
    

def DnaExons(dna_seq, start1, end1, start2, end2):
    ''' Returns 2 exons added together'''

    exon1 = dna_seq[start1: end1]

    exon2 = dna_seq[start2: end2]

    result = exon1 + exon2

    return result












print(DnaExons('ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT', 1, 20, 62, 123))
