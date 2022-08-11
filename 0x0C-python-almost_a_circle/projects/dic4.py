#!/usr/bin/phthon3
# coding: utf-8
# Exercice 4
""" This program print concatenation dictionary """
"""
    Args:
        dicPC: {"HP": 11, "Acer": 7, "Lenovo": 17, "Del": 23}
        dicPhone: {"Samsung": 22, "Iphone": 9, "Other": 13}
        dicTablette: {"Samsung": 15, "Other": 13}
"""
print("""***** Method 1 ****""")
dicPC = {"HP": 11, "Acer": 7, "Lenovo": 17, "Del": 23}
dicPhone = {"Samsung": 22, "Iphone": 9, "Other": 13}
dicTablette = {"Samssung": 15, "Other": 13}

""""Iniatialisation of dic global"""
dicTotal = dict({})

dicTotal.update(dicPC)
dicTotal.update(dicPhone)
dicTotal.update(dicTablette)
print(dicTotal)
print("\n")


print("""|||||||||||||||||||||||||||||||||||||||||||||""")
print("""*********************************************""")
print("""+++++++++++++++++++++++++++++++++++++++++++++\n""")
print("""***** Method 2 ****""")

for d in [dicPC, dicPhone, dicTablette]:
    dicTotal.update(d)
print("Le dictionnaire total est : {}".format(dicTotal))





