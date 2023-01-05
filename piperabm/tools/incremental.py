def name_gen(all_elements:list, default_name='element') -> str:

    all_names = []
    for element in all_elements:
        if isinstance(element, str):
            all_names.append(element)
        else:
            all_names.append(element.name)

    def find_index(name:str):
        name_parts = name.split('_')
        index = name_parts[-1]
        return int(index)

    indexes = []
    for name in all_names:
        index = find_index(name)
        indexes.append(index)
    
    i = 0
    while i <= len(indexes) + 1:
        if i not in indexes:
            new_index = i
            break
        i += 1
    name = default_name + '_' + str(new_index)
    return name


if __name__ == "__main__":
    all_names = ['cross_1']
    #all_names = []
    for i in range(3):
        new_name = name_gen(all_names, default_name='cross')
        all_names.append(new_name)
    print(all_names)