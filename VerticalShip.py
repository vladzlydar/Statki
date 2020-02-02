from Ship import Ship

class VerticalShip(Ship):

    def __init__(self, size):
        super().__init__(size)
        self._isHorizontal = False

    def shootAt(self, row, _):
        if self._row <= row <= self._row + self.getSize() - 1:
            if not self._hit[row - self._row]:
                self._hit[row - self._row] = True
                if not self.isSunk():
                    self._shipSymbols[row - self._row] = self.hittedShipSymbol
                    return True, "Hit!"
                else:
                    for i in range(0, len(self._shipSymbols)):
                        self._shipSymbols[i] = self.sunkedShipSymbol
                    print()
                    return True, "Hit and sink %s" % (self.getShipType())
            else:
                return False, "You already shot there!"
        else:
            print()
            return False, "You gave wrong row!"


    def toString(self, row, column):
        if self.isSunk():
            return Ship.sunkedShipSymbol
        else:
            return self._shipSymbols[row - self._row]

    def getIsHorizontal(self):
        return self._isHorizontal
