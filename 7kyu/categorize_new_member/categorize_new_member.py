def open_or_senior(data):
    #si tiene 55 o mas y +7 en handicap es senior
    list_senior_open=[]
    for lista in data:
        if lista[0] >= 55 and lista[1] >7:
                list_senior_open.append('Senior')
        else:
                list_senior_open.append('Open')
    return list_senior_open
