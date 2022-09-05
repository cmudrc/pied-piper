from environment.model1 import *
from environment.samples import e_1, e_2

class Simulation():
    def __init__(self, entities):
        self.environment = Model(
            name='test',
            entities=entities
        )
        
    def run(self):
        pass

    def run_step(self):
        pass

    def load(self):
        pass

    def save(self):
        pass
