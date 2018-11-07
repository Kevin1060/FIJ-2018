import random

nombre_a_trouver = random.randrange(100)

continuer = True

while continuer == True:

  entree = int ( input("tapez un nombre"))

  if nombre_a_trouver > entree :
    print ("le nombre est plus grand")
  elif nombre_a_trouver < entree : 
    print ("le nombre est plus petit")
  else :
    print ("le nombre est egale, bravo")
    continuer = False
