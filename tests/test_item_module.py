import unittest

from modules.alphanumeric import Alphanumeric
from modules.item import Item
from modules.price import Price
from modules.quantity import Quantity


class TestItemModule(unittest.TestCase):
    def test_item_initialization(self) -> None:
        with self.assertRaises(TypeError) as context:
            Item(name="",  quantity=Quantity(10))
        self.assertEqual(str(context.exception),
                         "Invalid type, name of an Item must be an instance of Alphanumeric")

        with self.assertRaises(TypeError) as context:
            Item(Alphanumeric(value="Item 1"), quantity=10)
        self.assertEqual(str(context.exception),
                         "Invalid type, quantity of an Item must be an instance of Quantity")

    def test_item_immutability(self) -> None:
        item = Item(name=Alphanumeric(value="Item 1"),
                    quantity=Quantity(value=12))

        with self.assertRaises(AttributeError) as context:
            item.name = Alphanumeric(value="Item 1")
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
