#!/usr/bin/phthon3
# Exercice 3
""" This program print the key and value in the list """
"""
    Args:
        key : ['Name', 'Email', 'Phone', "x"]
        values : ['El Hadj', 'elhadjyoussoufo@gmail.com', '2250777653212']
"""

keys = ['Name', 'Email', 'Phone']
values = ['El Hadj', 'elhadjyoussoufo@gmail.com', '2250777653212']

data = dict({})
for i in range(0, len(keys)):
    data[keys[i]] = values[i]

print(data)



