import enum

class Ship:

    class ShipType(enum.Enum):
        BATTLESHIP = 4
        CRUISER = 3
        DESTROYER = 2
        SUBMARINE = 1
        EMPTYSEA = 0

        def __str__(self):
            return self.name

    sunkedShipSymbol = "X"
    hittedShipSymbol = "H"

    def __init__(self, row, column, size, hit, shipSymbol="-"):
        self.__row = row
        self.__column = column
        self.__size = size
        self.__isHorizontal = False
        self.__hit = hit
        self.__shipSymbols = []
        self.__shipType = Ship.ShipType.EMPTYSEA
        for i in range(size):
            self.__shipSymbols.append(shipSymbol)


# SETTERS

    def setHit(self,index):
        self.__hit = index

    def setRow(self, row):
        self.__row = row

    def setColumn(self, column):
        self.__column = column

    def setIsHorizontal(self, isHorizontal):
        self.__isHorizontal = isHorizontal

    def setShipType(self,shipType):
        self.__shipType = shipType

#GETTERS
    def getSize(self):
        return self.__size

    def getRow(self):
        return self.__row

    def getColumn(self):
        return self.__column

    def getShipSymbols(self):
        return self.__shipSymbols

    def getHit(self):
        return self.__hit

    def getShipType(self):
        return self.__shipType

#OTHERFUNCTIONS


    def isHorizontal(self):
        return self.__isHorizontal

    def isSunk(self):
        if False in self.__hit:
            return False
        else:
            return True

    def shootAt(self,row,column):
        if self.isHorizontal():
            if self.__column <= column <= self.__column + self.getSize()-1:
                if not self.__hit[column-self.__column]:
                    self.__hit[column-self.__column] = True
                    if not self.isSunk():
                        self.__shipSymbols[column-self.__column] = self.hittedShipSymbol
                        return True, "Hit!"
                    else:
                        for i in range(0, len(self.__shipSymbols)):
                            self.__shipSymbols[i] = self.sunkedShipSymbol
                        return True, "Hit and sink %s"%(self.getShipType())
                else:
                    print()
                    return False, "You already shot there!"
            else:
                print()
                return False, "You gave wrong row!"
        else:
            if self.__row <= row <= self.__row + self.getSize()-1:
                if not self.__hit[row-self.__row]:
                    self.__hit[row - self.__row] = True
                    if not self.isSunk():
                        self.__shipSymbols[row - self.__row] = self.hittedShipSymbol
                        return True, "Hit!"
                    else:
                        for i in range(0, len(self.__shipSymbols)):
                            self.__shipSymbols[i] = self.sunkedShipSymbol
                        print()
                        return True, "Hit and sink %s"%(self.getShipType())
                else:
                    return False, "You already shot there!"
            else:
                print()
                return False, "You gave wrong row!"

    def toString(self, row, column):
        if self.isSunk():
            return Ship.sunkedShipSymbol
        else:
            if self.isHorizontal():
                return self.__shipSymbols[column - self.__column]
            else:
                return self.__shipSymbols[row - self.__row]

    def okToPlaceShip(self, row, column, horizontal, board):
        k = 0
        if horizontal:
            if column + self.getSize() <= len(board.getShips()[row]):
                for i in range(self.getSize()):
                    if not board.isOccupied(row, column):
                        k += 1
                        if k == self.getSize():
                            return True
            else:
                return False
        else:
            if row + self.getSize() <= len(board.getShips()):
                for i in range(self.getSize()):
                    if not board.isOccupied(row,column):
                        k += 1
                        if k == self.getSize():
                            return True
            else:
                return False

    def placeShipAt(self, row, column, horizontal, board):
        if self.okToPlaceShip(row,column,horizontal,board):
            if horizontal:
                for i in range(self.getSize()):
                    board.getShips()[row][column+i] = self
                self.setRow(row)
                self.setIsHorizontal(horizontal)
                self.setColumn(column)
                return True
            else:
                for i in range(0,self.getSize()):
                    board.getShips()[row+i][column] = self
                self.setRow(row)
                self.setIsHorizontal(horizontal)
                self.setColumn(column)
                return True
        else:
            print("You could not place ship in here")
            return False