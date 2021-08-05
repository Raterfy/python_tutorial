num = 3.54

print(type(num))
# command type says if the number is float or int


# Arithmetic Operators:
# Addition:       3 + 2
# Subtraction:    3 - 2
# Multiplication: 3 * 2
# Division:       3 / 2
# Floor Division: 3 // 2
# Exponent:       3 ** 2
# Modulus:        3 % 2 reste de la division

print(2 % 2)
print(3 * 2 + 1) # we can do various operation 
print(3 * (2 + 4)) # the order of operation work in python

nume = 2
nume = nume + 1
nume += 1 
# nume = nume + 1 = nume += 1 on peut le faire dans d'autre signe ex nume *= 10

print (nume)

print (abs(-3)) 
# valeur absolu de -3 est sa distance à 0 donc 3(forcément positif)

print(round(3.75))
# valeur arrondi de 3.75

print(round(3.75, 1))
# valeur arrondi de 3.75 à 0.1


# Comparisons:
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2 plus grand que
# Less Than:        3 < 2 plus petit que 
# Greater or Equal: 3 >= 2 plus grand ou egal
# Less or Equal:    3 <= 2 inferieur ou egal

num_1 = 3
num_2 = 2

print(num_1 != num_2)

num_3 = "100"
num_4 = "200"

num_3 = int(num_3)
num_4 = int(num_4)

print(num_3 + num_4)
# print(num_3 + num_4) = 100200 bc strings
# si on a des nombre entier integer and a strings we can use the syntaxe int 
# pour créer un nombre entier