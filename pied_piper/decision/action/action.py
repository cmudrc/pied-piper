from datetime import datetime as date


class Action:

    def __init__(self, start_date: date, end_date: date=None, instant=True):
        self.start_date, self.end_date, self.instant = self.refine_inputs(start_date, end_date, instant)

    def refine_inputs(self, start_date, end_date, instant):
        if start_date is not None:
            if instant is True: end_date = start_date
            else:
                if end_date is not None:
                    if start_date > end_date: raise ValueError
                else:
                    raise ValueError
        else:
            raise ValueError
        return start_date, end_date, instant
    
    def progress(self, time: date):
        """
        Calculate the progress ratio in the desired time

        Args:
            time: a datetime object

        Returns:
            float value between 0 and 1
        """
        duration = self.duration().total_seconds()
        progress = (time - self.start_date).total_seconds() / duration
        if progress > 1: progress = 1
        elif progress < 0: progress = 0
        return progress

    def duration(self):
        return self.end_date - self.start_date

    def status(self, time: date):
        result = None
        prog = self.progress(time)
        if prog is not None:
            if prog == 0:
                result = 'not started'
            elif prog == 1:
                result = 'done'
            else:
                result = 'in progress'
        return result


if __name__ == "__main__":

    from datetime import timedelta as dt


    start_date = date(2000, 1, 1)
    end_date = date(2000, 1, 3)
    a = Action(start_date, end_date, instant=False)
    print(a.progress(start_date + dt(days=1)))