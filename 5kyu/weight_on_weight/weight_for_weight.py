def order_weight(weights):
    list_weights = weights.split(' ')
    weight_sum = [sum([int(n) for n in weight]) for weight in list_weights]
    list_ordered_weights = sorted(zip(weight_sum,list_weights)) 
    return ' '.join([weight[1] for weight in list_ordered_weights])
