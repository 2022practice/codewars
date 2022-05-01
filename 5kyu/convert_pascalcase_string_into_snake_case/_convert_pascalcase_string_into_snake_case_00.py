def to_underscore(s):
    s_ = []
    for c in str(s):
        if c.isupper():
            s_.append(' ')
            s_.append(c)
        else:
            s_.append(c)
    return (''.join(s_)).lstrip().replace(' ','_').lower()


