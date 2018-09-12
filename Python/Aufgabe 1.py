#Aufgabe 1:Bierschaum
vol = 1.00
min = 0
while(vol > 0.01):
    min += 1
    vol *= 0.85

print("Der Schaum hat sich nach", min, "Minuten auf 1% reduziert")


