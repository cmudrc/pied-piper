from piperabm.environment.structures import Settlement


def load_structure(dictionary: dict):
    if dictionary is None:
        structure = None
    else:
        type = dictionary['type']
        if type == 'settlement':
            structure = Settlement()
        structure.from_dict(dictionary)
    return structure