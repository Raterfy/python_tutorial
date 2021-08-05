message = 'hello world' 
#"bobby's world" ou 'bobby\'s world'
#deux guillemet pour ne pas confondre : 'bobby's world'

print(message)

parler = """ je mange des bonbons tous les jours 
bahahhahahaahahaaahahah"""
#trois double guillemet pour des messages de plusieurs ligne

print(parler)

dire = 'Hello world'

print(dire[6:]) 
#len = longueur du msg print(len(dire)) 
#[] = index print(dire[0]) = slicing
#[:] = print(dire[0:5]) = Hello = slicing
#[:5] = print(dire[0:5]) = Hello = slicing
#[6:] = print(dire[6:]) =world = slicing

oui = 'Hello world'

print(oui.lower())

#print(oui.lower()) = hello world
#print(oui.upper()) = HELLO WORLD
#print(oui.count('l')) = 3
#print(oui.find(world)) = 6
#print(oui.find(blbllblblblb)) = -1 bc doesn't exist

non = 'Hello world'

non = non.replace('worl','universe')
# non.replace('worl','universe') separate by a comma
# new_non = non.replace('worl','universe') and print that to have the new message
# non = non.replace('worl','universe') = Hello universe

peut = 'Hello'
name = 'Jacque'

non = '{}, {}.' .format(peut, name) # version courte

non = f'{peut}, {name}. Welcome!' #f string

# non = f'{peut}, {name.upper()}. Welcome!'
# to change the message

print(non)

m = 'Hello'
j = 'Jacque'

print(dir(m)) # directory to modify the string like .replace .upper
print(help(stdr)) # to understand the dot in the directory 
print(help(str .lower)) # search the option you want 



 
