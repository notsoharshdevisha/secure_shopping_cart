class Quantity:
    value_validation_message = "Invalid value, must be non-zero positive integer"

    def __init__(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError(
                "Invalid type, Quantity must be a positive non-zero integer")

        if value <= 0:
            raise ValueError("Quantity must be greater than 0")
        self.value = value
