import sys
import random

length = int(sys.argv[1])
GC_con = int(sys.argv[2])

dna = ''.join(random.choices('ATGC', weights=[100 - GC_con, 100 - GC_con, GC_con, GC_con], k=length))
print(dna)
