# On importe la librairie qui contient plusieurs
import random
# On initialise nos différentes variables
entree =-1
reponse = random.randrange(100) # on utilise la fonction randrange qui permet de choisir un nombre entre 0 et le nombre entre (), ici 100
compteur=10

# Tant que l'entrée est différente de la réponse et que le compteur est plus grand que 0...
while entree != reponse and compteur > 0 :
  # On change la valeur de l'entrée avec celle tapée au clavier. Attention, convertion en int 
  entree =int( input("entre un nombre entre 0 et 100") )

  if entree < reponse :
    print("la reponse est plus grande")
  if entree > reponse : 
    print("la reponse est plus petite")
  else :
    print("bravoo")

#Attention à changer la valeur du compteur pour éviter une boucle infinie
compteur = compteur -1


