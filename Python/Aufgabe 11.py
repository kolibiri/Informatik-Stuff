#Aufgabe 11
n = int(input("n = "))
x = int(input("x = "))

for i in range(x-1):
    a = n**2 - 1
    b = 2*n
    c = n**2 + 1
    n -= 1
    print(a, b, c)
