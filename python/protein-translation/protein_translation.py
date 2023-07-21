codon_protein_map = {
    'AUG':'Methionine',
    'UUU':'Phenylalanine',
    'UUC':'Phenylalanine',
    'UUA':'Leucine',
    'UUG':'Leucine',
    'UCU':'Serine',
    'UCC':'Serine',
    'UCA':'Serine',
    'UCG':'Serine',
    'UAU':'Tyrosine',
    'UAC':'Tyrosine',
    'UGU':'Cysteine',
    'UGC':'Cysteine',
    'UGG':'Tryptophan',
    'UAA':'STOP',
    'UAG':'STOP',
    'UGA':'STOP'
}

def proteins(strand):
    proteins = []
    codons = [strand[i:i+3] for i in range(0, len(strand), 3)]
    for codon in codons:
        if codon_protein_map[codon] == 'STOP':
            return proteins
        else:
            proteins.append(codon_protein_map[codon])
    return proteins

