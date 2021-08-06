student = {"name": "John", "age": 25, "courses":["Math", "CompSci"]}
# {} signe pour le dico
# on peut remplacer la variable av le : par un chiffre et print le chiffre

print(student["courses"])
# pour montrer des valeur de courses

student = {1: "John", "age": 25, "courses":["Math", "CompSci"]}
# pas besoin de "" pour les chiffres
#print(student[1]) = John

print(student["phone"])
# KeyError: "phone"

print(student.get("name"))
# get pour choisir dans le dictionnaire

print(student.get("phone", "Not Found"))
# on peut set à Not Found quand on va print cette commande

student["phone"] = '555-5555'
student ['name'] = "Jane"
# update la valeur de la clé là John passe à Jane
student.update({"name": "Jane", "age": 26, "phone": "555-5555"})
# pour changer dans le dico et ajouter de nouvelle valeur et de clé

del student["age"]
# pour supprimer une valeur dans le dico
age = student.pop('age')
# on enlève age grâce à pop dans le dico
print(age)
# age variable
print(student)

print(len(student))
# ça nous donne le nombre de keys dans le dico
print(student.values())
# que les valeurs dans le dico
print(student.items())
# pour voir les keys et values

for key in student:
    print(key)
# boucle juste pour voir les keys

for key, value in student.items():
    print(key,value)
# pour voir les keys et value    


