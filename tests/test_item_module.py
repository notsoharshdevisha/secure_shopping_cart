import unittest

from modules.alphanumeric import Alphanumeric
from modules.item import Item
from modules.price import Price
from modules.quantity import Quantity


class TestItemModule(unittest.TestCase):
    def test_item_initialization(self) -> None:
        with self.assertRaises(TypeError) as context:
            Item(name="", price=Price(10), quantity=Quantity(10))
        self.assertEqual(str(context.exception),
                         "Invalid type, name of an Item must be an instance of Alphanumeric")

        with self.assertRaises(TypeError) as context:
            Item(
                name=Alphanumeric(value="test"),
                price=10.00, quantity=Quantity(10))
        self.assertEqual(str(context.exception),
                         "Invalid type, price of an Item must be an instance of Price")

        with self.assertRaises(TypeError) as context:
            Item(Alphanumeric(value="test"), price=Price(10.00), quantity=10)
        self.assertEqual(str(context.exception),
                         "Invalid type, quantity of an Item must be an instance of Quantity")

        with self.assertRaises(ValueError) as context:
            Item(Alphanumeric(value="a"*81), price=Price(10.00), quantity=10)
        self.assertEqual(str(context.exception),
                         "The name of an item must not be more than 80 characters long")

    def test_item_immutability(self) -> None:
        item = Item(
            name=Alphanumeric(value="test123"),
            price=Price(value=1.22),
            quantity=Quantity(value=12))

        with self.assertRaises(AttributeError) as context:
            item.name = Alphanumeric(value="test69")
        self.assertEqual(str(context.exception),
                         "property 'name' of 'Item' object has no setter")

        with self.assertRaises(AttributeError) as context:
            item.price = Price(value=12.2)
        self.assertEqual(str(context.exception),
                         "property 'price' of 'Item' object has no setter")

        with self.assertRaises(AttributeError) as context:
            item.quantity = Quantity(value=12)
        self.assertEqual(str(context.exception),
                         "property 'quantity' of 'Item' object has no setter")


if __name__ == "__main__":
    unittest.main()
