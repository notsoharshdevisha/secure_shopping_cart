from typing import Dict

from fake_db.db import catalogue
from modules.alphanumeric import Alphanumeric
from modules.initialization_error import InitializationError
from modules.price import Price
from modules.quantity import Quantity


class Item:
    def __init__(self, name: str,  quantity: int) -> None:

        try:
            self._name = Alphanumeric(value=name)
        except TypeError:
            raise InitializationError(
                "Invalid Type, name of an item must be string")
        except ValueError:
            raise InitializationError(
                "Invalid value, name of an item must be a non-empty alphanumeric string")

        try:
            self._quantity = Quantity(value=quantity)
        except TypeError:
            raise InitializationError(
                "Invalid Type, quantity of an item must be an integer")
        except ValueError:
            raise InitializationError(
                "Invalid value, quantity of an item must be a non-zero positive integer")

        item = self.get_item_from_catalogue(name)
        if not item:
            raise InitializationError("Item not found in catalogue")

        try:
            self._price = Price(value=item["price"])
        except TypeError:
            raise InitializationError(
                "Invalid type, price of an item must be a number")
        except ValueError:
            raise InitializationError(
                "Invalid value, price of an item must be a positive number"
            )

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
