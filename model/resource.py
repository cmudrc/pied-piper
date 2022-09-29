class Resource():
    """
    Representes a resource. Each resource has capability of using, producing and storing.

    Args:
        name: name
        use: the rate of use
        produce: the rate of production
        storage_current: current amount of storage
        storage_max: maximum amount of storage
        deficiency_current: current amount of storage
        deficiency_max: maximum amount of deficiency

    """
    def __init__(self, name=None, use=0, produce=0, storage_current=0, storage_max=0, deficiency_current=0, decificiency_max=0):
        self.name = name
        self.use = use # per hour
        self.use_current = None # used for calculations
        self.produce = produce # per hour
        self.produce_current = None # used for calculations
        self.storage_current = storage_current
        self.storage_max = storage_max
        self.deficiency_current = deficiency_current
        self.deficiency_max = decificiency_max

    def __str__(self):
        return str(self.name)

    def reset(self):
        """
        Used for prepairing the instance at the beginning of each simulation step.
        
        """
        self.use_current = self.use.copy()
        self.produce_current = self.produce.copy()

    def update(self):
        """
        Used for updating the values at the end of each simulation step.
        
        """
        self.deficiency_current += self.use_current
        self.use_current = 0
        # remaning self.produce_current goes to waste
        self.produce_current = 0


if __name__ == "__main__":
    food = Resource(
        name='food',
        use=0.1,
        produce=0.5,
        storage_current=0,
        storage_max=10,
        deficiency_current=0,
        decificiency_max=10
    )