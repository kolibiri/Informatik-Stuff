while True:
    try:
       variant = int(input("Welche Variante wollen sie ausgeben ? \n1, 2, 3 oder 4"))
       if(variant <= 0 or variant > 4):
        print("Es sind nur die Zahlen 1 - 4 zugelassen")
        continue

       stars = int(input("Wie viele Sterne sollen in die 1. Reihe kommen ? "))
       if(stars <= 1):
        print("Bitte geben sie mehr Sterne als 1 an !")
        continue

       x = stars
       y = 0

    except ValueError:
        print("Bitte nur Zahlen eingeben")
        continue


    if(variant == 1):
        print("*" * stars)
        for i in range(3):
          print("*", " " * (stars-4), "*")

        print("*" * stars)
        break

    if(variant == 2):
        for i in range(stars):
          print("*" * (x))
          x -= 1

        break

    if(variant == 3):
        for i in range(stars):
            print(" " * y, "*" * x)
            x -= 1
            y += 1

        break

    if(variant == 4):
        print(" ", "*" * stars)
        z = 1
        backup = stars
        while(stars >= 1):
            stars -= 2
            z += 1
            print(" " * z,"*" * stars)

        if(backup % 2 == 0):
            print(" " * z, "*")


        while(stars < backup):
            stars += 2
            z -= 1
            print( " " * int(z), "*" * stars)

        break











