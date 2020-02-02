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

    def __init__(self, size):
        self._row = 0
        self._column = 0
        self._size = size
        self._hit = []
        self._isHorizontal = True
        self._shipSymbols = []
        self._shipType = Ship.ShipType(size).name
        for i in range(size):
            self._hit.append(False)
            self._shipSymbols.append(str(size))

    def setRow(self, row):
        self._row = row

    def setColumn(self, column):
        self._column = column

    def getSize(self):
        return self._size

    def getRow(self):
        return self._row

    def getColumn(self):
        return self._column

    def getShipSymbols(self):
        return self._shipSymbols

    def getHit(self):
        return self._hit

    def getShipType(self):
        return self._shipType

    def isSunk(self):
        if False in self._hit:
            return False
        else:
            return True