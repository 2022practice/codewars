def duplicate_encode(word):
    word = word.lower()
    l = []
    for char,char_count in ((char,word.count(char)) for char in word):
        if char_count !=1:
            l.append(')')
        else:
            l.append('(')
    return ''.join(l)
