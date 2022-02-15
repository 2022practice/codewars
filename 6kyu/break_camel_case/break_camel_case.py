problem_link= 'https://www.codewars.com/kata/5208f99aee097e6552000148'

def solution(s):
    upper = []
    lower = []
    for letter in s:
        if letter.isupper():
            upper.append(letter)
            lower.append(' ')
            lower.append('')
        else:
            lower.append(letter)
    iter_upper = iter(upper)
    r = [item if item else next(iter_upper) for item in lower]
    return ''.join(r)
