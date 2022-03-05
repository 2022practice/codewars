def digital_root(n):
    num_list = str(sum([int(num) for num in str(n)]))
    while len(num_list) >1:
        num_list = str(sum([int(num) for num in num_list]))
    return int(num_list)
