from core.utils.unit_manager import Unit


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


class DynamicSource():
    """
    Resource production/use rate.

    Args:
        rate: rate of production/use
    """
    def __init__(self, rate=0):
        self.rate = rate
        self.current_amount = None
        
    def reset(self, delta_t):
        self.current_amount = self.rate * delta_t.days

    def sub(self, amount):
        self.current_amount -= amount
        if self.current_amount < 0:
            self.current_amount = 0


class Use(DynamicSource):
    def __init__(self, rate=0):
        super().__init__(
            rate=rate
        )


class Produce(DynamicSource):
    def __init__(self, rate=0):
        super().__init__(
            rate=rate
        )


class StaticSource():
    """
    Resource static storage.

    Args:
        current_amount: current amount
        max_amount: maximum amount
    """
    def __init__(self, current_amount=0, max_amount=0):
        self.current_amount = current_amount
        self.max_amount = max_amount

    def add(self, amount):
        self.current_amount += amount
        if self.current_amount > self.max_amount:
            self.current_amount = self.max_amount.copy()
    
    def sub(self, amount):
        self.current_amount -= amount
        if self.current_amount < 0:
            self.current_amount = 0


class Deficiency(StaticSource):
    def __init__(self, current_amount=0, max_amount=0):
        super().__init__(
            current_amount=current_amount,
            max_amount=max_amount
        )
    
    def is_alive(self):
        if self.current_amount > self.max_amount:
            return False
        else:
            return True


class Storage(StaticSource):
    def __init__(self, current_amount=0, max_amount=0):
        super().__init__(
            current_amount=current_amount,
            max_amount=max_amount
        )


if __name__ == "__main__":
    food = Resource(
        name='food',
        use=[Use(rate=0.1)],
        produce=[Produce(rate=0.5)],
        storage=[Storage(current_amount=0, max_amount=10)],
        deficiency=Deficiency(current_amount=0, max_amount=10)
    )