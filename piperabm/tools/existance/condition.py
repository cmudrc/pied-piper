class Condition:
    """
    A certain result of comparing input values
    """

    def __init__(
        self,
        symbol: str,
        result,
        item_start_vs_time_start: str,
        item_start_vs_time_end: str,
        item_end_vs_time_start: str,
        item_end_vs_time_end: str
    ):
        self.symbol = symbol
        self.result = result
        self.is_vs_ts = item_start_vs_time_start
        self.is_vs_te = item_start_vs_time_end
        self.ie_vs_ts = item_end_vs_time_start
        self.ie_vs_te = item_end_vs_time_end


conditions = [
    Condition(
        symbol='-[ ]-|--|--',
        result=False,
        item_start_vs_time_start='<',
        item_start_vs_time_end='<',
        item_end_vs_time_start='<',
        item_end_vs_time_end='<',
    ),
    Condition(
        symbol='--[ ]|--|--',
        result=False,
        item_start_vs_time_start='<',
        item_start_vs_time_end='<',
        item_end_vs_time_start='=',
        item_end_vs_time_end='<',
    ),
    Condition(
        symbol='--[|]--|--',
        result=True,
        item_start_vs_time_start='<',
        item_start_vs_time_end='<',
        item_end_vs_time_start='>',
        item_end_vs_time_end='<',
    ),
    Condition(
        symbol='--|[ ]--|--',
        result=True,
        item_start_vs_time_start='=',
        item_start_vs_time_end='<',
        item_end_vs_time_start='>',
        item_end_vs_time_end='<',
    ),
    Condition(
        symbol='--|-[ ]-|--',
        result=True,
        item_start_vs_time_start='>',
        item_start_vs_time_end='<',
        item_end_vs_time_start='>',
        item_end_vs_time_end='<',
    ),
    Condition(
        symbol='--|--[ ]|--',
        result=True,
        item_start_vs_time_start='>',
        item_start_vs_time_end='<',
        item_end_vs_time_start='>',
        item_end_vs_time_end='=',
    ),
    Condition(
        symbol='--|--[|]--',
        result=True,
        item_start_vs_time_start='>',
        item_start_vs_time_end='<',
        item_end_vs_time_start='>',
        item_end_vs_time_end='>',
    ),
    Condition(
        symbol='--|--|[ ]--',
        result=False,
        item_start_vs_time_start='>',
        item_start_vs_time_end='=',
        item_end_vs_time_start='>',
        item_end_vs_time_end='>',
    ),
    Condition(
        symbol='--|--|-[ ]-',
        result=False,
        item_start_vs_time_start='>',
        item_start_vs_time_end='>',
        item_end_vs_time_start='>',
        item_end_vs_time_end='>',
    ),
    Condition(
        symbol='--|[ ]|--',
        result=True,
        item_start_vs_time_start='=',
        item_start_vs_time_end='<',
        item_end_vs_time_start='>',
        item_end_vs_time_end='=',
    ),
    Condition(
        symbol='--|[--|-]-',
        result=True,
        item_start_vs_time_start='<',
        item_start_vs_time_end='<',
        item_end_vs_time_start='>',
        item_end_vs_time_end='>',
    ),
    Condition(
        symbol='-[-|--]|--',
        result=True,
        item_start_vs_time_start='<',
        item_start_vs_time_end='<',
        item_end_vs_time_start='>',
        item_end_vs_time_end='=',
    ),
    Condition(
        symbol='-[-|--|-]-',
        result=True,
        item_start_vs_time_start='=',
        item_start_vs_time_end='<',
        item_end_vs_time_start='>',
        item_end_vs_time_end='>',
    ),
    Condition(
        symbol='-[ ]||--',
        result=True,
        item_start_vs_time_start='<',
        item_start_vs_time_end='<',
        item_end_vs_time_start='=',
        item_end_vs_time_end='=',
    ),
    Condition(
        symbol='--||[ ]-',
        result=False,
        item_start_vs_time_start='=',
        item_start_vs_time_end='=',
        item_end_vs_time_start='>',
        item_end_vs_time_end='>',
    )
]
