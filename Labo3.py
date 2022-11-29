#créer classe trefle, classe pique, clasee coeur et classe carreau 1 a 13
#créer un menu 

import time 
def labo3():
    trefle = "♣ 1", "♣ 2", "♣ 3", "♣ 4", "♣ 5", "♣ 6", "♣ 7", "♣ 8", "♣ 9", "♣ 10", "♣ 11", "♣ 12", "♣ 13"
    coeur = "♥ 1", "♥ 2", "♥ 3", "♥ 4", "♥ 5", "♥ 6", "♥ 7", "♥ 8", "♥ 9", "♥ 10", "♥ 11", "♥ 12", "♥ 13"
    pique = "♠ 1", "♠ 2", "♠ 3", "♠ 4", "♠ 5", "♠ 6", "♠ 7", "♠ 8", "♠ 9", "♠ 10", "♠ 11", "♠ 12", "♠ 13"
    carreau = "♦ 1", "♦ 2", "♦ 3", "♦ 4", "♦ 5", "♦ 6", "♦ 7", "♦ 8", "♦ 9", "♦ 10", "♦ 11", "♦ 12", "♦ 13"
    carte = trefle, coeur, pique, carreau
#print('Trefle\nCoeur\nCarreau\nPique')
menulabo3 = {
    'Voici les choix disponible: '
    "[1] Afficher l'état du jeu de carte"
    "[2] Effectuer un brassage inter-coupé\n"
    "[3] Effectuer un brassage par paquets\n"
    "[4] Sauvegarder l'état final dans un fichier\n"
}
print(menulabo3)

choix_utilisateur = int(input('Ecriver votre option: '))

if choix_utilisateur == 1:
    print(carte)
elif choix_utilisateur == 2:
    length = len(carte)
    middle_index = length//2
    premiere_moitier = carte[:middle_index]
    deuxieme_moitier = carte[middle_index:]
    carte = [item for sublist in zip(premiere_moitier, deuxieme_moitier) for item in sublist]
    print(carte)
    time.sleep(5)
    #trouver comment revenir à if
elif choix_utilisateur == 3:
    import numpy as np

listA = [11, 18, 19, 21, 29, 46]

splits = np.array_split(listA, 13)

#user.sort()

#users.sort(reverse=True, key=lambda e: e['date_of_birth']) 

#for user in users:
#    print(user)

for array in splits:
    print(list(array))
elif choix_utilisateur ==4:
    #créer doc
    #mettre bureau
    # 13 cartes par ligne
    
