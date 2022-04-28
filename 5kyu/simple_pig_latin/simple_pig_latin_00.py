def pig_it(text):
    t = text.split()
    new_t_list= [ word[1:]+ word[0] + 'ay' if word.isalpha() else word  for word in t ]
    return ' '.join(new_t_list)

