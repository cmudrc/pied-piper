def find_element(self, name, all_elements):
    """
    Find an element between a list of elements based on its name property
    """
    result = None
    for element in all_elements:
        if element.name == name:
            result = element
            break
    return result