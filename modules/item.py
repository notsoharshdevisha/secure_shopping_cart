from fake_db.db import catalogue
from modules.alphanumeric import Alphanumeric
from modules.price import Price
from modules.quantity import Quantity


class Item:
    def __init__(self, name: Alphanumeric,  quantity: Quantity) -> None:
        if not isinstance(name, Alphanumeric):
            raise TypeError(
                "Invalid type, name of an Item must be an instance of Alphanumeric")

        if not self.is_item_present_in_catalogue(name.value):
            raise ValueError("Item not present in catalogue")

        if not isinstance(quantity, Quantity):
            raise TypeError(
                "Invalid type, quantity of an Item must be an instance of Quantity"
            )

        self._name = name
        # TODO get price from catalogue
        self._price = Price(value=0)
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

    def is_item_present_in_catalogue(self, item_name: str) -> bool:
        return item_name in [item["name"] for item in catalogue]
