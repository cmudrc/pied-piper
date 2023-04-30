from piperabm.transporation.walk import Walk
from piperabm.transporation.vehicle import Vehicle


def load_transportation(dictionary: dict):
    type = dictionary['type']
    if type == 'walk':
        transportation = Walk()
    elif type == 'vehicle':
        transportation = Vehicle()
    transportation.from_dict(dictionary)
    return transportation
