

def donnee_carte():
    trefle = ["♣ 1", "♣ 2", "♣ 3", "♣ 4", "♣ 5", "♣ 6", "♣ 7", "♣ 8", "♣ 9", "♣ 10", "♣ 11", "♣ 12", "♣ 13"]
    coeur = ["♥ 1", "♥ 2", "♥ 3", "♥ 4", "♥ 5", "♥ 6", "♥ 7", "♥ 8", "♥ 9", "♥ 10", "♥ 11", "♥ 12", "♥ 13"]
    pique = ["♠ 1", "♠ 2", "♠ 3", "♠ 4", "♠ 5", "♠ 6", "♠ 7", "♠ 8", "♠ 9", "♠ 10", "♠ 11", "♠ 12", "♠ 13"]
    carreau = ["♦ 1", "♦ 2", "♦ 3", "♦ 4", "♦ 5", "♦ 6", "♦ 7", "♦ 8", "♦ 9", "♦ 10", "♦ 11", "♦ 12", "♦ 13"]

    carte = trefle + coeur + pique + carreau

    return carte

#Pour réussir à choisir la séquence suivante avec le paramètre step: https://pythonexamples.org/python-for-i-in-range/
def Afficher_etat(deck):
    for i in range(0, 52, 13):
        print(deck[i:i+13])


def Brassage_inter_coupe(deck):
    half1 = deck[:26]
    half2 = deck[26:]
    deck = [item for sublist in zip(half1, half2) for item in sublist]
    return deck

#Pour mieux comprendre sur les cartes et les prob https://stackoverflow.com/questions/6007881/what-does-the-0x-syntax-do-in-python#:~:text=This%20is%20because%20of%20the%20fact%20that%20lists,cell%202%20to%20reference%20the%20newly%20computed%20value.
#Puis https://stackoverflow.com/questions/58608799/how-to-shuffle-a-deck-of-cards-in-python
def Brassage_paquet(deck):
    liste_carte = list()
    groupe_carte = 4
    for i in range (0, len(deck), groupe_carte):
        liste_carte.append(deck[i:i+groupe_carte])
        x = liste_carte
    deck = (x[6], x[0], x[2], x[12], x[1], x[3], x[10], x[5], x[7], x[4], x[11], x[9], x[8])
    return deck


def Sauvegarde(deck):
    with open("cards.txt", "w", encoding="UTF-8") as f:
        for i in range(0, 52, 13):
            f.write(" ".join(deck[i:i+13]) + "\n")


def menu_carte(deck):
    menu = {1: "Afficher l'état du jeu de carte",
            2: "Effectuer un brassage inter-coupé",
            3: "Effectuer un brassage par paquets",
            4: "Sauvegarder l'état final dans un fichier",}
    print()


    for num, option in menu.items():
        print(f"{num} - {option}")


    choix = int(input("Voici les choix disponibles: "))
    print()


    if choix == 1:
        Afficher_etat(deck)