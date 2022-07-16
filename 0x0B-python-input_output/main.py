#!/usr/bin/python3
"""function for open the file"""

animals = open('animals.txt', "a+")

text = animals.read()
print(text)
animals.seek(0)

for animal in animals:
	print(animal)

animals.write('lion\n')
animals.close