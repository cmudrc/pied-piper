class Queue:

    def __init__(self, actions:list=[]):
        self.actions = actions

    def add(self, action):
        self.actions.append(action)