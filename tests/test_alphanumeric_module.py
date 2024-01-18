import unittest

from modules.alphanumeric import Alphanumeric


class TestAlphanumericModule(unittest.TestCase):
    def test_alphanumeric_initialization(self) -> None:
        with self.assertRaises(TypeError) as context:
            Alphanumeric(value=1)
        self.assertEqual(str(context.exception),
                         "Invalid type, value must be a string")

        with self.assertRaises(ValueError) as context:
            Alphanumeric(value="")
        self.assertEqual(str(context.exception),
                         "value must be a non-empty string")

        with self.assertRaises(ValueError) as context:
            Alphanumeric(value="A Test 69 *")
        self.assertEqual(str(context.exception),
                         "value must be alphanumeric")

    def test_alphanumeric_immutability(self) -> None:
        string = Alphanumeric(value="123abc")
        with self.assertRaises(AttributeError) as context:
            string.value = "newval"
        self.assertEqual(str(context.exception),
                         "property 'value' of 'Alphanumeric' object has no setter")
