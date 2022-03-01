def disemvowel(string_):
    return ''.join([letter for letter in string_ if letter.lower() not in 'aeiou'])
