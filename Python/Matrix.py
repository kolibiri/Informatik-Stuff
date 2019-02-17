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

        00 01 02 03 04
        10 11 12 13 14
        20 21 22 23 24
        30 31 32 33 34
        40 41 42 43 44

        """
        x = 1
        y = 0
        c = 0
        by = 0
        bc = 0
        matrix[y][c]=x
        c += 1
        x += 1
        bc = c
        by = y
        for j in range(m-1):
            for i in range(bc+1):
                matrix[y][c]=x
                if(c>0):
                    c -= 1

                y += 1
                x += 1

            c = bc+1
            bc += 1
            y = 0

        y +=1
        by = 1
        bc = m-1
        c = 4
        for i in range(m-2):
            for j in range(bc):
                matrix[y][c]=x
                x+=1
                if(y<4):
                    y+=1

                c-=1

            y = by+1
            by+=1
            c=4

        matrix[y][c]=x







    elif(typ == 6):     #Schlange
        x = 1
        y = 0
        c = 0
        while(y < m):
            for j in range(len(matrix[y])):
                matrix[y][c] = x
                c += 1
                x += z
            y += 1
            c = n-1
            if(y == m):
                pass

            else:
                for k in range(n):
                    matrix[y][c] = x
                    c -= 1
                    x += z

            c = 0
            y += 1


    return(matrix)

"""
matrix1 = creatematrix(5, 5, 1, 1)
getmatrix(matrix1)
matrix2 = creatematrix(5, 5, 1, 2)
getmatrix(matrix2)
matrix3 = creatematrix(5, 5, 1, 3)
getmatrix(matrix3)
matrix4 = creatematrix(5, 5, 1, 4)
getmatrix(matrix4)
matrix5 = creatematrix(5, 5, 1, 6)
getmatrix(matrix5)
"""
matrix6 = creatematrix(5, 5, 1, 5)
getmatrix(matrix6)

