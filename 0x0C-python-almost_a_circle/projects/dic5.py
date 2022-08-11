# Exercice 5
eleveNotes = {'eleve 1': 15, "eleve 2": 7, "Eeleve 3": 9, "eleve 4": 8, "eleve 5": 15, "eleve 6": 18, "eleve 7": 20,
                "eleve 8": 18, "eleve 9": 14, "eleve 10": 5}

admin = dict({})
nonAdmin = dict({})

for key, value in eleveNotes.items():
    if value < 10:
        nonAdmin[key] = value
    else:
        admin[key] = value

print("La liste des élève admin est : {}".format(admin))
print("La liste des élève non admin est : {}".format(nonAdmin))