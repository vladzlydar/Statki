from Ship import Ship

class ThreeDeck(Ship):
    shipSymbol = "3"

    def __init__(self,allign):
        super().__init__(0, 0, 3, [False, False, False], "3")
        self.setShipType(Ship.ShipType.CRUISER)
        self.__isHorizontal = allign