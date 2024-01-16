from typing import List, Type

from modules.item import Item


class ShoppingCart:
    def __init__(self, id: str, customer_id: str, items: List[Item]):
        if not isinstance(id, str) or not id:
            raise ValueError("Invalid id, must be a non-empty string")

        if not isinstance(customer_id, str) or not customer_id:
            raise ValueError("Invalid customer id, must be a non-empty string")

        if not self.are_instances(items, Item):
            raise TypeError(
                "Invalid type, items must be a list of instances of Item")

        self.id = id
        self.customer_id = customer_id
        self.cart = items

    def are_instances(self, item_list: List, expected_type: Type[Item]) -> bool:
        return all(isinstance(item, expected_type) for item in item_list)
