def getmatrix(L):
    for i in range(len(L)):
        for l in range(len(L[i])):
            print(L[i][l], end = " ")

        print()

    print("\n")

def getcord(l):
    print(l)


def creatematrix(m, n, z, typ):
    matrix = [[0] * m for i in range(n)]
    if(typ == 1):   #"normal"
        x = 1
        y = 0
        c = 0
        for i in range(m):
            for j in range(len(matrix[y])):
                matrix[y][c] = x
                c += 1
                x += z
            y += 1
            c = 0

    elif(typ == 2): #rückwärts
        x = 1
        y = m-1
        c = n-1
        for i in range(m):
            for j in range(len(matrix[y])):
                matrix[y][c] = x
                c -= 1
                x += z
            y -= 1
            c = n-1

    elif(typ == 3):   # oben nach unten
        x = 1
        y = 0
        c = 0
        for i in range(len(matrix[y])):
            for j in range(m):
                matrix[y][c] = x
                y += 1
                x += 1

            c += 1
            y = 0



    elif(typ == 4):   # unten nach oben
        x = 1
        y = m-1
        c = n-1
        for i in range(len(matrix[y])):
            for j in range(m):
                matrix[y][c] = x
                y -= 1
                x += 1

            c -= 1
            y = m-1

    elif(typ == 5):    # diagonal
        """
        1   2   4   7   11
        3   5   8   12  16
        6   9   13  17  20
        10  14  18  21  23
        15  19  22  24  25

        """
        x = 1
        y = 0
        c = 0


    return(matrix)

matrix1 = creatematrix(5, 5, 1, 1)
getmatrix(matrix1)
matrix2 = creatematrix(5, 5, 1, 2)
getmatrix(matrix2)
matrix3 = creatematrix(5, 5, 1, 3)
getmatrix(matrix3)
matrix4 = creatematrix(5, 5, 1, 4)
getmatrix(matrix4)
