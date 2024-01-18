import unittest

from modules.price import Price


class TestPriceModule(unittest.TestCase):
    def test_price_initialization(self) -> None:
        with self.assertRaises(TypeError) as context1:
            Price(value="Invalid")
        self.assertEqual(
            str(context1.exception),
            "Invalid type, Price must be a positive non-zero number",
        )

        with self.assertRaises(ValueError) as context3:
            Price(value=-0.1)
        self.assertEqual(
            str(context3.exception),
            "Price must be greater than 0.0"
        )

    def test_price_immutability(self) -> None:
        price = Price(value=10)
        with self.assertRaises(AttributeError) as context:
            price.value = 11
        self.assertEqual(str(context.exception),
                         "property 'value' of 'Price' object has no setter")


if __name__ == "__main__":
    unittest.main()
