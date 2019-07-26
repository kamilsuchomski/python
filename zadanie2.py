def missing_values(input1, input2):

    full = []

    for i in range (1,input2+1):
        full.append(i)

    for n in input1:
        full.remove(n)

    return full
    
