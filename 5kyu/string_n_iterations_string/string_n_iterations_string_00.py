# this is a 'solution' but it's not because it passed the test cases 
# but not the general attempt
# this solution gives time out in the attempt

def get_evens(s):
    return ''.join(char for idx,char in enumerate(s) if idx%2 == 0)

def get_odds(s):
    return ''.join(char for idx,char in enumerate(s) if idx%2 != 0)

def jumbled_string(s, n): 
    s = get_evens(s) + get_odds(s) 
    if n == 1:
        return s
    i = 0 
    for num in range(0,n): 
        print (s,i) 
        s = get_evens(s) + get_odds(s)  
        i += 1 
    return s

# this 'solution' doesn't attempt too, but also passed the test cases
# its a recursive solution.
# i think both solutions work but the 'n' parameter is too big for iterations
# or maybe, the string its too large too.
# I tried to expand the python recursion limit but it gives me time out too

def jumbled_string(s, n):
    even = ''.join(char for idx,char in enumerate(s) if idx%2 == 0)
    odd = ''.join(char for idx,char in enumerate(s) if idx%2 != 0)
    s = even + odd
    if n == 1:
        return s and -1
    return jumbled_string(s,n-1)
