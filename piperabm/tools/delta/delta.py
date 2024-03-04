from copy import deepcopy
#from piperabm.tools.delta.terminology import terminology_short as terminology
from piperabm.tools.delta.terminology import terminology_full as terminology

class Delta:

    def create(old, new):
        delta = None
        if old is None:
            delta = {
                terminology['value']: new,
                terminology['command']: terminology['overwrite']
            }
        else: # old is not None
            if new is None:
                delta = {
                    terminology['value']: new,
                    terminology['command']: terminology['overwrite']
                }
            else: # old and new are not None
                if type(old) != type(new):
                    delta = {
                        terminology['value']: new,
                        terminology['command']: terminology['overwrite']
                    }
                else: # old and new have same types
                    if old != new:
                        if isinstance(old, bool):
                            delta = DeltaBool.create(old, new)
                        elif isinstance(old, (int, float)):
                            delta = DeltaNum.create(old, new)
                        elif isinstance(old, str):
                            delta = DeltaStr.create(old, new)
                        elif isinstance(old, dict):
                            delta = DeltaDict.create(old, new)
                        elif isinstance(old, list):
                            delta = DeltaList.create(old, new)
        return delta
    
    def apply(var, delta):
        if delta is not None:
            if var is None:
                if delta[terminology['command']] == terminology['overwrite']:
                    var = delta[terminology['value']]
            else:
                if isinstance(var, bool):
                    var = DeltaBool.apply(var, delta)
                elif isinstance(var, (int, float)):
                    var = DeltaNum.apply(var, delta)
                elif isinstance(var, str):
                    var = DeltaStr.apply(var, delta)
                elif isinstance(var, dict):
                    var = DeltaDict.apply(var, delta)
                elif isinstance(var, list):
                    var = DeltaList.apply(var, delta)
        return var


class DeltaBool:

    def create(old, new):
        delta = {
            terminology['value']: new,
            terminology['command']: terminology['overwrite']
        }
        return delta
    
    def apply(var, delta):
        if delta[terminology['command']] == terminology['overwrite']:
            var = delta[terminology['value']]
        return var


class DeltaNum:

    def create(old, new):
        delta = {
            terminology['value']: new - old,
            terminology['command']: terminology['change']
        }
        return delta
    
    def apply(var, delta):
        if delta[terminology['command']] == terminology['change']:
            var += delta[terminology['value']]
        elif delta[terminology['command']] == terminology['overwrite']:
            var = delta[terminology['value']]
        return var
    

class DeltaStr:

    def create(old, new):
        delta = {
            terminology['value']: new,
            terminology['command']: terminology['overwrite']
        }
        return delta
    
    def apply(var, delta):
        if delta[terminology['command']] == terminology['overwrite']:
            var = delta[terminology['value']]
        return var


class DeltaDict:

    def create(old: dict, new: dict):
        deltas_list = []
        old_keys = old.keys()
        new_keys = new.keys()
        keys_in_both = list(set(old_keys) & set(new_keys))
        keys_in_old_not_in_new = list(set(old_keys) - set(new_keys))
        keys_in_new_not_in_old = list(set(new_keys) - set(old_keys))
        # Possibility of change
        for key in keys_in_both:
            delta_value = Delta.create(old[key], new[key])
            if delta_value is not None:
                delta = {
                    terminology['key']: key,
                    terminology['command']: terminology['change'],
                    terminology['value']: delta_value
                }
                deltas_list.append(delta)
        # Deletion
        for key in keys_in_old_not_in_new:
            delta = {
                terminology['key']: key,
                terminology['command']: terminology['delete'],
            }
            deltas_list.append(delta)
        # Addition
        for key in keys_in_new_not_in_old:
            delta = {
                terminology['key']: key,
                terminology['value']: new[key],
                terminology['command']: terminology['add'],
            }
            deltas_list.append(delta)
        return deltas_list
    
    def apply(var: dict, delta):
        var = deepcopy(var)
        if isinstance(delta, dict):
            if delta[terminology['command']] == terminology['overwrite']:
                var = delta[terminology['value']]
        elif isinstance(delta, list):
            for action in delta:
                key = action[terminology['key']]
                command = action[terminology['command']]
                if command == terminology['add']:
                    var[key] = action[terminology['value']]
                elif command == terminology['change']:
                    var[key] = Delta.apply(var[key], action[terminology['value']])
                elif command == terminology['delete']:
                    var.pop(key, None)
        return var
    

class DeltaList:

    def create(old, new):
        old = DeltaList._list_to_dict(old)
        new = DeltaList._list_to_dict(new)
        return DeltaDict.create(old, new)

    def apply(var, delta):
        var = DeltaList._list_to_dict(var)
        new = DeltaDict.apply(var, delta)
        return DeltaList._dict_to_list(new)

    def _list_to_dict(input: list) -> dict:
        """ Convert list to dictionary """
        result = {}
        for i, item in enumerate(input):
            result[i] = item
        return result

    def _dict_to_list(input: dict) -> list:
        """ Convert dictionary to list """
        result = None
        if input is not None:
            result = []
            for i in input:
                result.append(input[i])
        return result


if __name__ == "__main__":
    old = {'a': 1, 'b': 2}
    new = {'b': 3, 'c': 4}
    delta = Delta.create(old, new)
    print('Delta: ', delta)
    print('Updated Variable: ', Delta.apply(old, delta))
