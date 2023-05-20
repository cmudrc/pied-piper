from piperabm.infrastructure import Settlement, Road


def load_structure(dictionary: dict):
    if dictionary is None:
        structure = None
    else:
        type = dictionary['type']
        if type == 'settlement':
            structure = Settlement()
        elif type == 'road':
            structure = Road()
        structure.from_dict(dictionary)
    return structure