courses = ['History', 'Math', 'Physic', 'CompSci']
print(courses[-1])
# on commence à 0 pour les chiffres dans [] dans ce cas là 0 = history
# si on veut le dernier item on peut utiliser [-1] donc ComSci

courses.append('Art')
# pour ajouter à la fin de la liste
 
courses.insert(0, 'Maison')
# pour choisir la position dans la liste 
# utiliser la commande print(courses) pour cet exemple 
print(courses)


print(courses[2:])
"""
print(courses[0:2]) 0 = starting point inclusive index deux point pour séparer 
et 2 n'est pas inclu donc on a History et Math qui seront juste afficher
print(courses[2:]) là on affiche à partir de 2 donc Physic et Math

"""

courses_2 = ["Art", "Education"]


courses.insert(0, courses_2)
print(courses[0])
# là on a print la liste courses 2 en position 0 
# [['Art', 'Education'], 'Maison', 'History', 'Math', 'Physic', 'CompSci', 'Art']

courses.extend(courses_2)
# extend pour le print sans les [] et append pour avec [] à la fin de la liste
print(courses)

courses.remove("Math")
# pour enlever Math de la liste
print(courses)

courses.pop()
# pour enlever la dernière valeur de la liste donc là c'est education
popped = courses.pop()
# en faisant ça on fait passer la valeur enlevé au dessus de la liste
print(popped)
print(courses)

courses.reverse()
# pour inverser la liste

courses.sort()
# pour organiser la liste par ordre alphabétique

print(courses)

nums = [1, 5, 2, 4, 3]

nums.sort(reverse)
# ça organise par ordre croissant
# nums.sort(reverse) pour ordre décroissant
# nums.sort(reverse = True) true en majuscule
print(nums)
sorted_courses = sorted(courses)
#pour ne pas altérer la liste originale
print(sorted_courses)

print(min(nums)) # le plus petit nombre de la liste
print(max(nums)) # le plus grand nombre de la liste 
print(sum(nums)) # la somme de tous les nombres de la liste
print(courses.index("CompSci"))
# la position de ComSci dans la liste donc 3 dans ce cas là
print(courses.index("Art"))
# si il n'existe pas la liste on a une ValueError
print("Art" in courses)
print("Math" in courses)
# pour demander si ils sont dans la liste
for item in courses:
    print(item)
# à chaque fois que print est exécuté on va à la ligne par défaut 
# "item" est juste une variable 
for index, item in enumerate(courses): 
     print(index, item)
# on a la variable index et item qui sont utilisés car on a une boucle
for index, item in enumerate(courses, start=1): 
    print(index, item)
# pour faire commencer la liste à 1
course_str = ", ".join(courses)
# nos valeurs sont séparées par une virgule et c'est une chaîne de caractère (string)
# on peut changer la virgule par autre chose comme -
new_list = course_str.split(' - ')
# en faisant on enlève les - et on revient à la liste orginale
print(course_str)
print(new_list)
#les listes sont muable et les tuples sont des listes pas mutable
# Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art' 
# changer la valeur 0 dans Maison est devenu Art de liste 1 et 2 car liste1 = liste 2
# on peut changer les liste car elle est muable

print(list_1)
print(list_2)
# Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

tuple_1[0] = 'Art'
# ça ne change pas la liste car tuple est immuable mais on peut utiliser
# les autres de la liste
# utiliser la liste pour modeifier et les tuples pour boucle et accès 

print(tuple_1)
print(tuple_2)
# Sets
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}
# sets ce sont des valeurs pas ordonnées et pas de duplication {} 
# parenthèse comme ça
# de la même valeur
# cs_courses = {'History', 'Math', 'Physics', 'CompSci','Math'}
# {'CompSci', 'Physics', 'Math', 'History'}
print(cs_courses)
# print('Math' in cs_courses) pour demander si Math est dans la liste
print(cs_courses.intersection(art_courses))
# pour savoir ce qu'il y a en commun dans les 2 listes
print(cs_courses.difference(art_courses))
# pour savoir la difference dans les 2 listes
print(cs_courses.union(art_courses))
# pour unir les 2 listes

# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict peut pas utiliser 
# se sera un empty dictionnaire
empty_set = set()
# pour vider une set forcément la commande ci-dessus