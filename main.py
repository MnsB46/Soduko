from squares import square

def createMatrix():
    lst = []
    lstr = []
    for i in range(1, 10):
        for j in range(1, 10):
            lstr.append(square(i, j, list(range(1, 10)), None))
        lst.append(lstr)
        lstr = []
    return lst


def placeStartingDigits(matrix):
    placing = True
    while placing:
        sqr = input()
        if sqr == "done":
            placing = False
        else:
            #matrix[int(sqr[0])-1][int(sqr[1])-1].value = int(sqr[2])
            placeDigit(matrix, int(sqr[0]), int(sqr[1]), int(sqr[2]))

def showMatrix(matrix):
    for e in matrix:
        string = ""
        for i in e:
            if i.value == None:
                string += " | N"
            else:
                string += " | " + str(i.value)
        print(string)

def placeDigit(matrix, row, column, v):
    matrix[row-1][column-1].changeDigit(v)
    matrix[row-1][column-1].possibleValues.clear()
    b = matrix[row-1][column-1].box
    removePossibleValuesAfterPlacingDigit(matrix, row, column, b, v)

def removePossibleValuesAfterPlacingDigit(matrix, r, c, b, v):
    for e in matrix:
        for sqr in e:
            if sqr.value == None and (sqr.row == r or sqr.column == c or sqr.box == b):
                if v in sqr.possibleValues:
                    sqr.removePossibleValue(v)
                    if len(sqr.possibleValues) == 1:
                        placeDigit(matrix, sqr.row, sqr.column, sqr.value)

def correctSoFar(matrix):
    dictionaryBox = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}
    dictionaryColumn = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}
    for e in matrix:
        rowlist = []
        for i in e:
            if i.value != None:
                rowlist.append(i.value)
                dictionaryBox[i.box].append(i.value)
                dictionaryColumn[i.column].append(i.value)
        if len(rowlist) != len(set(rowlist)):
            return False
    for e in dictionaryBox:
        if len(dictionaryBox[e]) != len(set(dictionaryBox[e])):
            return False
    for e in dictionaryColumn:
        if len(dictionaryColumn[e]) != len(set(dictionaryColumn[e])):
            return False
    return True
    
def startingPosition(matrix):
    lst = [112, 128, 137, 145, 154, 196, 225, 262, 278, 284, 299, 326, 353, 387, 436, 455, 467, 473, 511, 538, 574, 597, 627, 633, 679, 686, 691, 716, 744, 835, 847, 863, 889, 917, 949, 952, 981, 995]
    for e in lst:
        e = str(e)
        placeDigit(matrix, int(e[0]), int(e[1]), int(e[2]))
    
matrix = createMatrix()
startingPosition(matrix)
showMatrix(matrix)