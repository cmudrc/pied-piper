class Path:

    def __init__(self, infrastructure):
        self.G = self.create(infrastructure)
        self.environment = infrastructure.environment

    def create(self, infrastructure):
        pass