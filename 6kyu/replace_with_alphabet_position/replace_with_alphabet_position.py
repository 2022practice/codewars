def alphabet_position(text):
    string_a_z = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_with_positions = {k:v for v,k in enumerate(string_a_z,1)}
    text_in_numbers = [ alphabet_with_positions[letter.lower()] for letter in text if letter.lower() in string_a_z ]
    return ' '.join([str(_) for _ in text_in_numbers])

