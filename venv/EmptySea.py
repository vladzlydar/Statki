from Ship import Ship


class EmptySea(Ship):

    hittedEmptySeaSymbol = "O"

    def __init__(self):
        super().__init__(1)
        self.setIsHorizontal(True)
        self.setShipType(Ship.ShipType.EMPTYSEA)

    def toString(self, row, column):
        if self.getHit()[0]:
            return self.getShipSymbols()[0]
        return "~"

    def shootAt(self, row, column):
        if ((self.getColumn() <= column <= self.getColumn() + self.getSize() - 1) or (self.getRow() <= row <= self.getRow() + self.getSize() - 1)):
            if not self.getHit()[column - self.getColumn()]:
                self.getHit()[column - self.getColumn()] = True
                self.getShipSymbols()[column - self.getColumn()] = self.hittedEmptySeaSymbol
                return True, "You shoot in Sea!"
            else:
                return False, "You already shoot there !"
        else:
            return False, "You gave wrong shooting coordinates "