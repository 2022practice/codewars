def get_count(input_str):
    return len([(input_str.count(letter)) for letter in input_str if letter in 'aeiou'])
