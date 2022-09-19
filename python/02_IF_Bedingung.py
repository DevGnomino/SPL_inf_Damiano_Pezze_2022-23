import random as rand

randNumber1 = rand.randint(0,100)
randNumber2 = rand.randint(0,100)

print(randNumber1)
print(randNumber2)

if randNumber1 < randNumber2 and randNumber1 < 50:
    print("Zahl 1 ist kleiner als Zahl 2 und Mini")

if randNumber1 < 30 or randNumber2 < 30:
    print("Eine der beiden ist kleiner als 30")
    
if randNumber1 < 50 and randNumber2 != 50:
    print("Erste Zahl klein, zweite kein 50iger")
