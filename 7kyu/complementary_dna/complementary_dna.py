def DNA_strand(dna):
    dna_dict = {'A':'T','T':'A','C':'G','G':'C'}
    return ''.join([dna_dict[sym] for sym in dna])
