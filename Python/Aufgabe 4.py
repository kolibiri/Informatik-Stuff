master = True
while master:

 try:
   inp = float(input("Geben sie eine Zahl an : "))
   loop = 2
   ret = 1
   condition = True

 except ValueError:
    print("Bitte geben sie nur Zahlen an(Kommazahlen sind 1.1 und NICHT 1,1) !")
    continue

 while(ret <= inp and condition and loop < 100000):
    ret = ret + (1/loop)
    loop += 1



 if(loop == 100000):
    print("Das Programm wurde nach 100000 Durchläufen abgebrochen")

 else:
   print("Es hat", loop,"Durchläufe gebraucht bis die angegebene Zahl erreicht worden ist.")

 master = False

