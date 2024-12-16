class square:
    def __init__(self, row, column, possibleValues, value):
        self.row = row
        self.column = column
        self.box = self.findBox(row, column)
        self.possibleValues = possibleValues
        self.value = value
        
    def __str__(self):
        return f'Row: {self.row:2d}, column: {self.column:2d}, box: {self.box:2d}, Possible values: {self.possibleValues}, Value: {self.value}'
    
    def findBox(self, r, c):
        if r <= 3:
            if c <= 3:
                return 1
            elif c <= 6:
                return 2
            else:
                return 3
        elif r <= 6:
            if c <= 3:
                return 4
            elif c <= 6:
                return 5
            else:
                return 6
        else:
            if c <= 3:
                return 7
            elif c <= 6:
                return 8
            else:
                return 9
            
    def removePossibleValue(self, n):
        self.possibleValues.remove(n)
    
    def changeDigit(self, n):
        self.value = n
    
    def removeDigit(self):
        self.value = None