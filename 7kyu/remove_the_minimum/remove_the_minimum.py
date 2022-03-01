def remove_smallest(numbers):
    list_numbers = list(numbers)
    if numbers == []:
        return numbers
    else:
        list_numbers.remove(min(list_numbers))
        return list_numbers

