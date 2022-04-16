from collections import Counter

def first_non_repeating_letter(string):
    s = string.lower()
    l = [(k,s.find(k)) for k,v in Counter(s).items() if v == 1]
    if not l:
        return ''
    return string[l[0][1]]
