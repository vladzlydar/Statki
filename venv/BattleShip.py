from Board import Board
import GUI
from HorizontalShip import HorizontalShip
from VerticalShip import VerticalShip
from EmptySea import EmptySea

def whichShipToCreate(size, allign):
    if allign == 0:
        return HorizontalShip(size)
    elif allign == 1:
        return VerticalShip(size)
    else:
        return EmptySea()


def game():
    ships = []
    xDim,yDim = GUI.askForBoardSize()
    board = Board(xDim, yDim)
    GUI.printBoard(board)
    while True:
        size, xPos, yPos, allign = GUI.askForShipToPlace()
        ship = whichShipToCreate(int(size), allign)
        if board.okToPlaceShip(int(yPos), int(xPos), ship):
            board.placeShipAt(int(yPos), int(xPos), ship)
            ships.append(ship)
        next = input("Would you like to continue providing ships yes/no = 1/0 respectively: ")
        if int(next) == 0:
            break
        else:
            continue
    while len(ships) > 0:
        row, col = GUI.whereToShot()
        _, text = board.shootAt(row, col)
        print(text)
        GUI.printBoard(board)
        if "sink" in text:
            ships.pop()
            print("Congratulations you sink all the ships! Game over! ")

game()


