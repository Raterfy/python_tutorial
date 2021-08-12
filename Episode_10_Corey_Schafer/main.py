import os

print(dir(os))
"""cette commande pour voir toute les commandes de os"""
print(os.getcwd())

os.chdir("/home/raterfy/python_tutorial/")
"""cette commande pour changer de directory"""
print(os.getcwd())
"""faire ça pour montrer le directory et le path dans lequel on est"""

os.chdir("/home/raterfy/python_tutorial/")
"""cette commande pour changer de directory"""
os.mkdir("Os-demo-2")
"""mkdir crée juste un dossier"""
os.makedirs("Os_demo-2/python")
"""makedirs plus puissant, on peut créer des dossiers dans des dossiers"""
"Os-demo-2"
print(os.listdir())
"""pour voir les fichiers dans le directory"""

os.rmdir()
"""supprimer des dossiers mais pas les sous dossiers"""
os.removedirs()
"""supprimer les dossiers et sous dossiers"""
os.rename("test.txt", "demo.txt")
"""pour renommer les dossiers dans le format ci-dessus fichier de base virgule nv nom"""
print(os.stat("main.py"))
"""faire ça pour savoir les données sur un fichier on peut prendre une donnée spécifique en faisant""" 

print(os.stat("main.py").st_ctime)
from datetime import date, datetime
mod_time = (os.stat("main.py").st_mtime)
print(datetime.fromtimestamp(mod_time))
"""pour comprendre la donnée du temps"""

for dirpath, dirnames, filenames in os.walk("/home/raterfy/python_tutorial/"):
    print("Current path:", dirpath)
    print("Directories:", dirnames)
    print("File:", filenames)
    print()
"""le os.walk permet de chercher des fichiers et dossier dans l'ordi et leur location"""

print(os.environ.get("home"))
"""pour capturer le home directory"""
file_path = os.path.join(os.environ.get("home") + "test.txt")
print(file_path)
"""pour créer un path avec slash et tout"""

print(os.path.basename("/tmp/test.txt"))
"""pour voir le fichier on utilise .basename"""
print(os.path.dirname("/tmp/test.txt"))
"""pour juste voir le directory"""
print(os.path.split("/tmp/test.txt"))
"""pour voir le dossier et le fichier du path"""
print(os.path.exists("/tmp/test.txt"))
"""pour savoir si le path existe"""
print(os.path.isdir("/tmp/test.txt"))
"""pour savoir si c un dossier"""
print(os.path.isfile("/tmp/test.txt"))
"""pour savoir si c'est un fichier"""
print(os.path.splitext("/tmp/test.txt"))
"""pour séparer le test du .txt"""