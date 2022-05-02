from fractions import Fraction as frac

def mixed_fraction(s):
    #for negative fractions
    if '-' in s:
        if s.count('-') == 1:
            s = s.replace('-','')

        f = frac(s)
        n = f.numerator
        d = f.denominator
        int_ = n//d
        frac_n = n%d
        frac_d = d
        return f'-{int_} {frac_n}/{frac_d}'
    f = frac(s)
    n = f.numerator
    d = f.denominator
    int_ = n//d
    frac_n = n%d
    frac_d = d
    if n == 0:
        return '0'
    # for positive fractions
    if n > 0 and d > 0:
        if frac_n == 0:
            return f'{int_}'
        return f'{int_} {frac_n}/{frac_d}'
