#Aufgabe 2: Merkwürdige Zahlenfolge

def mx(x):    #WIP
    count = 0
    ret = 0


    return ret




while True:
 try:
  num = int(input("Geben sie eine Zahl an :"))
  array = [num]

 except ValueError:
    print("Bitte geben sie nur natürliche Zahlen an !")
    continue

 while(num != 1.0):
  if((num%2) == 0):
        num /= 2.0
  else:
        num = num * 3.0 + 1.0
  array.append(num)

 for x in array:
   print(x)

 print("Anzahl der Durchläufe: ", len(array))
 print("Höchste Zahl in der Folge : ", max(array))
 break



