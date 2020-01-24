from Board import Board
from Ship import Ship
from HorizontalShip import HorizontalShip
from VerticalShip import VerticalShip
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
    print(end="   ")
    for i in range(0, len(board.getShips())):
        print(str(i),end=" ")
    print()
    print("  "+ "_"*2*len(board.getShips()[0]),end="")
    print()
    for row in range(0,len(board.getShips())):
        print(str(row)+"|", end =" ")
        for column in range(0,len(board.getShips()[row])):
            print(board.getShips()[row][column].toString(row, column), end=" ")
        print()