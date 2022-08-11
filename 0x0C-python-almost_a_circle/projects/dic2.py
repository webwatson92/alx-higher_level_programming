#!/usr/bin/phthon3
# Exercice 2
""" This program print the key and value of word enter in the list """


T = input("Entrer une phrase: ")
L = T.split()
d = dict({}) 
"""
    Args:
        L : variable the user
        d : variable for our dictionary
        mot : variable the user
"""
for mot in L:
    d[mot] = len(mot)

print(d)




