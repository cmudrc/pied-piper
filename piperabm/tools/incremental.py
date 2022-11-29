def name_gen(all_names:list, default_name='element') -> str:

    def split(name:str):
        name_parts = name.split('_')
        main_part = name_parts[:-1]
        index = name_parts[-1]
        main = ''
        for part in main_part:
            main += part + '_'
        return main[:-1], index

    prefixes = {}
    if all_names is None or len(all_names) == 0:
        prefixes[default_name] = []
    for name in all_names:
        main, index = split(name)
        if main not in prefixes: prefixes[main] = [index]
        else: prefixes[main].append(index)
    
    def find_popular_prefix(prefixes):
        popular_prefix = None
        popular_prefix_length = -1
        for prefix in prefixes:
            if len(prefixes[prefix]) > popular_prefix_length:
                popular_prefix_length = len(prefixes[prefix])
                popular_prefix = prefix
        return popular_prefix
    
    prefix = find_popular_prefix(prefixes)
    indexes = prefixes[prefix]
    
    i = 0
    while i <= len(indexes) + 1:
        if str(i) not in indexes:
            index = i
            break
        i += 1
    
    return prefix + '_' + str(index)
        

if __name__ == "__main__":
    all_names = ['a_0', 'a_1', 'a_2', 'b_2']
    #all_names = []
    for i in range(3):
        new_name = name_gen(all_names)
        all_names.append(new_name)
    print(all_names)