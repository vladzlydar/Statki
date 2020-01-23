from Board import Board
from Ship import Ship
from OneDeck import OneDeck
from TwoDeck import TwoDeck
from ThreeDeck import ThreeDeck
from FourDeck import FourDeck
from EmptySea import EmptySea

def whereToShot():
    row = input("Input row to shoot: ")
    column = input("Input column to shoot: ")
    return int(row), int(column)

def askForBoardSize():
    xDimension = input("Provide how many cells should be horizontally: ")
    yDimension = input("Provide how many cells should be vertically: ")
    print("Now lets place the Ships!")
    return xDimension, yDimension

def askForShipToPlace():
    size = input("Provide size of ship 1-4: ")
    xPos = input("Provide X position of ship nose: ")
    yPos = input("Provide Y position of ship nose: ")
    allign = input("Should be horizontal/vertical? Type 0/1 respectively: ")
    print("==========================================")
    if int(allign) == 0:
        return size, xPos, yPos, True
    elif int(allign) == 1:
        return size, xPos, yPos, False

def printBoard(board):
    print(end="  ")
    for i in range(0, len(board.getShips())):
        print(i,end=" ")
    print()
    for row in range(0,len(board.getShips())):
        print(row, end =" ")
        for column in range(0,len(board.getShips()[row])):
            print(board.getShips()[row][column].toString(row, column), end=" ")
        print()

def whichShipToCreate(size, allign):
    if size == 1:
        return OneDeck(allign)
    elif size == 2:
        return TwoDeck(allign)
    elif size == 3:
        return ThreeDeck(allign)
    elif size == 4:
        return FourDeck(allign)
    else:
        return EmptySea()

def game():
    ships = []
    xDim,yDim = askForBoardSize()
    board = Board(xDim, yDim)
    while True:
        size, xPos, yPos, allign = askForShipToPlace()
        ship = whichShipToCreate(int(size),allign)
        if ship.placeShipAt(int(yPos), int(xPos), allign, board):
            ships.append(ship)
        next = input("Would you like to continue providing ships yes/no = 1/0 respectively: ")
        if int(next) == 0:
            break
        else:
            continue
    while len(ships)>0:
        row, col = whereToShot()
        _,text = board.shootAt(row, col)
        print(text)
        printBoard(board)
        if "sink" in text:
            ships.pop()
            print("Congratulations you sink all the ships! Game over! ")

game()


