import random as rand

randNumber = rand.randint(0,100)

if randNumber < 20:
    print(str(randNumber) + " is Mini")
elif randNumber >= 20 and randNumber <= 50:
    print(str(randNumber) + " is Medium")
elif randNumber > 50:
    print(str(randNumber) + " is Large")