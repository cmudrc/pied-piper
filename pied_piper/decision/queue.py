class Queue:

    def __init__(self, actions:list=[]):
        self.actions = actions

    def add(self, action):
        self.actions.append(action)

    def validate_action_dates(self, actions):
        result = True
        for i, action in enumerate(actions):
            if i == 0:
                if action[i].start_date is None:
                    result = False
            else:
                if action[i].start_date < action[i-1].end_date:
                    result = False

    def bl(self, actions):
        """
        If no start_date 
        """
        
        for action in actions:
            if action.start_date:
                pass