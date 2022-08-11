 #!/usr/bin/phthon3
# Exercice 6
# program count the number of letter print

phrase = input('Entrer votre phrase ou mot: ')
d = dict({})

for i in phrase:
    d[i] = phrase.count(i)

print(d)



