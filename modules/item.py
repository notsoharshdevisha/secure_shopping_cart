from typing import Dict

from fake_db.db import catalogue
from modules.alphanumeric import Alphanumeric
from modules.price import Price
from modules.quantity import Quantity


class Item:
    def __init__(self, name: Alphanumeric,  quantity: Quantity) -> None:
        if not isinstance(name, Alphanumeric):
            raise TypeError(
                "Invalid type, name of an Item must be an instance of Alphanumeric")

        if not isinstance(quantity, Quantity):
            raise TypeError(
                "Invalid type, quantity of an Item must be an instance of Quantity"
            )

        item = self.get_item_from_catalogue(name.value)
        if not item:
            raise ValueError("Item not present in catalogue")

        self._name = name
        self._price = Price(value=item["price"])
        self._quantity = quantity

    @property
    def name(self) -> str:
        return self._name.value

    @property
    def price(self) -> float:
        return self._price.value

    @property
    def quantity(self) -> int:
        return self._quantity.value

    def get_item_from_catalogue(self, item_name: str) -> Dict[str, str | int] | None:
        try:
            index = [item["name"] for item in catalogue].index(item_name)
            return catalogue[index]
        except:
            return None
