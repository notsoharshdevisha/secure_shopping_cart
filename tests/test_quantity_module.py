import unittest

from modules.quantity import Quantity


class TestQuantityModule(unittest.TestCase):
    def test_quantity_initialization(self) -> None:
        with self.assertRaises(TypeError) as context1:
            Quantity(value="invalid")
        self.assertEqual(
            str(context1.exception),
            "Invalid type, Quantity must be a positive non-zero integer",
        )

        with self.assertRaises(ValueError) as context2:
            Quantity(value=0)
        self.assertEqual(
            str(context2.exception),
            "Quantity must be greater than 0",
        )


if __name__ == "__main__":
    unittest.main()
