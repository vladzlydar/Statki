from Ship import Ship

class FourDeck(Ship):
    shipSymbol = "4"

    def __init__(self,allign):
        super().__init__(0, 0, 4, [False, False, False, False], "4")
        self.setShipType(Ship.ShipType.BATTLESHIP)
        self.__isHorizontal = allign
