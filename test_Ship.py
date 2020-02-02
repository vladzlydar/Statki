from unittest import TestCase
from Ship import Ship


class TestShip(TestCase):
    def setUp(self) -> None:
        self.ship = Ship(4)

    def test_get_row(self):
        self.assertEqual(self.ship.getRow(), 0)

    def test_get_column(self):
        self.assertEqual(self.ship.getColumn(), 0)

    def test_set_row(self):
        self.ship.setRow(4)
        self.assertEqual(4, self.ship._row)

    def test_set_column(self):
        self.ship.setColumn(4)
        self.assertEqual(4, self.ship._column)

    def test_get_size(self):
        self.assertEqual(self.ship.getSize(), 4)

    def test_get_ship_symbols(self):
        self.assertEqual(self.ship.getShipSymbols(), ["4", "4", "4", "4"])

    def test_get_hit(self):
        self.assertEqual(self.ship.getHit(), [False, False, False, False])

    def test_get_ship_type(self):
        self.assertEqual(self.ship.getShipType(), Ship.ShipType.BATTLESHIP.name)

    def test_is_sunk(self):
        self.assertEqual(self.ship.isSunk(), False)
