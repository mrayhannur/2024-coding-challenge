# 2024 Coding Challenge
# February 7, 2024 (29/366)
# https://www.codewars.com/kata/554e4a2f232cdd87d9000038/

# Testcase: "ATTGC" --> "TAACG"
# Testcase: "GTAT" --> "CATA"

# My Own
def DNA_strand(dna):
    complements = ""
    for letter in dna:
        if letter == 'A':
            complements += 'T'
        elif letter == 'T':
            complements += 'A'
        elif letter == 'C':
            complements += 'G'
        else:
            complements += 'C'
            
    return complements

# Forum Best Answer
pairs = {'A':'T','T':'A','C':'G','G':'C'}
def DNA_strand(dna):
    return ''.join([pairs[x] for x in dna])