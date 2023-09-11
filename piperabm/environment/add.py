class Add:

    def add(self, new_items):
        if isinstance(new_items, list):
            self.add_multiple(new_items)
        else:
            self.add_single(new_items)

    def add_single(self, new_item):
        if self.validate(new_item) is True:
            self.items[new_item.id] = new_item
        
    def add_multiple(self, new_items: list):
        for new_item in new_items:
            self.add_single(new_item)


class Validate:

    def validate(self, new_item):
        result = True
        validation_results = []
        validation_results.append(self.validate_name(new_item))
        validation_results.append(self.validate_pos(new_item))
        if len(validation_results) == 0 or \
            False in validation_results:
            result = False
        return result
    
    def validate_name(self, new_item):
        result = False
        new_name = new_item.name
        if new_name != '':
            name_result = self.find(new_name)
            if name_result is None:
                result = True
        return result

    def validate_pos(self, new_item):
        result = False
        new_pos = new_item.pos
        pos_result = self.find(new_pos)
        if pos_result is None:
            result = True
        return result
        