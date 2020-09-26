#import
import os
import time
import menus
import modif_table
#Déclaration variables
choix_ok = False
tab_total = [['test', 'test']]
select_modif_table = 0
select_modif_ok = False

#Debut
print("Bienvenu !")
print("Vous êtes dans le menu de tableau, vous pouvez crée un tableau le modif ou en supprimer un")
#selection
choix = menus.menu()
if(choix == 1):
  print("1")
elif(choix == 2):
  modif_table.modif(tab_total)