from squares import square
from matrix import board

def placeDigitsByHand(matrix):
    placing = True
    print("Type a 3 digit number.")
    print("The first digits is row, the second is column and the third is the value")
    print("Type done when finished placing digits")
    while placing:
        sqr = input()
        if sqr == "done":
            placing = False
        else:
            try:
                matrix.placeDigit(int(sqr[0]), int(sqr[1]), int(sqr[2]))
            except:
                print("Type a 3 digit number")

def startingPosition(matrix):
    #lst = [111, 122, 133, 214, 225, 236, 317, 328]
    lst = [112, 128, 137, 145, 154, 196, 225, 262, 278, 284, 299, 326, 353, 387, 436, 455, 467, 473, 511, 538, 574, 597, 627, 633, 679, 686, 691, 716, 744, 835, 847, 863, 889, 917, 949, 952, 981, 995]
    for e in lst:
        e = str(e)
        matrix.placeDigit(int(e[0]), int(e[1]), int(e[2]))

def generateRandomSudoku(matrix):
    #Add this feature later
    startingPosition(matrix)


matrix = board()
start_menu = True
playing = True
while start_menu:
    print("1. Make your own sudoku")
    print("2. Generate random sudoku")
    print("Type 1 or 2")
    user_input = input()
    if user_input == "1":
        placeDigitsByHand(matrix)
        start_menu = False
    elif user_input == "2":
        generateRandomSudoku(matrix)
        start_menu = False
    else:
        print("Type 1 or 2")

while playing:
    print(matrix.correctSoFar())
    print(matrix)
    print("1. Place digit")
    print("2. Automatic solver")
    print("Type 1 or 2")
    user_input = input()
    if user_input == "1":
        placeDigitsByHand(matrix)
    elif user_input == "2":
        print("Not finished yet")
    else:
        print("Type 1 or 2")