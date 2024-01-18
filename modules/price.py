class Price:
    def __init__(self, value: float | int) -> None:

        if not isinstance(value, float | int):
            raise TypeError(
                "Invalid type, Price must be a positive non-zero number")

        if value < 0.0:
            raise ValueError("Price must be greater than 0.0")

        self._value = float(value)

    @property
    def value(self) -> float:
        return self._value
