from piperabm.actions.move import Move
from piperabm.actions.trade import Trade


def load_action(dictionary: dict):
    if dictionary is None:
        action = None
    else:
        type = dictionary['type']
        if type == 'move':
            action = Move()
        elif type == 'trade':
            action = Trade()
        action.from_dict(dictionary)
    return action