#Aufgabe 5: Fakultäten und Binomialkoeffizienten

def factorial(x):
    fac = 1
    while(x >= 1):
        fac *= x
        x -= 1

    return fac



while True:

 try:
   choice = int(input("Es stehen die folgenden Rechenoperationen zu Verfügung : \n  1 = Fakultät \n  2 = Binominalkoeffizient"))

   if(choice > 2):
    print("Es stehen nur die Optionen 1 und 2 zur Verfügung ! \n \n")
    continue

   inp = int(input("Geben sie den Wert n an : "))

   if(choice == 2):
    inp2 = int(input("Geben sie den Wert k an : "))
    fac2 = factorial(inp2)

 except ValueError:
    print("Bitte geben sie nur Zahlen an ! \n \n")
    continue

 fac1 = factorial(inp)


 if(choice == 1):
    print(inp, "Fakultät ergibt", fac1)

 elif(choice == 2):
    ret =(fac1)/(fac2 * (factorial(inp - inp2)))
    print(inp , "über", inp2, "ergibt", ret)

 break









