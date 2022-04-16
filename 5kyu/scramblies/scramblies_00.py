from collections import Counter

def scramble(s1, s2):
    l = all(c in set(s1) for c in set(s2) )
    if not l:
        return False
    s1_c = Counter(s1)
    s2_c = Counter(s2)
    return all(s1_c.get(k,0)//s2_c[k] for k in s2_c)  

w1,w2 = 'rkqodlw', 'worldez'
# assert scramble(w1,w2) == False
