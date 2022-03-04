def spin_words(sentence):
    list_of_words = [list(word) for word in sentence.split(' ')]
    w = []
    for word in list_of_words:
        if len(word) <5:
            w.append(''.join(word))
        else:
            word.reverse()
            w.append(''.join(word))
    return ' '.join(w)
