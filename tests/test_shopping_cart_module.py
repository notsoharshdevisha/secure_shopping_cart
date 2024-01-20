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
        pass


if __name__ == "__main__":
    unittest.main()
