from Ship import Ship


class HorizontalShip(Ship):

    def __init__(self, size):
        super().__init__(size)
        self._isHorizontal = True

    def shootat(self, _, column):
        if self._column <= column <= self._column + self.getsize() - 1:
            if not self._hit[column - self._column]:
                self._hit[column - self._column] = True
                if not self.issunk():
                    self._shipSymbols[column - self._column] = self.hittedShipSymbol
                    return True, "Hit!"
                else:
                    for i in range(0, len(self._shipSymbols)):
                        self._shipSymbols[i] = self.sunkedShipSymbol
                    return True, "Hit and sink %s" % (self.getshiptype())
            else:
                return False, "You already shot there!"
        else:
            return False, "You gave wrong row!"

    def tostring(self, row, column):
        if self.issunk():
            return Ship.sunkedShipSymbol
        else:
            return self._shipSymbols[column - self._column]

    def getishorizontal(self):
        return self._isHorizontal
