#Aufgabe 8
while True:
    try:
        inp = int(input("Bitte geben sie eine Zahl an, die umgewandelt werden soll :"))

    except ValueError:
        print("Bitte geben sie nur ganze Zahlen an !")
        continue

    i = 0
    roemisch= ""
    zahlen = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    zahlzeichen = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    inp / zahlen[-1]
    for i in zahlen:
        while inp >= i:
            #füge immer größt mögliche römische Zahl ein
            roemisch = roemisch + zahlzeichen[zahlen.index(i)]
            #subtrahiere das zugefügte Zeichen vom Input
            inp = int(inp) - i


    print("\nDie roemische Zahl zu deiner Eingabe lautet: " + roemisch)
    break

    
