 if True: 
 print('Conditional was True')
# ça va imprimer car c'est vrai

if False:
    print('Conditional was True') 
# ça ne va pas imprimer car la condition après if n'est pas vrai
# le if ne s'execute que si la déclaration après le if est vrai 

# Comparisons:
# Equal:            == 
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is # same object or memory différent de égalité

language = "Python"

if language == "Python":
   print('Conditional was True')

language = "Java"

if language == "Python": # si le language == python alors else ne se lance pas
    print("Language is Python")
else: # si le language est "Java" alors là else se lance 
    print("No match")

if language == "Python": 
    print("Language is Python")
# si le language est python on lance celui là
elif language == "Java":
    print("Language is Java")
# sinon on lance celui là c'est la fonction de elif
elif language == "JavaScript":
    print("Language is JavaScript")
# même fonctionnalité que une switch case car on peut mettre elif à l'infini
else: 
    print("No match")
# sinon on lance le dernier 

# and 
# or
# not
user = "Admin"
logged_in = False
if user == "Admin" and logged_in:
    print("Admin Page")

else:
    print("Bad Creds")

user == "Admins" 
# été évalué pour Vraie mais pas logged_in du coup le else
# se lance 
# mais si on s'en fout on en veux juste qui soit Vraie alors on remplace le and par
# or 

if not logged_in:
    print("Please Log In")
else:
    print("Welcome")
# là not inverse tout si c'est vrai alors ça devient faux et si c'est faux 
# ça devient vrai

a = [1, 2, 3]
b = [1, 2, 3]
b = a
# en faisant ça on défini les id de a et b pour qu'il soit égaux
# print(a is b) cette commande donne True maintenant

print(a == b)
# là on a True car c'est 2 liste sont égale

print(a is b)
# là c'est faux car ce sont différent object a et b

print(id(a) == id(b))
# c'est la même chose que print(a is b)

print(id(a))
print(id(b))
# en faisant ça on voit bien que a et b on différent id

# False Values:
    # False
    # None
    # Zero le seul chiffre faux
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}. = empty dictionnary

condition = False
# pour check dans une liste dictionnaire ou string si les valeurs sont actuellement présente
# maintenant on connait tous les faux les autres choses seront vraie
# condition = False = True dans le programme

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')