import unittest

from modules.alphanumeric import Alphanumeric
from modules.item import Item
from modules.price import Price
from modules.quantity import Quantity
from modules.shopping_cart import ShoppingCart


class TestShoppingCart(unittest.TestCase):
    def test_shopping_cart_initialization(self):
        with self.assertRaises(TypeError) as context:
            ShoppingCart(items='cart')
        self.assertEqual(str(context.exception),
                         "Invalid type, items must be a list of instances of Item")

        valid_item = Item(
            name=Alphanumeric(value="test"),
            price=Price(value=2.3),
            quantity=Quantity(value=12)
        )
        invalid_item = "lol"
        invalid_item_list = [valid_item, invalid_item]
        with self.assertRaises(TypeError) as context:
            ShoppingCart(items=invalid_item_list)
        self.assertEqual(str(context.exception),
                         "Invalid type, items must be a list of instances of Item")


if __name__ == "__main__":
    unittest.main()
