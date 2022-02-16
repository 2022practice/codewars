def count_smileys(arr):
    #eyes=[':',';']
    #smiles=[')','D']
    #c=[list(face) for face in arr]
    valid_smiley_faces = [':)',':-)',':~)',';)',';~)',';-)',':D',':-D',':~D',';D',';-D',';~D']
    d=[]
    for face in arr:
        if face in valid_smiley_faces:
            d.append(1)
        else:
            d.append(0)

    return sum(d)
