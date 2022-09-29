class Resource():
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