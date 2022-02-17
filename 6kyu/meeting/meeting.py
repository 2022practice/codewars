def meeting(s):
    '''me van a ingresar un string con este formato ---> fulanito:apellido;fulanito:apellido;
    y tengo que pasarlo a este ---> (apellido, fulanito)(apellido, fulanito2)'''
    t = s.upper().split(';')
    o=[name.split(':') for name in t]
    for name in o:
        name.reverse()
    p=[' '.join(name) for name in o]
    k=[name.replace(' ',', ') for name in p]
    j=[f'({name})' for name in k]
    return ''.join(sorted(j))
