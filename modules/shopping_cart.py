import uuid
from typing import Dict, List, Type

from modules.item import Item
from utils.utility import generate_customer_id


class ShoppingCart:
    def __init__(self, items: List[Item]):

        if not self.are_instances(items, Item):
            raise TypeError(
                "Invalid type, items must be a list of instances of Item")

        self._id = uuid.uuid4()
        self._customer_id = generate_customer_id()
        self._items = items

    def are_instances(self, item_list: List, expected_type: Type[Item]) -> bool:
        return all(isinstance(item, expected_type) for item in item_list)

    @property
    def id(self) -> str:
        return str(self._id)

    @property
    def customer_id(self) -> str:
        return self._customer_id

    @property
    def items(self) -> List[Dict]:
        item_list_summary = []
        for (index, item) in enumerate(self._items):
            item_list_summary.append({"Sr No.": index + 1,
                                      "name": item.name,
                                      "price": item.price,
                                      "quantity": item.quantity})
        return item_list_summary
