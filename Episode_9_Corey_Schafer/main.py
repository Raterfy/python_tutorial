courses = ['History', 'Math', 'Physics', 'CompSci']

import my_module
index = my_module.find_index(courses, "Math")
print(index)

import my_module as mm
'''on définit my_module à mm car c'est plus facile à écrire'''
index = mm.find_index(courses, "Math")
print(index)

from my_module import find_index
'''on fait ça juste pour import une fonction'''
index = find_index(courses, "Math")
print(index)

from my_module import find_index as fi, test
'''on peut rajouter la variable test et le print(test) après
on peut aussi définir la fonction find_index as fi pour nous simplifier la vie mais 
dans ce cas là on arrive plus à lire '''
index = fi(courses, "Math")
print(index)
print(test)

from my_module import *
'''on peut faire étoiles au lieu de tout écrire mais ça nous complique la vie l'étoile
nous permet de tout import de my_module'''
index = find_index(courses, "Math")
print(index)
print(test)

from my_module import find_index, test
import sys
'''le import sys c'est pour savoir d'où vient vient les import puis faire print(sys.path)  '''
index = find_index(courses, "Math")
print(index)
print(test)
print(sys.path)

import sys
sys.path.append('/Users/')
""" si on déplace un fichier par exemple my_module.py sur le bureau il va falloir écrire
le path du fichier pour l'import comme sur la commande ci-dessus"""
from my_module import find_index, test
index = find_index(courses, "Math")
print(index)
print(test)

import random
"""ça vient de la librairie python"""
random_course = random.choice(courses)
print(random_course)

import math
"""ça vient de la librairie python"""
rads = math.radians(90)
print(rads)
"""pour avoir le radian"""
print(math.sin(rads))
"""pour avoir le sinus"""

import datetime
import calendar
"""ça vient de la librairie python"""
today = datetime.date.today()
print(today)
print(calendar.isleap(2017))

import os
print(os.getcwd())
"""pour savoir le dossier dans lequel on est"""
"""on peut scan un fichier créer grâce à ce module"""

import os
print(os.__file__)

import antigravity
"""blague dans la commu"""