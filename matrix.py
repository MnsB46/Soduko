from squares import square

class board:
    def __init__(self):
        self.matrix = self.createMatrix()

    def __str__(self):
        string = "+--------+--------+--------+\n"
        counter = 1
        for e in self.matrix:
            counter2 = 0
            for i in e:
                if counter2 % 3 == 0:
                    string += "|"
                if i.value == None:
                    string += "  "
                else:
                    string += " " + str(i.value)
                counter2 += 1
            string += "|\n"
            if counter % 3 == 0:
                string += "+------+------+------+\n"
            counter += 1
        return string

    def removePossibleValuesAfterPlacingDigit(self, r, c, b, v):
        for e in self.matrix:
            for sqr in e:
                if sqr.value == None and (sqr.row == r or sqr.column == c or sqr.box == b):
                    if v in sqr.possibleValues:
                        sqr.removePossibleValue(v)
                        #if len(sqr.possibleValues) == 1:
                            #self.placeDigit(sqr.row, sqr.column, sqr.possibleValues[0])
    
    def placeDigit(self, row, column, v):
        self.matrix[row-1][column-1].changeDigit(v)
        self.matrix[row-1][column-1].possibleValues.clear()
        b = self.matrix[row-1][column-1].box
        self.removePossibleValuesAfterPlacingDigit(row, column, b, v)

    def correctSoFar(self):
        dictionaryBox = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}
        dictionaryColumn = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}
        for e in self.matrix:
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

    def createMatrix(self):
        lst = []
        lstr = []
        for i in range(1, 10):
            for j in range(1, 10):
                lstr.append(square(i, j, list(range(1, 10)), None))
            lst.append(lstr)
            lstr = []
        return lst
    
    def countDigits(self):
        sum = 0
        for i in self.matrix:
            for e in i:
                if e.value != None:
                    sum += 1
        return sum

    def placeDigitIfOnlyPossibility(self):
        for i in self.matrix:
            for e in i:
                if len(e.possibleValues) == 1:
                    self.placeDigit(e.row, e.column, e.value)