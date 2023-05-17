from piperabm.object import Object
from piperabm.unit import Date
from piperabm.actions.move import Move
from piperabm.actions.trade import Trade


class Queue(Object):

    def __init__(self):
        super().__init__()
        self.actions = []

    def add(self, action):
        """
        Add new *action* to *self.actions*
        """
        self.actions.append(action)

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
        move = self.last_action(type='move')
        return move.how_much_fuel(start_date, end_date)
    
    def last_action(self, type=None):
        """
        Return last action from *self.actions* list
        """

        def find_last(type):
            result = None
            for i in range(len(self.actions)): # checks all actions
            #for i in range(5): # checks last 5 actions
                index = -i - 1
                action = self.actions[index]
                if action.type == type and action.done is False:
                    result = action
            return result
        
        result = None
        if type is None:
            result = self.actions[-1]
        else:
            result = find_last(type)
        return result

    @property
    def done(self):
        """
        Is every action in *self.queue* already done?
        """
        result = True
        for action in self.actions:
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
