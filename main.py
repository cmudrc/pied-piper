#from environment.model import Entity
from environment.samples import e_1, e_2

class Simulation():
    def __init__(self, entities):
        self.environment = None
        for entity in entities:
            self.environment += entity
        
    def run(self):
        pass

    def run_step(self):
        pass

    def load(self):
        pass

    def save(self):
        pass
