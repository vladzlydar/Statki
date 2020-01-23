from Ship import Ship

class OneDeck(Ship):

    def __init__(self,allign):
        super().__init__(0, 0, 1, [False], "1")
        self.setShipType(Ship.ShipType.SUBMARINE)
        self.__isHorizontal = allign