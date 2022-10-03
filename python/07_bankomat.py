# Erstelle ein Programm, das einen Bankomaten simuliert. Folgende Möglichkeiten gibt es:
# 1. Einzahlen
# 2. Abheben
# 3. Kontostand
# 4. Beenden
balance = 0

def deposit(money):
    newBalance = balance + money
    print("Sie haben " + str(money) + "€ eingezahlt!\n")
    return int(newBalance)

def withdraw(money):
    newBalance = balance - money
    print("Sie haben " + str(money) + "€ abgehoben!\n")
    return int(newBalance)

while True:
    toDo = input("Selektieren Sie die gewünschte Funktion:"
        "\n1.\tEinzahlen\n2.\tAbheben\n3.\tKontostand\n4.\tBeenden\n\n")
    toDo = int(toDo)

    if toDo == 1:
        money = int(input("Geben Sie den Betrag ein, den sie einzahlen wollen:\t"))
        balance = deposit(money)
    elif toDo == 2:
        money = int(input("Geben Sie den Betrag ein, den sie abheben wollen:\t"))
        balance = withdraw(money)
    elif toDo == 3:
        print("Ihr Kontostand beträgt:\t" + str(balance) + "€\n")
    elif toDo == 4:
        print("Das Programm wird beendet!")
        break
