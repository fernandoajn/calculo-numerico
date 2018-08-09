# Intercalar 2 listas
def intercalar(l1,l2):
    l3 = []
    size = len(l1) < len(l2) and len(l1) or len(l2)
    sobrou = len(l1) > len(l2) and len(l1) or len(l2)

    for i in range(size):
        l3.append(l1[i+1])
        l3.append(l2[i])

    if(len(l1) == sobrou):
        l3.extend(l1[size:])
    elif(len(l2) == sobrou):
        l3.extend(l2[size:])

    return l3

l1 = [1, 2, 3]
l2 = ['a', 'b', 'c', 'd', 'e']

print intercalar(l1,l2)