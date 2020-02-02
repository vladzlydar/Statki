from unittest import TestCase
import Board
import HorizontalShip
import EmptySea
import VerticalShip

class TestBoard(TestCase):
    def setUp(self):
        self.board = Board.Board(10, 10)
        self.horizontalShip = HorizontalShip.HorizontalShip(4)
        self.verticalShip = VerticalShip.VerticalShip(3)

    def test_get_xdim(self):
        self.assertEqual(self.board.getXDim(), 10)

    def test_get_ydim(self):
        self.assertEqual(self.board.getYDim(), 10)

    def test_is_occupied(self):
        self.assertEqual(self.board.isOccupied(5, 5), False)

    def test_shoot_at_empty_sea(self):
        self.assertEqual(self.board.shootAt(4, 4), (True, "You shoot in Sea!"))

    def test_shoot_at_horizontal_ship(self):
        self.board.placeShipAt(0, 0, self.horizontalShip)
        self.assertEqual(self.board.shootAt(0, 0), (True, "Hit!"))

    def test_shoot_at_vertical_ship(self):
        self.board.placeShipAt(0, 0, self.verticalShip)
        self.assertEqual(self.board.shootAt(0, 0), (True, "Hit!"))

    def test_ok_to_place_ship(self):
        self.assertEqual(self.board.okToPlaceShip(5, 5, self.verticalShip), True)

    def test_place_ship_at(self):
        self.assertEqual(self.board.placeShipAt(3, 3, self.horizontalShip), True)

    def test_get_ships(self):
        k = 0
        for row in range(len(self.board.getShips())):
            for column in range(len(self.board.getShips()[row])):
                if isinstance(self.board.getShips()[row][column], EmptySea.EmptySea):
                    k += 1
        self.assertEqual(self.board.getYDim()*self.board.getXDim(), k)
