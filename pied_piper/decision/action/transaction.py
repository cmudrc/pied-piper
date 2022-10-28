try:
    from .action import Action
except:
    from action import Action


class Transaction(Action):

    def __init__(
        self,
        start_date,
        instant=False
    ):
        super().__init__(
            start_date,
            instant
        )