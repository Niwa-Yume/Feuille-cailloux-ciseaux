from random import randint

# Liste des choix possibles
t = ["Pierre", "Papier", "Ciseaux"]

# Initialiser les compteurs
counterComputer = 0
counterPlayer = 0

while counterComputer < 3 and counterPlayer < 3:
    # Assigner l'ordinateur comme joueur avec une option de jeu aléatoire entre 0 etr 2
    computer = t[randint(0, 2)]

    # Demander au joueur son choix
    player = input("Pierre, Papier ou Ciseaux ? :")

    if player == computer:
        print("Égalité !")
        computer = t[randint(0, 2)]
        
    elif player == "Pierre":
        if computer == "Papier":
            print("Vous avez perdu !", computer, "couvre la", player)
            counterComputer += 1
            computer = t[randint(0, 2)]

        else:
            print("Vous avez gagné !", player, "écrase la", computer)
            counterPlayer += 1
            computer = t[randint(0, 2)]

    elif player == "Papier":
        if computer == "Ciseaux":
            print("Vous avez perdu !", computer, "coupe", player)
            counterComputer += 1
            computer = t[randint(0, 2)]

        else:
            print("Vous avez gagné !", player, "couvre", computer)
            counterPlayer += 1
            computer = t[randint(0, 2)]

    elif player == "Ciseaux":
        if computer == "Pierre":
            print("Vous avez perdu !", computer, "écrase", player)
            counterComputer += 1
            computer = t[randint(0, 2)]

        else:
            print("Vous avez gagné !", player, "coupe", computer)
            counterPlayer += 1
            computer = t[randint(0, 2)]

    else:
        print("Ce n'est pas une option valide. Vérifiez votre orthographe !")

# Vérifier le gagnant
if counterComputer == 3:
    print("Vous avez perdu !")
elif counterPlayer == 3:
    print("Vous avez gagné !")