 #!/usr/bin/phthon3
# Exercice 7
# program convert a list an dict

def listToDict(L):
    """
        Args:
            L: list of value 
            x: value use for the boucle
    """
    dictParity = dict()
    for x in L:
        if x % 2 == 0 :
            dictParity[x] = "Pair"
        else :
            dictParity[x] = "Inpaire"
    return dictParity



L = [24, 14, 3, 10, 11, 5]

print(listToDict(L))