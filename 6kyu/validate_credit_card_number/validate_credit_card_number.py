def validate(n):
    len_n = len(str(n))
    if len_n >16:
        return False
    # if the number of elements are even 
    if len_n %2 == 0:
        l = [int(num)*2 if p%2 == 0 else int(num) for p,num in enumerate(str(n))]
     # if the number of elements are odd 
    else:
        l = [int(num)*2 if p%2 != 0 else int(num) for p,num in enumerate(str(n))]
        
    l_2 = [int(num)-9 if int(num)>9 else int(num) for num in l] 
                 
    return sum(l_2)%10 == 0
