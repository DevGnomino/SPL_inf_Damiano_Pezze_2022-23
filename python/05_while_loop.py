# Erstelle ein Programm, dass Zufallszahlen zwischen 10 und 30 generiert. 
# Das Programm soll die Zufallszahlen zusammenzählen. Sobald die Zahl 15 oder die Zahl 25 kommt, 
# wird das Programm beendet und die Summe der vorherigen Zufallszahlen ausgegeben!

import random as rand

sum = 0
randNumber = 0

while True:
    randNumber = rand.randint(10,30)
    if randNumber == 15 or randNumber == 25:
        break
    else:
        sum += randNumber

print(sum)

