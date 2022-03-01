def valid_parentheses(string):
    if string == '':
        return True
    parentheses = [char for char in string if char in '()']
    try:
        eval(''.join(parentheses))
    except TypeError:
        return True
    except SyntaxError:
        return False
    else:
        return True
