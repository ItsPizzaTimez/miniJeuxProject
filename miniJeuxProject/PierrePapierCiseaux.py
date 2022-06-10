import random
import os
def clear():
    os.system('cls')
choices = ["pierre","papier","ciseaux"]
game = True
pc_health = 3
player_health = 3
while game:
    pc = random.choice(choices)
    player = str(input("> "))
    if player == "pierre":
        if pc == "pierre":
            clear()
            print("Egalité")
            pc_health = 3
            player_health = 3
        elif pc == "papier":
            clear()
            print("Perdu !")
            pc_health = 3
            player_health -= 1
        else:
            clear()
            print("Gagné !")
            pc_health -= 1
            player_health = 3
    elif player == "papier":
        if pc == "papier":
            clear()
            print("Egalité")
            pc_health = 3
            player_health = 3
        elif pc == "ciseaux":
            clear()
            print("Perdu !")
            pc_health = 3
            player_health -= 1
        else:
            clear()
            print("Gagné !")
            pc_health -= 1
            player_health = 3
    elif player == "ciseaux":
        if pc == "ciseaux":
            clear()
            print("Egalité")
            pc_health = 3
            player_health = 3
        elif pc == "pierre":
            clear()
            print("Perdu !")
            pc_health = 3
            player_health -= 1
        else:
            clear()
            print("Gagné !")
            pc_health -= 1
            player_health = 3
    elif pc_health or player_health == 0:
        game = False
print("Partie terminée !\n")
if pc_health > 0:
    print("C'est le pc qui a gagné !")
elif player_health > 0:
    print("C'est toi qui a gagné !")