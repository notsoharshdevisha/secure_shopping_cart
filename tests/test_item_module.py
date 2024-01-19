import unittest

from fake_db.db import catalogue
from modules.initialization_error import InitializationError
from modules.item import Item


class TestItemModule(unittest.TestCase):
    def test_item_initialization(self) -> None:
        with self.assertRaises(InitializationError) as context:
            Item(name=123, quantity=12)
        self.assertEqual(str(context.exception),
                         "Invalid Type, name of an item must be string")

        with self.assertRaises(InitializationError) as context:
            Item(name="", quantity=12)
        self.assertEqual(str(context.exception),
                         "Invalid value, name of an item must be a non-empty alphanumeric string")

        with self.assertRaises(InitializationError) as context:
            Item(name="test 69*!", quantity=12)
        self.assertEqual(str(context.exception),
                         "Invalid value, name of an item must be a non-empty alphanumeric string")

        with self.assertRaises(InitializationError) as context:
            Item(name="test 1", quantity="")
        self.assertEqual(str(context.exception),
                         "Invalid Type, quantity of an item must be an integer")

        with self.assertRaises(InitializationError) as context:
            Item(name="test 1", quantity=0)
        self.assertEqual(str(context.exception),
                         "Invalid value, quantity of an item must be a non-zero positive integer")

        with self.assertRaises(InitializationError) as context:
            Item(name="test 1", quantity=-1)
        self.assertEqual(str(context.exception),
                         "Invalid value, quantity of an item must be a non-zero positive integer")

        with self.assertRaises(InitializationError) as context:
            Item(name="Item 69", quantity=12)
        self.assertEqual(str(context.exception),
                         "Item not found in catalogue")

    def test_price_of_newly_initailized_item(self):
        item_name = "Item 1"
        new_item = Item(name=item_name, quantity=10)
        catalogue_item_index = [
            item["name"] for item in catalogue].index(item_name)
        item_from_catalogue = catalogue[catalogue_item_index]
        self.assertEqual(item_from_catalogue["price"], new_item.price)

    def test_item_immutability(self) -> None:
        item = Item(name="Item 1", quantity=12)

        with self.assertRaises(AttributeError) as context:
            item.name = "Item 1"
        self.assertEqual(str(context.exception),
                         "property 'name' of 'Item' object has no setter")

        with self.assertRaises(AttributeError) as context:
            item.price = 12.2
        self.assertEqual(str(context.exception),
                         "property 'price' of 'Item' object has no setter")

        with self.assertRaises(AttributeError) as context:
            item.quantity = 12
        self.assertEqual(str(context.exception),
                         "property 'quantity' of 'Item' object has no setter")


if __name__ == "__main__":
    unittest.main()
