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
        for row in range(0, self.__yDimension):
            extendCol = []
            for column in range(0, self.__yDimension):
                extendCol.append(EmptySea())
            self.__ships.append(extendCol)

        for row in range(len(self.__ships)):
            for column in range(len(self.__ships[row])):
                self.__ships[row][column].setRow(row)
                self.__ships[row][column].setColumn(column)

    def getXDim(self):
        return self.__xDimension

    def getYDim(self):
        return self.__yDimension

    def isOccupied(self, row, column):
        if isinstance(self.__ships[row][column], EmptySea):
            return False
        else:
            return True

    def shootAt(self, row, column):
        return self.__ships[row][column].shootAt(row, column)

    def okToPlaceShip(self, row, column, ship):
        k = 0
        if ship.getIsHorizontal():
            if column + ship.getSize() <= len(self.__ships[row]):
                for i in range(ship.getSize()):
                    if not self.isOccupied(row, column):
                        k += 1
                        if k == ship.getSize():
                            return True
            else:
                print("This cell is occupied, use other,  ship is not placed !")
                return False
        else:
            if row + ship.getSize() <= len(self.__ships):
                for i in range(ship.getSize()):
                    if not self.isOccupied(row,column):
                        k += 1
                        if k == ship.getSize():
                            return True
            else:
                print("This cell is occupied, use other,  ship is not placed !")
                return False

    def placeShipAt(self, row, column, ship):
        if ship.getIsHorizontal():
            for i in range(ship.getSize()):
                self.__ships[row][column+i] = ship
            ship.setRow(row)
            ship.setColumn(column)
            return True
        else:
            for i in range(0,ship.getSize()):
                self.__ships[row+i][column] = ship
            ship.setRow(row)
            ship.setColumn(column)
            return True

    def getShips(self):
        return copy.deepcopy(self.__ships)