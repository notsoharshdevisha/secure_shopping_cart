import uuid
from typing import Dict, List, Type

from fake_db.db import catalogue
from modules.item import Item
from utils.utility import generate_customer_id


class ShoppingCart:
    def __init__(self, items: List[Item] = []) -> None:

        if not self.are_instances(items, Item):
            raise TypeError(
                "Invalid type, items must be a list of instances of Item")

        if not self.are_all_items_present_in_catalogue(items):
            raise ValueError(
                "item/s not present in the catalogue")

        self._id = uuid.uuid4()
        self._customer_id = generate_customer_id()
        self._items = items

    @property
    def id(self) -> str:
        return str(self._id)

    @property
    def customer_id(self) -> str:
        return self._customer_id

    @property
    def items(self) -> List[dict]:
        return [{"Sr No.": index + 1,
                 "name": item.name,
                 "price": item.price,
                 "quantity": item.quantity}
                for index, item in enumerate(self._items)]

    def are_instances(self, item_list: List[Item], expected_type: Type[Item]) -> bool:
        return all(isinstance(item, expected_type) for item in item_list)

    def is_item_present_in_catalogue(self, item_name: str) -> bool:
        return item_name in [item["name"] for item in catalogue]

    def are_all_items_present_in_catalogue(self, item_list: List[Item]) -> bool:
        return all(self.is_item_present_in_catalogue(item.name) for item in item_list)
