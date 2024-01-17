import uuid
from typing import List, Type

from modules.item import Item
from utils.utility import generate_customer_id


class ShoppingCart:
    def __init__(self, items: List[Item]):

        if not self.are_instances(items, Item):
            raise TypeError(
                "Invalid type, items must be a list of instances of Item")

        self.id = uuid.uuid4()
        self.customer_id = generate_customer_id()
        self.cart = items

    def are_instances(self, item_list: List, expected_type: Type[Item]) -> bool:
        return all(isinstance(item, expected_type) for item in item_list)
