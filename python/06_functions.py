import random as rand

# Erstelle eine Funktion die 2 Zahlen addiert
def addition(a, b):
    sum = a + b
    return sum

# Erstelle eine Funktion, die eine zufällige Zahl zwischen 100 und 200 zurückliefert

def randNum():
    randNum = rand.randint(100,200)
    return randNum


# Erstelle eine Funktion, die ein Wort aus einem String Array zurückliefert.
def oneWord(arr):
    randIndex = rand.randint(0, len(arr))
    word = arr[randIndex]
    return word


print(addition(2,4))
print(randNum())
print(oneWord(["Lorem", "ipsum", "dolor", "sit", "amet", "consetetur", "sadipscing", "elitr", "sed", "diam"]))