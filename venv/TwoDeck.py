from Ship import Ship

class TwoDeck(Ship):
    shipSymbol = "2"

    def __init__(self,allign):
        super().__init__(0, 0, 2, [False,False], "2")
        self.setShipType(Ship.ShipType.DESTROYER)
        self.__isHorizontal = allign
