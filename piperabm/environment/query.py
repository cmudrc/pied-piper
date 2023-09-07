class Query:

    def get(self, input):
        """ Get item(s) as object(s) """
        result = None
        if isinstance(input, list):
            result = self.get_items_by_ids(input)
        elif isinstance(input, str):
            result = self.get_item_by_id(input)
        return result

    def get_item_by_id(self, input: str):
        """ Get item as object by its id """
        result = None
        if input in self.items:
            result = self.items[input]
        return result
    
    def get_items_by_ids(self, input: list) -> list:
        """ Get items as objects by their list of ids """
        result = []
        for id in input:
            item = self.get_object_by_id(id)
            if item is not None:
                result.append(item)
        return result


class Search:

    def find(self, input):
        """ Find and return item id based on input """
        result = None
        if isinstance(input, str):
            result = self.find_id_by_name(input)
        if isinstance(input, list):
            result = self.find_id_by_pos(input)
        return result

    def find_id_by_name(self, input: str) -> str:
        """ Find and return item id by the name """
        result = None
        for item in self.items:
            if item.name == input:
                result = item.id
                break
        return result
    
    def find_id_by_pos(self, input: list) -> str:
        """ Find and return item id by the pos """
        result = None
        for item in self.items:
            if item.pos == input:
                result = item.id
                break
        return result       


class Filter:
    
    def filter_items_by_type(self, input: str, items: list = None) -> list:
        """ Filter all objects of same type """
        result = []
        if items is None: items = self.items
        for item in items:
            if item.type == input:
                result.append(item.id)
        return result
    
    def filter_items_by_category(self, input: str, items: list = None) -> list:
        """ Filter all objects of same category (node/edge) """
        result = []
        if items is None: items = self.items
        for item in items:
            if item.type == input:
                result.append(item.id)
        return result