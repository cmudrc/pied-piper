class Add:

    def add(self, new_item):
        if self.validate(new_item) is True:
            self.items[new_item.id] = new_item


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
        