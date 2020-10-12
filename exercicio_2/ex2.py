
from Bio.Seq import Seq

from main import AAPercent


aa_seq = str(input('Enter a Amino acid sequence, please: '))
aa_percent = AAPercent(aa_seq)

print('The percentual of every amino acid as followed: %s' % aa_percent)