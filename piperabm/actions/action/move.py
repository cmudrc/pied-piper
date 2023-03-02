from piperabm.unit import Date, DT
from piperabm.tools import euclidean_distance


class Move:

    def __init__(self, start_date: Date, path, transportation):
        self.start_date = start_date
        self.path = path
        self.transportation = transportation
        self.duration = self.path.duration(self.transportation)
        self.end_date  = self.start_date + DT(seconds=self.duration)
        self.fuel_consumption = self.total_fuel_consumption()

    def total_fuel_consumption(self):
        result = {}
        for key in self.transportation.fuel_rate:
            result[key] = self.transportation.fuel_rate[key] * self.duration
        return result

    def how_much_fuel(self, start_date: Date, end_date: Date):
        start_progress = self.progress(start_date)
        end_progress = self.progress(end_date)
        progress = end_progress - start_progress
        duration = self.duration.total_seconds() * progress # in seconds
        return self.transportation.fuel_consumption(duration)

    def is_current_action(self, date: Date):
        """
        Assess whether the action is in the progress
        """
        progress = self.progress(date)
        if progress < 1 and progress > 0:
            current = True
        else:
            current = True
        return current

    def is_done(self, date: Date):
        result = False
        if self.progress(date) == 1:
            result = True
        return result

    def pos(self, date: Date):
        """
        Calculate pos in the *date*
        """
        return self.path.pos(date - self.start_date, self.transportation)

    def progress(self, date: Date):
        delta_time = date - self.start_date
        return self.path.progress(delta_time, self.transportation)

    
if __name__ == "__main__":
    from piperabm.actions import Move, Walk

    path=None
    start_date=Date.today()
    m = Move(
        start_date=start_date,
        path=path,
        transportation=Walk()
    )

    end_date = start_date + DT(hours=1)
    print(m.how_much_fuel(start_date, end_date))
    print(m.pos(date=start_date), m.pos(date=end_date))