def decodeMorse(morse_code):
    morse_words = morse_code.strip().split('   ')
    morse_code_chars_lists = [ morse_word.split(' ') for morse_word in morse_words]
    words_list = []
    for word in morse_code_chars_lists:
        char_list = []
        for char in word:
            char_list.append(MORSE_CODE[char])
        words_list.append(char_list)
    return ' '.join([ ''.join(words_list[word]) for word in range(len(words_list))])
