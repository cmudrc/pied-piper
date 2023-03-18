class Index:
    
    def __init__(self):
        self.index_list = []

    def find_next_index(self):
        """
        Check self.index_list (indexes) and suggest a new index
        """
        index_list = self.index_list
        if len(index_list) > 0:
            max_index = max(index_list)
            new_index = max_index + 1
        else:
            new_index = 0
        return new_index


if __name__ == "__main__":
    index_manager = Index()
    new_index = index_manager.find_next_index()
    print(new_index)
    index_manager.index_list.append(new_index)
    new_index = index_manager.find_next_index()
    print(new_index)