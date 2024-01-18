import re
import unittest

from utils.utility import generate_customer_id


class TestUtilities(unittest.TestCase):

    def test_generate_customer_id_utility(self):
        customer_id = generate_customer_id()
        is_valid = re.match(
            r"^[a-zA-z]{3}\d{5}[a-zA-z]{2}-[A|Q]$",
            customer_id)
        self.assertEqual(not not is_valid, True)
