#Zähle in einem For-Loop die Zahlen von 1 bis 100 (inklusive) zusammen

sum = 0
for number in range(1,101): #range(101) starts at 0, which would be the same
    sum += number

print(sum)