def count(string):
    return {char:string.count(char)for char in set(string)}
