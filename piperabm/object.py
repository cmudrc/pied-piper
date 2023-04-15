class Object:

    def __str__(self) -> str:
        return str(self.to_dict())

    def __eq__(self, other) -> bool:
        result = False
        if self.to_dict() == other.to_dict():
            result = True
        return result