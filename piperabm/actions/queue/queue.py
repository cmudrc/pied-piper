from piperabm.object import Object
from piperabm.unit import Date
from piperabm.actions.move import Move
from piperabm.actions.trade import Trade
from piperabm.actions.load import load_action


class Queue(Object):

    def __init__(self):
        super().__init__()
        self.actions = []

    def add(self, action):
        """
        Add new *action* to *self.actions*
        """
        self.actions.append(action)

    def __call__(self, index: int):
        return self.actions[index]

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

    @property
    def history(self):
        """
        Return completed actions in reverse format
        """
        result = []
        for i in range(self.break_index):
            result.append(self.actions[i])
        result.reverse()
        return result

    @property
    def current(self):
        """
        Return current actions
        """
        result = []
        for i in range(self.break_index, self.size):
            result.append(self.actions[i])
        return result
    
    @property
    def size(self):
        """
        Return total number of actions
        """
        return len(self.actions)

    @property
    def break_index(self):
        """
        Calculate the index in *self.actions* list that separates current and
        completed actions
        """
        break_index = self.size
        for i in range(self.size): # checks all actions
        #for i in range(5): # checks last 5 actions
            index = -i - 1
            action = self.actions[index]
            if action.done is False:
                break_index -= 1
            else:
                break
        return break_index
    
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
    
    def to_dict(self) -> list:
        dictionary = []
        for action in self.actions:
            dictionary.append(action.to_dict())
        return dictionary
    
    def from_dict(self, dictionary) -> None:
        actions = []
        for action_dictionary in dictionary:
            action = load_action(action_dictionary)
            actions.append(action)
        self.actions = actions


if __name__ == "__main__":
    queue = Queue()
    print(queue)