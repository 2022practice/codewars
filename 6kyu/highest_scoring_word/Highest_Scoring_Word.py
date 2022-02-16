import string
def high(x):
    ''' me ingresan un string asi >> 'juanito fue a comprar papa' 
    y tengo que devolver la palabra que mayor sume segun la unicacion de sus letras en el dicc'''
    s= x.split(' ')
    d={key:value for value,key in enumerate(string.ascii_lowercase, start=1)}
    valores=[]
    for name in s:
        for letter in name:
            valores.append(d.get(letter))
        valores.append(None)
    valores_list=[str(num) for num in valores]
    valores_str=' '.join(valores_list)
    valores_str_list=valores_str.split('None')
    valores_str_list.remove('')
    numeros_esp=[num.split(' ') for num in valores_str_list]
    p=[]
    for lista in numeros_esp:
        o=[]
        for num in lista:
            if num !='':
                o.append(int(num))
        p.append(o)
    suma =[sum(lista) for lista in p]
    indice_max_valor=suma.index(max(suma))
    return s[indice_max_valor]



    
    #def high(x):
    #l = x.split()

    #d = {chr(i):i-ord('a')+1 for i in range(ord('a'),ord('z')+1)}

    #return sorted(l[::-1],key=lambda w: sum([d[char] for char in w]))[-1]


