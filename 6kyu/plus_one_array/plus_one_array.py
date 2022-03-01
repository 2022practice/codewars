def up_array(arr):
    if not arr:
        return None
    for num in arr:
        if num <0 or num>9:
            return None
    number = int(''.join([str(num) for num in arr])) +1
    return [int(num) for num in str(number)]
