from collections import Counter

def scramble(s1, s2):
    l = all(c in set(s1) for c in set(s2) )
    if not l:
        return False
    return all(Counter(s1).get(k,0)//Counter(s2)[k] for k in Counter(s2))  

w1,w2 = 'rkqodlw', 'worldez'
# assert scramble(w1,w2) == False
