def highlight(code):
    l=[str(num) for num in range(10)]
    def equals(a,b):
        if a in l and b in l:
            return True
        elif a == b:
            return True
        else:
            return False
    groups, root_idx = [],0
    for idx,current in enumerate(code):
        _next= code[idx+1:idx+2]
        if not equals(current, _next):
            groups.append(code[root_idx:idx+1])
            root_idx = idx+1
    a=[]
    for element in groups:
        for char in element:
                if char in ['F']:
                    a.append(f'<span style="color: pink">{element}</span>')
                    break
                elif char in ['L']: 
                    a.append(f'<span style="color: red">{element}</span>')
                    break
                elif char in ['R']:
                    a.append(f'<span style="color: green">{element}</span>')
                    break
                elif char in l:
                    a.append(f'<span style="color: orange">{element}</span>')
                    break
                else:
                    a.append(char)
    return ''.join(a) 
