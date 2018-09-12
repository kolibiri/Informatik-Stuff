import random
import math

while True:
    #Eingabe
    try:
        inp = int(input("Geben sie die Anzahl der Zufälligen Punkte an : "))

    except ValueError:
        print("Bitte geben sie nur Zahlen an ! ")
        continue


    treffer = 0
    #loope Anzahl der zufälligen Punkte
    for i in range(inp):
        #generiere zufällige Punkte
        x = random.random() ** 2
        y = random.random() ** 2
        #Wenn Wurzel von x+ y < 1 ist dann zähle treffer nach oben
        if (math.sqrt(x + y) < 1.0):
            treffer += 1

    #Berechne Pi
    pi = (float(treffer) / inp) * 4

    print("Annäherungswert für Pi : ", pi)
    break
