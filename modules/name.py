import re


class Name:
    def __init__(self, name: str):
        if not isinstance(name, str):
            raise TypeError("Invalid type, Name must be a string")

        if not name:
            raise ValueError("Name must be a non-empty string")

        if len(name) > 80:
            raise ValueError("Name must be within 80 characters")

        if not re.match(r"^[a-zA-Z0-9 ]+$", name):
            raise ValueError("Name must be alphanumeric")

        self.name = name.strip()
