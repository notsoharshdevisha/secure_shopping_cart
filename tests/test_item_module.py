import unittest

from modules.alphanumeric import Alphanumeric
from modules.item import Item
from modules.price import Price
from modules.quantity import Quantity


class TestItemModule(unittest.TestCase):
    def test_item_initialization(self) -> None:
        with self.assertRaises(TypeError) as context:
            Item(name="", price=Price(10.00), quantity=Quantity(10))
        self.assertEqual(str(context.exception),
                         "Invalid type, name of an Item must be an instance of Alphanumeric")

        with self.assertRaises(TypeError) as context:
            Item(name=Alphanumeric(value="test"),
                 price=10.00, quantity=Quantity(10))
        self.assertEqual(str(context.exception),
                         "Invalid type, price of an Item must be an instance of Price")

        with self.assertRaises(TypeError) as context:
            Item(Alphanumeric(value="test"), price=Price(10.00), quantity=10)
        self.assertEqual(str(context.exception),
                         "Invalid type, quantity of an Item must be an instance of Quantity")


if __name__ == "__main__":
    unittest.main()
