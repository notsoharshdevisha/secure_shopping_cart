import uuid
from typing import List, Type

from modules.initialization_error import InitializationError
from modules.item import Item
from modules.update_error import UpdateError
from utils.utility import generate_customer_id


class ShoppingCart:
    def __init__(self) -> None:
        self._id = uuid.uuid4()
        self._customer_id = generate_customer_id()
        self._items = []

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

    def is_item_present_in_cart(self, item_name) -> int | None:
        item_name_list = [item["name"] for item in self.items]
        try:
            return item_name_list.index(item_name)
        except:
            return None

    def add_to_cart(self, item_name: str) -> None:
        index = self.is_item_present_in_cart(item_name)
        if isinstance(index, int):
            concerned_item = self._items[index]
            new_quantity = concerned_item.quantity + 1
            concerned_item.update_quantity(new_quantity)
        else:
            try:
                new_item = Item(name=item_name, quantity=1)
            except InitializationError:
                raise UpdateError(
                    "Could not add item to the cart because it was not found in the catalogue, The item must be from the catalogue")
            self._items.append(new_item)

    def remove_from_cart(self, item_name: str) -> None:
        pass
