try:
    from .action import Action
except:
    from action import Action


class Package:

    def __init__(self, resource_name, amount):
        self.resource_name = resource_name
        self.amount = amount
        

class Transaction(Action):

    def __init__(
        self,
        start_date,
        package,
        instant=True
    ):
        super().__init__(
            start_date,
            instant
        )
