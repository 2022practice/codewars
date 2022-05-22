def ult_dig_4(a,b): 
    div = (a+b)%2 
    if div == 0: 
        return 6 
    return 4 

def ult_digit_9(a,b):
    div = (a+b)%2
    if div == 0:
        return 9
    return 1


def last_digit(a, b):
    a = int(str(a)[-1])
    if a == 1 or b == 0:
        return 1
    if a == 2:
        return ult_digit_2(a,b)
    if a == 3:
        return ult_digit_3(a,b)
    if a == 4:
        return ult_digit_4(a,b)
    if a == 5:
        return 5
    if a == 6:
        return 6
    if a == 7:
        return ult_digit_7(a,b)
    if a == 8:
        return ult_digit_8(a,b)
    if a == 9:
        return ult_digit_9(a,b)
    if a == 0:
        return 0
    return a


