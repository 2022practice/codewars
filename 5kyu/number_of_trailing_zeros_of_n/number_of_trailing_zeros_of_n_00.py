from math import factorial

def zeros(n):
    ceros = []
    for num in reversed(str(factorial(n))):
        if num == '0':
            ceros.append(num)
        else:
            break
    return len(ceros)


