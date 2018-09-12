while True:

 try:
  highest = int(input("Geben sie den Grenzwert an : "))
  if(0 >= highest):
      print("Bitte nur positive Zahlen angeben !")
      continue

 except ValueError:
     print("Bitte geben sie nur Zahlen an \n")
     continue


 else:
  summ = 0
  num = 0
  while(highest > summ):
     summ += 1
     num += summ

  print("Das Ergebnis ist", num)

 break