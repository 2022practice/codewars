def find_short(s):
    return sorted([len(word) for word in s.split(' ')])[0]
