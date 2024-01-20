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

    def test_add_to_cart(self) -> None:
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

        with self.assertRaises(UpdateError) as context:
            for _ in range(69):
                shopping_cart.add_to_cart(item_name)
        self.assertEqual(str(context.exception),
                         f"quantity of an item should not be more than max allowed quantity for that item. The max allowed quantity for Item 1 is 21")

    def test_remove_from_cart(self) -> None:
        shopping_cart = ShoppingCart()
        item_name = "Item 3"
        with self.assertRaises(UpdateError) as context:
            shopping_cart.remove_from_cart(item_name)
        self.assertEqual(str(context.exception), "Item not present in cart")

        shopping_cart.add_to_cart(item_name)
        shopping_cart.remove_from_cart(item_name)
        self.assertEqual(len(shopping_cart.items), 0)

        shopping_cart.add_to_cart(item_name)
        shopping_cart.add_to_cart("Item 1")
        shopping_cart.remove_from_cart(item_name)
        is_still_present_in_cart = item_name in [
            item["name"] for item in shopping_cart.items]
        self.assertEqual(is_still_present_in_cart, False)

    def test_update_cart_item_quantity(self) -> None:
        shopping_cart = ShoppingCart()

        item_name = "Item 3"
        shopping_cart.add_to_cart(item_name)
        shopping_cart.update_item_quantity(item_name, 3)
        self.assertEqual(shopping_cart.items[0]["quantity"], 3)

        with self.assertRaises(UpdateError) as context:
            shopping_cart.update_item_quantity(item_name, 69)
        self.assertEqual(str(context.exception),
                         f"quantity of an item should not be more than max allowed quantity for that item. The max allowed quantity for Item 3 is 23")

        item_name = "Item 4"
        shopping_cart.add_to_cart(item_name)
        shopping_cart.update_item_quantity(item_name, 4)
        self.assertEqual(shopping_cart.items[1]["quantity"], 4)

        with self.assertRaises(UpdateError) as context:
            shopping_cart.update_item_quantity(item_name, 69)
        self.assertEqual(str(context.exception),
                         f"quantity of an item should not be more than max allowed quantity for that item. The max allowed quantity for Item 4 is 24")

        item_name = "Item 5"
        shopping_cart.add_to_cart(item_name)
        with self.assertRaises(UpdateError) as context:
            shopping_cart.update_item_quantity(item_name, "lol")
        self.assertEqual(str(context.exception),
                         "Invalid value, quantity of an item must be a positive non-zero integer")

        item_name = "Item 7"
        with self.assertRaises(UpdateError) as context:
            shopping_cart.update_item_quantity(item_name, "lol")
        self.assertEqual(str(context.exception),
                         "Item not present in cart")

    def test_get_cart_total(self) -> None:
        shopping_cart = ShoppingCart()
        shopping_cart.add_to_cart("Item 1")
        shopping_cart.add_to_cart("Item 1")
        shopping_cart.add_to_cart("Item 2")
        shopping_cart.add_to_cart("Item 3")
        total = shopping_cart.get_cart_total()
        self.assertEqual(total, 11 * 2 + 12 + 13)

        shopping_cart = ShoppingCart()
        total = shopping_cart.get_cart_total()
        self.assertEqual(total, 0)


if __name__ == "__main__":
    unittest.main()
