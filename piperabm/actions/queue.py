from piperabm.unit import Date

try:
    from .action import Move
except:
    from action import Move


class Queue:
    def __init__(self):
        self.action_list = []

    def add(self, action):
        self.action_list.append(action)

    def execute(self, date: Date):
        current_i = None
        result = None
        for i, action in enumerate(self.action_list):
            if action.is_current_action(date) is True:
                current_i = i
                if isinstance(action, Move):
                    result = action.pos(date), "pos"
        self.action_list = self.action_list[current_i:]
        return result