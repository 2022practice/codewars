from math import log, floor

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

