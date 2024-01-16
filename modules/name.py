class Name:
    def __init__(self, name: str):
        if not isinstance(name, str):
            raise TypeError("Invalid type, Name must be a string")

        if not name:
            raise ValueError("Name must be a non-empty string")

        self.name = name
