def anagrams(word, words):
    len_word = len(word)
    word = set(word)
    anagrams = [w for w in words if set(w) == word and len(w) == len_word]
    return anagrams
