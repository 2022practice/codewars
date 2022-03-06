def is_valid_IP(string):
    l = string.split('.')
    if len(l)!= 4 :
        return False
    l2 = []
    for n in l:
        if len(n) != 1 and list(n)[0] == '0':
            return False
        if n.isdigit() and int(n) in range(0,256):
            l2.append(n)
        else:
            return False
    if len(l) == len(l2):
        return True
