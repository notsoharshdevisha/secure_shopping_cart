import uuid
from typing import List, Type

from modules.item import Item
from utils.utility import generate_customer_id


class ShoppingCart:
    def __init__(self, items: List[Item] = []) -> None:

        if not self.are_instances(items, Item):
            raise TypeError(
                "Invalid type, items must be a list of instances of Item")

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

    def is_item_present_in_cart(self, item_name) -> int | None:
        item_name_list = [item["name"] for item in self.items]
        try:
            return item_name_list.index(item_name)
        except:
            return None

    def add_to_cart(self, item_name: str) -> None:
        index = self.is_item_present_in_cart(item_name)
        if index:
            # TODO update item quantity
            pass
        else:
            # TODO add to cart
            pass
