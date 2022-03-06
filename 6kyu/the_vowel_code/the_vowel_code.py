def encode(st):
    vowels = {'a':1,'e':2 ,'i':3,'o':4,'u':5}
    return ''.join([str(vowels[char]) if char in vowels else char for char in st])
def decode(st):
    vowels = {'1':'a','2':'e' ,'3':'i','4':'o','5':'u'}
    return ''.join([vowels[char] if char in vowels else char for char in st])
