def unique_in_order(iterable):
    unique_list = []
    if len(iterable)==0:
        return unique_list
    else:
        unique_list.append(iterable[0])
    for n in range(1,len(iterable)):
        if iterable[n] != iterable[n-1]:
            unique_list.append(iterable[n])
    return unique_list

