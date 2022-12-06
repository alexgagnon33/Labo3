def donnée_carte():
    trefle = ["♣ 1", "♣ 2", "♣ 3", "♣ 4", "♣ 5", "♣ 6", "♣ 7", "♣ 8", "♣ 9", "♣ 10", "♣ 11", "♣ 12", "♣ 13"]
    coeur = ["♥ 1", "♥ 2", "♥ 3", "♥ 4", "♥ 5", "♥ 6", "♥ 7", "♥ 8", "♥ 9", "♥ 10", "♥ 11", "♥ 12", "♥ 13"]
    pique = ["♠ 1", "♠ 2", "♠ 3", "♠ 4", "♠ 5", "♠ 6", "♠ 7", "♠ 8", "♠ 9", "♠ 10", "♠ 11", "♠ 12", "♠ 13"]
    carreau = ["♦ 1", "♦ 2", "♦ 3", "♦ 4", "♦ 5", "♦ 6", "♦ 7", "♦ 8", "♦ 9", "♦ 10", "♦ 11", "♦ 12", "♦ 13"]
    carte = trefle + coeur + pique + carreau
    return carte

def Afficher_état(carte):
    print(carte[0:13])
    print(carte[13:26])
    print(carte[26:39])
    print(carte[39:52])

def Brassage_inter_coupé(carte):
    longeur = len(carte)
    moitier = longeur//2
    premiere_moitier = carte[:moitier]
    deuxieme_moitier = carte[moitier:]
    carte = [item for sublist in zip(premiere_moitier, deuxieme_moitier) for item in sublist]
    return carte

def Brassage_paquet(carte):
    liste_carte = list()
    groupe_carte = 4
    for i in range (0, len(carte), groupe_carte):
        liste_carte.append(carte[i:i+groupe_carte])
        x = liste_carte
    carte = (x[6], x[0], x[2], x[12], x[1], x[3], x[10], x[5], x[7], x[4], x[11], x[9], x[8])
    return carte

def Sauvegarde(carte):

    with open("cards.txt", "w", encoding="UTF-8") as f:
        f.write({carte[0:13]}, {carte[13:26]}, {carte[26:39]}, {carte[39:52]})

def menu_carte(carte):
    carte 
        menu_carte= {1: "Afficher l'état du jeu de carte",
                    2: "Effectuer un brassage inter-coupé",
                    3: "Effectuer un brassage par paquets",
                    4: "Sauvegarder l'état final dans un fichier",}
        print()

        for num, option in menu_carte.items():
            print(f"{num} - {option}")

        choix = int(input("Voici les choix disponibles: "))
        print()

        match choix:
            case 1: 
                Afficher_état(carte) 
            case 2:
                Brassage_inter_coupé(carte)
            case 3:
                Brassage_paquet(carte)
            case 4:
                Sauvegarde(carte)
            case _:
                print("Choix invalide")

menu_carte()