while True:

 try:
  highest = int(input("Geben sie den Grenzwert an : "))
  num = highest
  if(0 >= highest):
     print("Bitte nur positive Zahlen angeben !")
     continue

 except ValueError:
     print("Bitte geben sie nur Zahlen an \n")
     continue

 else:
  for i in range(highest):
    highest -= 1
    num += highest

  print("Das Ergebnis ist", num)

 break