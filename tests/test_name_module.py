import unittest

from modules.name import Name


class TestNameModule(unittest.TestCase):
    def test_name_initialization(self):
        with self.assertRaises(TypeError) as context:
            Name(name=1)
        self.assertEqual(str(context.exception),
                         "Invalid type, Name must be a string")

        with self.assertRaises(ValueError) as context:
            Name(name="")
        self.assertEqual(str(context.exception),
                         "Name must be a non-empty string")
