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

        with self.assertRaises(TypeError) as context2:
            Price(value=0)
        self.assertEqual(
            str(context2.exception),
            "Invalid type, Price must be a positive non-zero number",
        )

        with self.assertRaises(ValueError) as context3:
            Price(value=0.0)
        self.assertEqual(
            str(context3.exception),
            "Price must be greater than 0.0"
        )


if __name__ == "__main__":
    unittest.main()
