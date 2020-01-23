
from OneDeck import OneDeck
from TwoDeck import TwoDeck
from ThreeDeck import ThreeDeck
from FourDeck import FourDeck
from EmptySea import EmptySea
from Ship import Ship

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

    def getShips(self):
        return self.__ships