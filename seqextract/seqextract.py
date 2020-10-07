#!/usr/bin/env python3

SEQ = input("Input your sequence in FASTA format:")
L = input("What is the lower bound of your sequence?")
U = input("What is the upper bound of your sequence?")
lower = int(L)
upper = int(U)

#for item in L:
#       print(item)

import textwrap
seq = ''
sequ = []
rev = ''
Charcount = 0
Linecount = 0
revcount = 0
#for line in open("/Users/cruz/Downloads/halan.fasta"):
#       Linecount += 1
#       if Linecount == 1:
#               seq += line
#               seq += "reverse strand 249 - 133 \n"
#
#       elif Linecount > 1:
for char in SEQ:
        Charcount += 1
        if Charcount in range(lower,upper +1):
                seq += char

#for char in sequ:
#       if char == 'A':
#               rev += 'T'
#       elif char == 'T':
#               rev += 'A'
#       elif char == 'G':
#               rev += 'C'
#       elif char == 'C':
#               rev += 'G'
#wrapped = textwrap.fill(rev, 60)
#seq += wrapped

print(seq)

