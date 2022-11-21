import random as rand
playerTempInt = 0
computerTempInt = 0
playerInt = 0
computerInt = 0
roundCounter = 0

while roundCounter < 6:
    roundCounter += 1   

    computerTempInt = rand.randint(1,6)
    computerInt += computerTempInt
    print("Der Computer hat gewürfelt")

    userInput = input("Würfeln Sie (enter)!")
    playerTempInt = rand.randint(1,6)
    playerInt += playerTempInt

    print("Rundenresultat:\n" +
          "Spieler:\t" + str(playerTempInt) + "\tComputer:\t" + str(computerTempInt) +
          "\nSpielstand:\n" + "Spieler:\t" + str(playerInt) + "\tComputer:\t" + str(computerInt))

print("\n-----------------------------\n")
if playerInt < computerInt:
    print("Der Computer hat gewonnen!")
elif playerInt == computerInt:
    print("Das Spiel ist unentschieden zu Ende gegangen!")
else:
    print("Sie haben gewonnen!")
