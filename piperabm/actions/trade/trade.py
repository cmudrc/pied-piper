from piperabm.unit import Date, DT
from piperabm.tools import ElementExists


class Trade:

    def __init__(self, start_date: Date):
        self.start_date = start_date
        self.done = False
        self.duration = DT(seconds=0)

    '''
    def ready_for_trade(self, start_date: Date, end_date: Date):
        ee = ElementExists()
        exists = ee.check(
            item_start=self.start_date,
            item_end=self.start_date+self.duration,
            time_start=start_date,
            time_end=end_date
        )
        result = False
        if self.done is False and exists:
            result = True
        return result
    '''


if __name__ == "__main__":
    t = Trade(start_date=Date(2020, 1, 1))
    start_date = Date(2020, 1, 1) - DT(hours=6)
    end_date = Date(2020, 1, 1) + DT(hours=6)
    #t.done = True
    print(t.ready_for_trade(start_date, end_date))
    