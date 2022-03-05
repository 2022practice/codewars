def count_bits(n):
    num = n
    resto = []
    if n == 0:
        return num
    while num:
        resto.append(num%2)
        num = num//2
    
    return resto.count(1)
