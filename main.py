from model.model import Model


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


if __name__ == "__main__":
    pass
