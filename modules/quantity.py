class Quantity:
    def __init__(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError(
                "Invalid type, Quantity must be a positive non-zero integer")

        if value <= 0:
            raise ValueError("Quantity must be greater than 0")

        self._value = value

    @property
    def value(self) -> int:
        return self._value
