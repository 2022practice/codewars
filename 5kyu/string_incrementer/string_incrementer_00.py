def increment_string(s):
    if not any(s.endswith(d) for d in '0123456789'):
        return s + '1'
    s_r = list(reversed(s))
    num_idx = 0    
    for c in s_r:
        if not c.isdigit():
            num_idx += s_r.index(c)
            break
    nums = str( int( s[-num_idx:] ) + 1 ) 
    if s.isdigit():
        return nums.zfill(len(s))
    return s[:-num_idx] + nums.zfill(num_idx)
