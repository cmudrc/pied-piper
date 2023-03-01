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
        result = {
            'pos': None,
            'delta_resource': None,
            }
        '''
        current_i = None
        result = None
        for i, action in enumerate(self.action_list):
            if action.is_current_action(date) is True:
                current_i = i
                if isinstance(action, Move):
                    result['pos'] = action.pos(date)
            elif action.is_done(date) is True:
                fuel = action.fuel_consumptio
        '''
        result['pos'] = self.pos(date)    
        result['delta_resource'] = self.fuel_consumption(date)
        current_i = self.current_action(date)
        self.action_list = self.action_list[current_i:]
        return result
    
    
    def current_action(self, date: Date):
        current_i = None
        for i, action in enumerate(self.action_list):
            if action.is_current_action(date) is True:
                current_i = i
        return current_i

    def pos(self, date: Date):
        pos = None
        for action in self.action_list:
            if isinstance(action, Move):
                if action.end_date <= date:
                    pos = action.end_pos
                elif action.is_current_action(date) is True:
                    pos = action.pos(date)
        return pos
    
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
