from piperabm.unit import Date, DT
from piperabm.tools import euclidean_distance


class Move:
    def __init__(self, start_date: Date, start_pos, end_pos, transportation, adjusted_length=None):
        self.start_date = start_date
        self.start_pos = start_pos
        self.end_pos = end_pos
        if adjusted_length is None:
            self.adjusted_length = euclidean_distance(*start_pos, *end_pos)
        else:
            self.adjusted_length = adjusted_length
        self.transportation = transportation
        self.duration = self.calculate_duration()
        self.end_date  = self.calculate_end_date()

    def calculate_end_date(self):
        """
        Calculate end_date based on given data
        """
        duration = self.calculate_duration()
        return self.start_date + duration

    def calculate_duration(self):
        duration = DT(
            seconds=self.adjusted_length/self.transportation.speed
        )
        return duration

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

    def pos(self, date: Date):
        """
        Calculate pos in the date between *self.start_date* and *self.end_date*
        """
        progress = self.progress(date)
        x = self.start_pos[0] + ((self.end_pos[0] - self.start_pos[0]) * progress)
        y = self.start_pos[1] + ((self.end_pos[1] - self.start_pos[1]) * progress)
        return [x, y]

    def progress(self, date: Date):
        result = None
        if date > self.start_date and date < self.end_date:
            result = (date - self.start_date).total_seconds() / (self.end_date - self.start_date).total_seconds()
        else:
            if date <= self.start_date:
                result = 0
            if date >= self.end_date:
                result = 1
        return result

    
if __name__ == "__main__":
    from piperabm.actions import Move, Walk

    start_date=Date.today()
    m = Move(
        start_date=start_date,
        start_pos=[-1800, 0],
        end_pos=[1800, 0],
        transportation=Walk()
    )

    end_date = start_date + DT(hours=1)
    print(m.how_much_fuel(start_date, end_date))
    print(m.pos(date=start_date), m.pos(date=end_date))