from tools import Unit


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
    def __init__(self, name=None, use=None, produce=None, storage=None, deficiency=None):
        self.name = name
        self.use = use
        self.produce = produce
        self.storage = storage
        self.deficiency = deficiency

        self.overall()

    def innter_transactions(self):
        for produce_case in self.produce:
            pass

    def add(self, amount):
        if amount > 0:      
            if self.deficiency is not None:
                if self.deficiency.current_amount < amount:
                    amount -= self.deficiency
                    self.deficiency = 0
                else:
                    self.deficiency -= amount
                    amount = 0

        if amount > 0:
            if self.use is not None:
                for use_case in self.use:
                    if use_case.current_amount < amount:
                        amount -= use_case.current_amount
                        use_case.current_amount = 0
                    else:
                        use_case.current_amount -= amount
                        amount = 0
                    if not amount > 0:
                        break

        if amount > 0:
            if self.storage is not None:
                for storage_case in self.storage:
                    if storage_case.current_amount < amount:
                        amount -= storage_case.current_amount
                        storage_case.current_amount = 0
                    else:
                        storage_case.current_amount -= amount
                        amount = 0
                    if not amount > 0:
                        break

    def update(self, delta_t):
        for use_case in self.use:
            use_case.current_amount
            use_case.reset(delta_t)
        
        for produce_case in self.produce:
            produce_case.reset(delta_t)

    def overall(self):
        self.overall_use = 0
        if self.use is not None:
            for use_case in self.use:
                self.overall_use += use_case.current_amount

        self.overall_produce = 0
        if self.produce is not None:
            for produce_case in self.produce:
                self.overall_produce += produce_case.current_amount

        self.overall_storage = 0
        self.overall_storage_max = 0
        if self.storage is not None:
            for storage_case in self.storage:
                self.overall_storage += storage_case.current_amount
                self.overall_storage_max += storage_case.max_amount  


if __name__ == "__main__":
    food = Resource(
        name='food',
        use=[Use(rate=0.1)],
        produce=[Produce(rate=0.5)],
        storage=[Storage(current_amount=0, max_amount=10)],
        deficiency=Deficiency(current_amount=0, max_amount=10)
    )