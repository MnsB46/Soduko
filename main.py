from squares import square
from matrix import board

def placeStartingDigitsByHand(matrix):
    placing = True
    while placing:
        sqr = input()
        if sqr == "done":
            placing = False
        else:
            matrix.placeDigit(int(sqr[0]), int(sqr[1]), int(sqr[2]))
    
def startingPosition(matrix):
    #lst = [111, 122, 133, 214, 225, 236, 317, 328]
    lst = [112, 128, 137, 145, 154, 196, 225, 262, 278, 284, 299, 326, 353, 387, 436, 455, 467, 473, 511, 538, 574, 597, 627, 633, 679, 686, 691, 716, 744, 835, 847, 863, 889, 917, 949, 952, 981, 995]
    for e in lst:
        e = str(e)
        matrix.placeDigit(int(e[0]), int(e[1]), int(e[2]))


matrix = board()
playing = True
while playing:
    placeStartingDigitsByHand(matrix)
    print(matrix.correctSoFar())
    print(matrix)