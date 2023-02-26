try: from .condition import conditions
except: from condition import conditions


class ElementExists:
    """
    Checks existance of an item in a certain duration of time
    """
    def __init__(self):
        self.conditions = conditions

    def vs(self, first, second):
        """
        Compare two values
        """
        result = None
        if first == second:
            result = '='
        elif first > second:
            result = '>'
        elif first < second:
            result = '<'
        return result

    def check(self, item_start, time_start, item_end=None, time_end=None):
        """
        Check condition result
        """
        if time_end is None:
            time_end = time_start
        if item_end is None:
            item_end = time_end
        if item_start > item_end or time_start > time_end:
            raise ValueError
        is_vs_ts = self.vs(item_start, time_start)
        is_vs_te = self.vs(item_start, time_end)
        ie_vs_ts = self.vs(item_end, time_start)
        ie_vs_te = self.vs(item_end, time_end)
        cs = self.find_condition(
            item_start_vs_time_start=is_vs_ts,
            item_start_vs_time_end=is_vs_te,
            item_end_vs_time_start=ie_vs_ts,
            item_end_vs_time_end=ie_vs_te
        )
        return cs.result

    def find_condition(self, item_start_vs_time_start, item_start_vs_time_end, item_end_vs_time_start, item_end_vs_time_end):
        """
        Search for the corresponding condition in the self.conditions based on entries
        """
        result = None
        for condition in self.conditions:
            if condition.is_vs_ts == item_start_vs_time_start and \
                    condition.is_vs_te == item_start_vs_time_end and \
                condition.ie_vs_ts == item_end_vs_time_start and \
                    condition.ie_vs_te == item_end_vs_time_end:
                result = condition
                break
        return result


if __name__ == "__main__":
    ee = ElementExists()
    result = ee.check(
        item_start=1,
        item_end=5,
        time_start=4,
        time_end=7
    )
    print(result)
