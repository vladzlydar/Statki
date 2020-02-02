from HorizontalShip import HorizontalShip
from VerticalShip import VerticalShip
from EmptySea import EmptySea
from Ship import Ship
import copy

class Board:

    def __init__(self, xDim, yDim):
        self.__xDimension = int(xDim)
        self.__yDimension = int(yDim)
        self.__ships = []
        for _ in range(0, self.__yDimension):
            extendCol = []
            for _ in range(0, self.__yDimension):
                extendCol.append(EmptySea())
            self.__ships.append(extendCol)

        for row in range(len(self.__ships)):
            for column in range(len(self.__ships[row])):
                self.__ships[row][column].setrow(row)
                self.__ships[row][column].setcolumn(column)

    def getxdim(self):
        return self.__xDimension

    def getydim(self):
        return self.__yDimension

    def isoccupied(self, row, column):
        if isinstance(self.__ships[row][column], EmptySea):
            return False
        else:
            return True

    def shootat(self, row, column):
        return self.__ships[row][column].shootAt(row, column)

    def oktoplaceship(self, row, column, ship):
        k = 0
        if ship.getishorizontal():
            if column + ship.getsize() <= len(self.__ships[row]):
                for i in range(ship.getsize()):
                    if not self.isoccupied(row, column):
                        k += 1
                        if k == ship.getsize():
                            return True
            else:
                print("This cell is occupied, use other,  ship is not placed !")
                return False
        else:
            if row + ship.getsize() <= len(self.__ships):
                for i in range(ship.getsize()):
                    if not self.isoccupied(row,column):
                        k += 1
                        if k == ship.getsize():
                            return True
            else:
                print("This cell is occupied, use other,  ship is not placed !")
                return False

    def placeshipat(self, row, column, ship):
        if ship.getishorizontal():
            for i in range(ship.getsize()):
                self.__ships[row][column+i] = ship
            ship.setrow(row)
            ship.setcolumn(column)
            return True
        else:
            for i in range(0, ship.getsize()):
                self.__ships[row+i][column] = ship
            ship.setrow(row)
            ship.setcolumn(column)
            return True

    def getships(self):
        return copy.deepcopy(self.__ships)