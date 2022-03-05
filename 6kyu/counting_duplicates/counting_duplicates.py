def duplicate_count(text):
    txt = text.lower()
    l = []
    for char,char_count in ((char,txt.count(char)) for char in set(txt)):
        if char_count != 1:
            l.append(char)
    return len(l)
