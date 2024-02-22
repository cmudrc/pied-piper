from copy import deepcopy


class DeltaBool:
    """
    Create and apply delta for boolean variable
    """

    def create(old_variable: bool = None, new_variable: bool = None) -> bool:
        """ Create delta for boolean variable """
        delta = None
        if old_variable is None:
            if new_variable is None:
                pass
            else:
                action = 'addition'
                value = deepcopy(new_variable)
        else:
            if new_variable is None:
                action = 'delete'
                value = None
            
    
    def apply(old_variable: bool = None, delta: dict = None) -> bool:
        """ Create delta to boolean variable """
        action = delta['action']
        if action == 'addition':
            new_variable = deepcopy(delta['value'])
        elif action == 'modify':
            new_variable = deepcopy(delta['value'])
        elif action == 'delete':
            new_variable = None
        return new_variable


if __name__ == "__main__":
    old_variable = True
    new_variable = False
    delta = DeltaBool.create(new_variable, old_variable)
    print(delta)