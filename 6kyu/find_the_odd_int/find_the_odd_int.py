def find_it(seq):
    for n,n_count in ((n,seq.count(n)) for n in set(seq)):
        if n_count%2 !=0:
            return n
