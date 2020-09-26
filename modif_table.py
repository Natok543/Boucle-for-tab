def modif():
  select_modif_ok = False
  print("Vous êtes enter dans la modification.")
  nb_tables = len(tab_total)
  print(f"Il y a {nb_tables} crée.")
  while(select_modif_ok == False):
    select_modif_table = int(input("Quel table voulez vous modif ?"))
    if(select_modif_table < 0 or select_modif_table >= nb_tables):
      print("Le nombre que vous avez choisie est invalide !")
    else:
      print(f"Vous avez selectionner la table numero {select_modif_table}")
      select_modif_ok = True
  print("pour crée une entrée, taper 1")
  print("Pour supprimer une entrée taper, taper 2")
  modif_select = int(input("Votre selection"))
  if(modif_select == 1):  
    tab.append(input(f"Choisir un nombre n°{n} : "))
    print("Votre table : ")
    for element in tab:
      print(element)