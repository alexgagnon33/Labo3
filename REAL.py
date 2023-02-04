def donnee_carte():
    trefle = ["♣ 1", "♣ 2", "♣ 3", "♣ 4", "♣ 5", "♣ 6", "♣ 7", "♣ 8", "♣ 9", "♣ 10", "♣ 11", "♣ 12", "♣ 13"]
    coeur = ["♥ 1", "♥ 2", "♥ 3", "♥ 4", "♥ 5", "♥ 6", "♥ 7", "♥ 8", "♥ 9", "♥ 10", "♥ 11", "♥ 12", "♥ 13"]
    pique = ["♠ 1", "♠ 2", "♠ 3", "♠ 4", "♠ 5", "♠ 6", "♠ 7", "♠ 8", "♠ 9", "♠ 10", "♠ 11", "♠ 12", "♠ 13"]
    carreau = ["♦ 1", "♦ 2", "♦ 3", "♦ 4", "♦ 5", "♦ 6", "♦ 7", "♦ 8", "♦ 9", "♦ 10", "♦ 11", "♦ 12", "♦ 13"]

    carte = trefle + coeur + pique + carreau

    return carte

def Afficher_etat(carte):
    for i in range(0, 52, 13):
        print(carte[i:i+13])

def Brassage_inter_coupe(carte):
    half1 = carte[:26]
    half2 = carte[26:]
    carte = [item for sublist in zip(half1, half2) for item in sublist]
    return carte

def Brassage_paquet(carte):
    liste_carte = []
    groupe_carte = 4
    for i in range (0, len(carte), groupe_carte):
        liste_carte.append(carte[i:i+groupe_carte])
    x = liste_carte
    carte = (x[6], x[0], x[2], x[12], x[1], x[3], x[10], x[5], x[7], x[4], x[11], x[9], x[8])
    return [item for sublist in carte for item in sublist]

def Sauvegarde(carte):
    with open("cards.txt", "w", encoding="UTF-8") as f:
        for i in range(0, 52, 13):
            f.write(" ".join(carte[i:i+13]) + "\n")

def dict_carte(carte):
    menu = {1: "Afficher l'état du jeu de carte",
            2: "Effectuer un brassage inter-coupé",
            3: "Effectuer un brassage par paquets",
            4: "Sauvegarder l'état final dans un fichier",}
    print()
    for num, option in menu.items():
        print(f"{num} - {option}")
    choix = int(input("Voici les choix disponibles: "))
    carte = menu[choix](carte)
    return carte

dict_carte(donnee_carte())