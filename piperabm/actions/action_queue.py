from piperabm.unit import Date

try: from .action import Move
except: from action import Move
try: from .action import Trade
except: from action import Trade


class Queue:
    def __init__(self):
        self.action_list = []

    def add(self, action):
        """
        Add new *action* to *self.action_list*
        """
        self.action_list.append(action)

    def pos(self, start_date: Date=None, end_date: Date=None):
        """
        Return position of agent in *date*
        """
        if end_date is None: raise ValueError
        actions = self.find_actions('move')
        move = actions[0]
        pos = None
        pos = move.pos(end_date) # *pos* at *end_date*
        return pos
    
    def find_actions(self, type='all'):
        result = []
        for action in self.action_list:
            if isinstance(action, Move):
                if type == 'move' or type == 'all':
                    result.append(action)
            elif isinstance(action, Trade):
                if type == 'trade' or type == 'all':
                    result.append(action)
        return result

    def how_much_fuel(self, start_date: Date, end_date: Date):
        actions = self.find_actions('move')
        move = actions[0]
        return move.how_much_fuel(start_date, end_date)
    
    def is_empty(self):
        result = False
        if len(self.action_list) == 0:
            result = True
        return result

    def done(self):
        result = True
        for action in self.action_list:
            if action.done is False:
                result = False
                break
        return result

    def is_done(self, date: Date):
        """
        Check if all the actions are completed
        """
        result = None
        if self.is_empty():
            result = True
        else:
            result_list = []
            for action in self.action_list:
                status = action.is_done(date)
                result_list.append(status)
            if False in result_list:
                result = False
            else:
                result = True
        return result

    def reset(self):
        """
        Reset *self.action_list*
        """
        self.action_list = []
    

    def fuel_consumption(self, date: Date):

        def add(input_1: dict, input_2: dict):

            def add_non_empty(input_1, input_2):
                result = {}
                for key in input_1:
                    if key in input_2:
                        result[key] = input_1[key] + input_2[key]
                    else:
                        result[key] = input_1[key]
                for key in input_2:
                    if key not in result:
                        result[key] = input_2[key]
                return result

            result = {}
            if len(input_1) == 0:
                if len(input_2) == 0:
                    pass
                else:
                    result = input_2
            else:
                if len(input_2) == 0:
                    result = input_1
                else:
                    result = add_non_empty(input_1, input_2)
            return result

        result = {}
        for action in self.action_list:
            if action.end_date <= date:
                result = add(result, action.fuel_consumption)
        return result
        

    def cumulative_resource_consumption(self, new, total={}):
        pass
