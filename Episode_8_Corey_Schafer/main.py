
def hello_func():
    pass # pass keyword c'est pour dire que l'on va remplir la fonction plus tard
hello_func() # on met les parenthèse pour l'éxecuter
print(hello_func()) 
# si on print(hello_func) on aura juste la position de la fonction
# print(hello_func()) nous donne rien car on a pas défini la fonction

def hello_func():
    print("Hello Function!")

hello_func()
# on peut juste écrire hello_func() pour éxécuter la fonction pas besoin de print

def hello_func():
    print("Hello Function.")
 
hello_func()
hello_func()
hello_func()
hello_func()

"""
les fonctions sont utiles car on peut changer les points en point d'exclamation 
juste en mofifiant la fonction:

def hello_func():
    print("Hello Function.") 
 
#print("Hello Function.")
#print("Hello Function.")
#print("Hello Function.")
#print("Hello Function.")

au lieu de print plusieur fois et changer la string manuellement par exemple

#hello_func()
#hello_func()
#hello_func()
#hello_func()

"""

def hello_func():
    return "Hello Function." 
# return signifie que si on éxécute la fonction se sera égale "Hello Function"
# si on éxécute la fonction sans print ça ne donnera rien car c'est juste une string 
# avec qui on ne fera rien
# lorsaue l'on execute une fonction il vaut mieux juste connaître l'input et le return
# print(hello_func().upper()) 
# on peut modifier les résultats avec les commandes de string

def hello_func(greeting):
    return "{} Function.".format(greeting) 
# on fait ça pour utiliser greeting dans les parenthèses de hello_func()
# greeting ne fait partie que de la fonction 
print(hello_func("Hi"))
# là on peut mettre une nouvelle string dans les parenthèses
# quand on lance cette fonction ça donne Hi Function.

def hello_func(greeting, name= "You"):
    return "{}, {}".format(greeting, name) 
# {} = place holder    

# print(hello_func("Hi", name = "Correy"))    

def student_info(*args, **kwargs):
# * : allow us to accept an arbitrary number of positional or keyword argument
# args and kwargs est une convention  
    print(args)
    print(kwargs)


student_info("Math", "Art", name = "John", age = 22) 
# *args = tuple avec les positional argument: ('Math', 'Art')
# **kwargs = dictionary with all our keyword and value: {'name': 'John', 'age': 22}

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ["Math", "Art"]
info = {"name": "John", "age": 22}

student_info(*courses, **info) 

# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    # Comment une année bisextile est calculé


def days_in_month(year, month):
    """Return number of days in that month in that year."""

# year 2017
# month 2
    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(is_leap(2017))
# La fonction is_leap nous permet de savoir si on est dans une année bisextile 
print(days_in_month(2017, 2))
""" La fonction days_in_month nous permet de savoir si le mois de février se 
fini par un 28 ou un 29 et nous dire si l'annés est bisextile ou pas""" 

""" Exemple pour nous montrer que l'on peut déjà comprendre des fonction compliqué
avec des notions de base """