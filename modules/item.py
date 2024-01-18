from modules.alphanumeric import Alphanumeric
from modules.price import Price
from modules.quantity import Quantity


class Item:
    def __init__(self, name: Alphanumeric, price: Price, quantity: Quantity) -> None:
        if not isinstance(name, Alphanumeric):
            raise TypeError(
                "Invalid type, name of an Item must be an instance of Alphanumeric")

        if len(name.value) > 80:
            raise ValueError(
                "The name of an item must not be more than 80 characters long")

        if not isinstance(price, Price):
            raise TypeError(
                "Invalid type, price of an Item must be an instance of Price")

        if not isinstance(quantity, Quantity):
            raise TypeError(
                "Invalid type, quantity of an Item must be an instance of Quantity"
            )

        self._name = name
        self._price = price
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
