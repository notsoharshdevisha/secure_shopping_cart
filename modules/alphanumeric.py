import re


class Alphanumeric:
    def __init__(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Invalid type, value must be a string")

        if not value:
            raise ValueError("value must be a non-empty string")

        if not re.match(r"^[a-zA-Z0-9 ]+$", value):
            raise ValueError("value must be alphanumeric")

        self._value = value.strip()

    @property
    def value(self) -> str:
        return self._value
