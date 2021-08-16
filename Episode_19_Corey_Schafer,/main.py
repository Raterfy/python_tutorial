li = [9,1,8,2,7,3,6,4,5]

s_li = sorted(li)
"""on crée une nouvelle variable qui nous permet de l'organiser"""
s_li = sorted(li, reverse = True)
"""pour inverser les listes"""
print ("Sorted Variable:\t", s_li)
"""pour organiser les variables """
li.sort()
"""c'est une variable"""
print ("Original Variable:\t", li)
"""pour remettre la liste à la base """

tup = (9,1,8,2,7,3,6,4,5)
s_tup = sorted(tup)
print("Tuple\t", s_tup)
"""pareil que au dessus l'explicationj"""

di = {"name": "Corey", "job": "programming", "age": None, "os": "Mac"}
s_di = sorted(di)
print("Dict\t", s_di)
"""ça va par défaut organiser les clés par ordre alphabétique"""

li = [-6,-5,-4,1,2,3]
s_li = sorted(li, key=abs)
"""key=abs pour organiser en valeur absolu"""
print(s_li)

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def __repr__(self):
        return "({},{},${})".format(self.name, self.age, self.salary)

from operator import attrgetter

e1 = Employee("Carl", 37, 70000)
e2 = Employee("Sarah", 29, 80000)
e3 = Employee("John", 43, 90000)

employees = [e1, e2, e3]

#def e_sort(emp):
#    return emp.name
#"""pour faciliter la vue du salaire et les autres trucs"""
s_employees = sorted(employees, key=attrgetter("age"))
s_employees = sorted(employees, key=lambda e: e.name)
"""lambda fonction"""

print(s_employees)
"""pour voir le salaire et tout"""