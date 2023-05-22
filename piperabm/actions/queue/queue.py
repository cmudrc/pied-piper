from piperabm.object import Object
from piperabm.unit import Date, DT
from piperabm.actions.move import Move
from piperabm.actions.trade import Trade
from piperabm.actions.load import load_action


class Queue(Object):

    def __init__(self):
        super().__init__()
        self.actions = []
        ''' bindings '''
        self.agent_index = None
        self.environment = None
        self.society = None

    def add(self, action):
        """
        Add action (or a list of actions) to *self.actions*
        """
        if isinstance(action, list):
            for a in action:
                self.add(a)
        else:
            ''' bindings '''
            action.environment = self.environment
            action.society = self.society
            action.agent_index = self.agent_index
            ''' add '''
            self.actions.append(action)

    @property
    def end_date(self):
        """
        When will current actions in the queue finish?
        """
        action = self.last_action()
        return action.end_date
    
    def remaining(self, date: Date):
        """
        How long does it remain to finish the queue
        """
        if self.done is True:
            return DT(seconds=0)
        else:
            return self.end_date - date

    def __call__(self, index: int):
        return self.actions[index]
    
    def find_action(self, date: Date, actions: list = None):
        """
        Find the action that is happening in *date*
        """
        object = None
        index = None
        if actions is not None:
            actions_list = actions
        else:
            actions_list = self.actions
        for i, action in enumerate(actions_list):
            if action.is_current(date) is True:
                object = action
                index = i
                break
        return index, object
    
    def find_closest(self, date: Date):
        """
        Find the closest action in time
        """
        actions = self.filter(date=date)
        index, object = self.find_action(date, actions)
        if object is None:
            pass #######


    def pos(self, date: Date):
        """
        Return position of agent in *date*
        """
        ''' find nearst move action '''
        i, action = self.find_action(date)
        if action is None:
            pos = self.society.get_agent_pos(self.agent_index)
        else:
            if action.type != 'move':
                if i-1 in self.actions:
                    action = self.actions[i-1]
                else:
                    action = None
            if action is None:
                pos = self.society.get_agent_pos(self.agent_index)
            else:
                if action.end_date < date:
                    date = action.end_date
                pos = action.pos(date)
        return pos
    
    def update(self, start_date: Date, end_date: Date) -> None:
        recently_done = []
        for action in self.current:
            if action.end_date <= end_date:
                action.do()
                recently_done.append(action)
        return recently_done

    def filter(self, date: Date):
        result = []
        for action in self.actions:
            if action.start_date <= date:
                result.append(action)
        return result

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
    
    def filter_actions(self, type='all', current=None):
        """
        Filter and return the list of actions
        """
        result = []
        if current is None:
            actions = self.actions
        elif current is True:
            actions = self.current
        elif current is False:
            actions = self.history
        for action in actions:
            if type == 'all':
                result.append(action)
            elif type == 'move' and isinstance(action, Move):
                result.append(action)
            elif type == 'trade' and isinstance(action, Trade):
                result.append(action)
        return result
    
    def last_action(self, type='all'):
        """
        Return last action
        """
        result = None
        if type == 'all':
            result = self.actions[-1]
        else:
            actions = self.filter_actions(type)
            result = actions[-1]
        return result

    @property
    def done(self):
        """
        Check if all the actions are completed
        """
        result = True
        for action in self.actions:
            if action.done is False:
                result = False
                break
        return result
    
    def to_dict(self) -> list:
        dictionary = []
        for action in self.actions:
            dictionary.append(action.to_dict())
        return dictionary
    
    def from_dict(self, dictionary) -> None:
        self.actions = []
        for action_dictionary in dictionary:
            action = load_action(action_dictionary)
            self.add(action)


if __name__ == "__main__":
    queue = Queue()
    print(queue)