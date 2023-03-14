import os

class Test:
    def __init__(self):
        self.path = os.getcwd()
        self.dir = os.path.dirname(os.path.realpath(__file__))

    def get_dir(self):
        return os.path.dirname(self.path)
