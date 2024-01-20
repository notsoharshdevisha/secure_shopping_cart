import unittest

from modules.shopping_cart import ShoppingCart
from modules.update_error import UpdateError


class TestShoppingCart(unittest.TestCase):
    def test_shopping_cart_immutability(self) -> None:
        shopping_cart = ShoppingCart()

        with self.assertRaises(AttributeError) as context:
            shopping_cart.items = []
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

    def test_add_to_cart(self):
        shopping_cart = ShoppingCart()
        item_name = "Item 1"
        shopping_cart.add_to_cart(item_name)
        cart_items = shopping_cart.items
        self.assertEqual(cart_items[0]["name"], item_name)
        self.assertEqual(cart_items[0]["quantity"], 1)

        shopping_cart.add_to_cart(item_name)
        cart_items = shopping_cart.items
        self.assertEqual(cart_items[0]["name"], item_name)
        self.assertEqual(cart_items[0]["quantity"], 2)

        with self.assertRaises(UpdateError) as context:
            shopping_cart.add_to_cart("Item 69")
        self.assertEqual(str(context.exception),
                         "Could not add item to the cart because it was not found in the catalogue, The item must be from the catalogue")


if __name__ == "__main__":
    unittest.main()
