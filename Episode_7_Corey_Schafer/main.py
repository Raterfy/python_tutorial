nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num)
# cette boucle affiche tous les chiffres dans la liste

for num in nums:
    if num == 3:
        print("Found")
        continue
    print(num) 
# break la commande casse la boucle
# continue permet de continuer la boucle

for num in nums: # boucle dans la liste de nombre 
    for letter in "abc": # boucle qui passe dans la string 
        print(num, letter)
#cette boucle fait: 1a 1b 1c puis 2a 2b 2c etc

for i in range(10): 
    print(i)
# la valeur commence à 0 par défaut

for i in range(1, 11): # pour faire commencer la valeur à 1 et finir à 10
    print(i) = 0

while x < 10: # tant que x est strictement inférieur à 10
    print(x)
    x += 1 # ajoute +1 à x
# cette boucle s'arrête lorsque que la commande while n'est pas respecté

while x < 10:
    if x == 5: # ça break à 4 car on compte à partir de 0
        break 
    print(x)
    x += 1 

while True: # infinite loop car on a plus de condition
   #if x == 5: 
   #    break # break permet de casser la boucle infini
    print(x)
    x += 1 
# ctrl+c pour casser dans le terminal la boucle infini