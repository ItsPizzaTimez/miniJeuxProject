from random import *
import os



def clearSystem():
    os.system('cls')
def gameDifficulty():
    clearSystem()
    gameDifficulty = str(input("Choisis la difficulté du jeu : facile ; normal ; difficile :\n> "))
    if gameDifficulty == "facile":
        essay = 18
        numberMax = 40
    elif gameDifficulty == "normal":
        essay = 16
        numberMax = 60
    elif gameDifficulty == "difficile":
        essay = 14
        numberMax = 80
    else:
        clearSystem()
        print("Aucuns des choix ne correspond !\n")
        gameDifficulty()
    return numberMax, essay



def game(numberMax,essay):
    clearSystem()
    numberOfBot = randint(0,numberMax)
    lengthOfGame = True
    while lengthOfGame:
        playerInput = int(input("Choisis un nombre entre 0 et "+str(numberMax)+" :\n> "))
        if playerInput == numberOfBot:
            clearSystem()
            print("Vous avez gagné en ",essay," essaies !")
            lengthOfGame = False
            scoreRegister()
        elif playerInput < numberOfBot:
            essay -= 1
            print("Trop bas, il vous reste plus que ",essay," !")
        elif playerInput > numberOfBot:
            essay -= 1
            print("Trop haut, il vous reste plus que ",essay," !")
        elif playerInput < int(numberMax):
            clearSystem()
            print("La limite de nombre est de"+str(numberMax)+". Vous ne perdez pas de points d'essaies !")



def scoreRegister():
        scorePlayer = str(input("Voulez-vous enregistrer votre score ?\n1- Oui\n2- Non\n> "))
        if scorePlayer == "1":
            clearSystem()
            if gameDifficulty == "facile":
                userInputPseudoEasy = str(input("Pseudo : "))
            elif gameDifficulty == "normal":
                userInputPseudoNormal = str(input("Pseudo : "))
            elif gameDifficulty == "difficile":
                userInputPseudoDifficil = str(input("Pseudo : "))
            main()
        elif scorePlayer == "2":
            clearSystem()
            main()
        else:
            clearSystem()
            print("Aucuns des choix ne correspond !\n")
        return userInputPseudoEasy,userInputPseudoNormal,userInputPseudoDifficil



def bestScoreEasy(userInputPseudoEasy,scoreBoardEasy):
    userScoreEasy = essay
    scoreBoardEasy.update({userInputPseudoEasy:userScoreEasy})
    resultEasy = sorted(scoreBoardEasy.items(), key=lambda x: x[1], reverse = True)
    for i in resultEasy:
        print(i[0], i[1])
        break



def bestScoreNormal(userInputPseudoNormal):
    userScoreNormal = essay
    scoreBoardNormal.update({userInputPseudoNormal:userScoreNormal})
    resultNormal = sorted(scoreBoardNormal.items(), key=lambda x: x[1], reverse = True)
    for i in resultNormal:
        print(i[0], i[1])
        break



def bestScoreDifficil(userInputPseudoDifficil):
    userScoreDifficil = essay
    scoreBoardDifficil.update({userInputPseudoDifficil:userScoreDifficil})
    resultDifficil = sorted(scoreBoardDifficil.items(), key=lambda x: x[1], reverse = True)
    for i in resultDifficil:
        print(i[0], i[1])
        break



def showScoreBoard():
    userInputShowScoreBoard = str(input("Menu : \n1- Tableau des scores Facile\n2- Tableau des scores Normal\n3- Tableau des scores Difficile\n> "))
    if userInputShowScoreBoard == "1":
        clearSystem()
        bestScoreEasy(userInputPseudoEasy,scoreBoardEasy)
    elif userInputShowScoreBoard == "2":
        clearSystem()
        bestScoreNormal()
    elif userInputShowScoreBoard == "3":
        clearSystem()
        bestScoreDifficil()



def main():
    menuChoice = True
    while menuChoice:
        userInput = str(input("Menu : \n1- Commencer une nouvelle partie\n2- Choisir la difficulté\n3- Voir le tableau des scores\n4- Quitter le jeu :\n> "))
        if userInput == "1":
            menuChoice = False
            clearSystem()
            game(numberMax,essay)
        elif userInput == "2":
            clearSystem()
            gameDifficulty()
        elif userInput == "3":
            clearSystem()
            showScoreBoard()
        elif userInput == "4":
            quit()
        else:
            print("Aucuns des choix ne correspond à votre requête !")



scoreBoardEasy = {
}
scoreBoardNormal = {
}
scoreBoardDifficil = {
}
scoreOfPlayer = 0
numberMax,essay = gameDifficulty()
userInputPseudoEasy,userInputPseudoNormal,userInputPseudoDifficil = scoreRegister()
print("Bienvenue sur le Juste Prix !\n")
main()