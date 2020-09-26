def modif(a):
  select_modif_ok = False
  print("Vous êtes enter dans la modification.")
  nb_tables = len(a)
  print(f"Il y a {nb_tables} tables crée.")
  while(select_modif_ok == False):
    try:
      select_modif_table = int(input("Quel table voulez vous modif ? :"))
    except:
      print("Vous n'avez pas saisie un nombre")
      continue
    if(select_modif_table < 0 or select_modif_table > nb_tables):
      print("Le nombre que vous avez choisie est invalide !")
    else:
      print(f"Vous avez selectionner la table numero {select_modif_table}")
      select_modif_ok = True
      select_modif_table = select_modif_table - 1
  print("pour crée une entrée, taper 1")
  print("Pour supprimer une entrée taper, taper 2")
  print("Pour supprimer une entrée taper, taper 3")
  modif_select = int(input("Votre selection : "))
  if(modif_select == 1):  
    a[select_modif_table].append(input(f"Choisir une entrée : "))
    print("Votre table : ")
    for element in a[select_modif_table]:
      print(element)