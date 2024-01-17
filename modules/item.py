from modules.alphanumeric import Alphanumeric
from modules.price import Price
from modules.quantity import Quantity


class Item:
    def __init__(self, name: Alphanumeric, price: Price, quantity: Quantity) -> None:
        if not isinstance(name, Alphanumeric):
            raise TypeError(
                "Invalid type, name of an Item must be an instance of Alphanumeric")

        if not isinstance(price, Price):
            raise TypeError(
                "Invalid type, price of an Item must be an instance of Price")

        if not isinstance(quantity, Quantity):
            raise TypeError(
                "Invalid type, quantity of an Item must be an instance of Quantity"
            )

        self.name = name
        self.price = price
        self.quantity = quantity
