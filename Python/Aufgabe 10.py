#Aufgabe 10: Einmaleins
x = 1
y = 1

for i in range(100):
    if(y < 10):
        print(x ,"x", y, "=", x * y)
        y += 1

    else:
        x += 1
        y = 1

print(10 ,"x", 10, "=", 100)
