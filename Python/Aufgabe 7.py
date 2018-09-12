#Aufgabe 7: Altersstatistik
while True:
    Altersangaben = []
    age = 1
    num = 1
    mid = 0
    x = 0
    try:
      variant = int(input("Wollen sie Aufgabe a oder b testen ? \n Für a geben sie die Zahl 1 und für b die Zahl 2 an."))

      if(variant == 1):
        inp = int(input("Wie viele Schüler sind in der Klasse ? : "))
        for i in range(inp):
            print("Wie alt ist der", num,". Schüler ?")
            age = int(input())
            Altersangaben.append(age)
            num += 1

      elif(variant == 2):
       while(True):
         print("Wie alt ist der", num,". Schüler ? \nFalls sie aufhören wollen Eingaben zu geben, geben sie als Alter 0 an \n")
         age = int(input())
         if(age == 0):
            break
         Altersangaben.append(age)
         num += 1



    except ValueError:
        print("Bitte geben sie nur Zahlen an !")
        continue

    for j in range(len(Altersangaben)):
        mid += Altersangaben[x]
        x += 1


    print("Das kleinste Alter ist", min(Altersangaben), "\nDas höchste Alter ist", max(Altersangaben), "\nDer Mittelwert ist :", mid / len(Altersangaben))
    break