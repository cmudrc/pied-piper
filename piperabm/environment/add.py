class Add:

    def validate(self, new_item):
        name = new_item.name
        if name != '' and isinstance(name, str):
            name_result = self.find(name)
        id = new_item.id