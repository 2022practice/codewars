def sort_array(source_array):
    if not source_array:
        return []
    even=[]
    odd=[]
    for num in source_array:
        if num%2 ==0:
            even.append(num)
        else:
            even.append('*')
            odd.append(num)
    odd.sort()
    iter_odd=iter(odd)
    return [n if type(n) != str else next(iter_odd) for n in even]
