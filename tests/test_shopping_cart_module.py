import unittest

from modules.alphanumeric import Alphanumeric
from modules.item import Item
from modules.price import Price
from modules.quantity import Quantity
from modules.shopping_cart import ShoppingCart


class TestShoppingCart(unittest.TestCase):
    def test_shopping_cart_initialization(self) -> None:
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

        with self.assertRaises(ValueError) as context:
            ShoppingCart(items=[valid_item])
        self.assertEqual(str(context.exception),
                         "item/s not present in the catalogue")

    def test_shopping_cart_immutability(self) -> None:
        item_list = [Item(
            name=Alphanumeric(value="Item 1"),
            price=Price(value=2.3),
            quantity=Quantity(value=12)
        )]
        shopping_cart = ShoppingCart(items=item_list)

        with self.assertRaises(AttributeError) as context:
            shopping_cart.items = item_list
        self.assertEqual(str(context.exception),
                         "property 'items' of 'ShoppingCart' object has no setter")

        with self.assertRaises(AttributeError) as context:
            shopping_cart.id = "test"
        self.assertEqual(str(context.exception),
                         "property 'id' of 'ShoppingCart' object has no setter")

        with self.assertRaises(AttributeError) as context:
            shopping_cart.customer_id = 'test'
        self.assertEqual(str(context.exception),
                         "property 'customer_id' of 'ShoppingCart' object has no setter")


if __name__ == "__main__":
    unittest.main()
