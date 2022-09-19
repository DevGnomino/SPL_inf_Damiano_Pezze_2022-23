#Zähle die geraden Ziffern zwischen 1 und 1000 zusammen - Tipp: 
#Starte den Loop bei 2 und erhöhe den Zählindex jeweils um 2.

sum = 0
for number in range(2,1001,2):
   sum += number

print(sum)