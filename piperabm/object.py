class Object:
    """
    Contains global methods for classes 
    """

    def __str__(self) -> str:
        return str(self.to_dict())

    def __eq__(self, other) -> bool:
        result = False
        if self.to_dict() == other.to_dict():
            result = True
        return result
    
    def to_dict(self) -> dict:
        dictionary = {}
        print("NOT IMPLEMENTED YET")
        return dictionary
    
    def from_dict(self, dictionary: dict) -> None:
        print("NOT IMPLEMENTED YET")
