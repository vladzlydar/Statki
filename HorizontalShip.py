from Ship import Ship


class HorizontalShip(Ship):

    def __init__(self, size):
        super().__init__(size)
        self._isHorizontal = True

    def shootAt(self, _, column):
        if self._column <= column <= self._column + self.getSize() - 1:
            if not self._hit[column - self._column]:
                self._hit[column - self._column] = True
                if not self.isSunk():
                    self._shipSymbols[column - self._column] = self.hittedShipSymbol
                    return True, "Hit!"
                else:
                    for i in range(0, len(self._shipSymbols)):
                        self._shipSymbols[i] = self.sunkedShipSymbol
                    return True, "Hit and sink %s" % (self.getShipType())
            else:
                return False, "You already shot there!"
        else:
            return False, "You gave wrong row!"

    def toString(self, row, column):
        if self.isSunk():
            return Ship.sunkedShipSymbol
        else:
            return self._shipSymbols[column - self._column]

    def getIsHorizontal(self):
        return self._isHorizontal
