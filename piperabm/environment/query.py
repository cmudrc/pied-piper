class Query:

    def get(self, id: int):
        """ Return object based on id """
        result = None
        for item in self.items:
            if item.id == id:
                result = item
                break
        return result

    def find(self, input):
        """ Find and return item id """
        result = None
        # find by id
        if isinstance(input, int):
            for item in self.items:
                if item.id == input:
                    result = item.id
                    break
        # find by pos
        if isinstance(input, list):
            pass
        # find by name
        if isinstance(input, str):
            for item in self.items:
                if item.name == input:
                    result = item.id
                    break
        return result

    def filter(self, type: str):
        """ Filter all objects of same type """
        result = []
        for item in self.items:
            if item.type == type:
                result.append(item.id)
        return result