#!/usr/bin/phthon3
# File for list in dictionanry the mineur with our age and majeur our age
# Exercice 1
# program describe a dictionary that present key and value
"""You must be class the majeur as the valeur"""
d = {'Youri': 35, "Ali": 31, "El Hadj": 10, "Treka": 20, "kadi": 15, "Anzata": 18}

mineur = ({})
majeur = ({})

for key, value in d.items():
    if value < 18:
        mineur[key] = value
    else:
        majeur[key] = value

print("La liste des Majeurs est : {}".format(majeur))
print("La liste des Mineur est : {}".format(mineur))

print("********************** Exerccice 2 **************************\n")


