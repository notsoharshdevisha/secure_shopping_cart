import unittest

from modules.alphanumeric import Alphanumeric


class TestAlphanumericModule(unittest.TestCase):
    def test_alphanumeric_initialization(self):
        with self.assertRaises(TypeError) as context:
            Alphanumeric(value=1)
        self.assertEqual(str(context.exception),
                         "Invalid type, value must be a string")

        with self.assertRaises(ValueError) as context:
            Alphanumeric(value="")
        self.assertEqual(str(context.exception),
                         "value must be a non-empty string")

        with self.assertRaises(ValueError) as context:
            Alphanumeric(value="a"*81)
        self.assertEqual(str(context.exception),
                         "value must be within 80 characters")

        with self.assertRaises(ValueError) as context:
            Alphanumeric(value="A Test 69 *")
        self.assertEqual(str(context.exception),
                         "value must be alphanumeric")
