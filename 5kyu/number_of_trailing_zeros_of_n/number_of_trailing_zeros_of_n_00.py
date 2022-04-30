from math import factorial
from math import log
from math import floor
# not efficient

def zeros_(n):
    ceros = []
    for num in reversed(str(factorial(n))):
        if num == '0':
            ceros.append(num)
        else:
            break
    return len(ceros)

# I use the formula to calculate trailing zeros in n!

def zeros(n):
    if n == 0:
        return 0
    kmax = floor(log(n,5))
    sum_ = 0
    for k in range(1,kmax+1):
        exp_ = 5**k
        sum_ += floor(n/exp_)
    return sum_

assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7

