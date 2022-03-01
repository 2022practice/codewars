problem_link = 'https://www.codewars.com/kata/52597aa56021e91c93000cb0'

def move_zeros(array):
    nums_in_order_without_ceros = [num for num in array if num != 0]
    ceros = [cero for cero in array if cero == 0]
    return nums_in_order_without_ceros + ceros
