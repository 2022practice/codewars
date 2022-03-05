def find_outlier(integers):
    odd = [i for i in integers if i%2 != 0]
    even = [i for i in integers if i%2 == 0]
    if len(odd) < len(even):
        return odd[0]
    else:
        return even[0]
