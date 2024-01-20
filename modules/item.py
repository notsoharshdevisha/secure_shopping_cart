from typing import Dict

from fake_db.db import catalogue
from modules.alphanumeric import Alphanumeric
from modules.initialization_error import InitializationError
from modules.price import Price
from modules.quantity import Quantity
from modules.update_error import UpdateError


class Item:
    def __init__(self, name: str,  quantity: int) -> None:
        try:
            self._name = Alphanumeric(value=name)
        except (TypeError, ValueError):
            raise InitializationError(
                "Invalid value, name of an item must be a non-empty alphanumeric string")

        valid_quantity = None
        try:
            valid_quantity = Quantity(value=quantity)
        except (TypeError, ValueError):
            raise InitializationError(
                "Invalid value, quantity of an item must be a positive non-zero integer")

        item = self.get_item_from_catalogue(name)
        if not item:
            raise InitializationError("Item not found in catalogue")

        if valid_quantity.value > item["max_allowed_quantity"]:
            raise InitializationError(
                f"quantity of an item should not be more than max allowed quantity for that item. The max allowed quantity for {item['name']} is {item['max_allowed_quantity']}")

        self._quantity = valid_quantity

        try:
            self._price = Price(value=item["price"])
        except (TypeError, ValueError):
            raise InitializationError(
                "Invalid value, price of an item must be a positive number")

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

    def update_quantity(self, new_quantity) -> None:
        new_valid_quantity = None
        try:
            new_valid_quantity = Quantity(value=new_quantity)
        except (TypeError, ValueError):
            raise UpdateError(
                "Invalid value, quantity of an item must be a positive non-zero integer")

        item = self.get_item_from_catalogue(self.name)
        if item and (new_valid_quantity.value > item["max_allowed_quantity"]):
            raise UpdateError(
                f"quantity of an item should not be more than max allowed quantity for that item. The max allowed quantity for {item['name']} is {item['max_allowed_quantity']}")

        self._quantity = new_valid_quantity

    def is_more_than_max_allowed_quantity(self):
        pass
