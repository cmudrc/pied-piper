from piperabm.unit import Date, DT
from piperabm.actions.action import Action


class Move(Action):

    def __init__(self, start_date: Date, path, transportation):
        super().__init__(
            start_date=start_date,
            duration=self.path.duration(self.transportation)
        )
        self.path = path
        self.transportation = transportation
        self.fuel_consumption = self.total_fuel_consumption()
        self.done = False
        self.type = 'move'

    def total_fuel_consumption(self):
        result = self.transportation.fuel_rate * self.duration
        return result

    def how_much_fuel(self, start_date: Date, end_date: Date):
        start_progress = self.progress(start_date)
        end_progress = self.progress(end_date)
        delta_progress = end_progress - start_progress
        delta_time = self.duration * delta_progress # in seconds
        travel_length = self.path.travel_length(delta_time, self.transportation)
        return self.transportation.how_much_fuel(travel_length)
    
    def is_possible(self, current_resource, start_date: Date, end_date: Date):
        result = True
        fuel_consumption = self.how_much_fuel(start_date, end_date)
        if fuel_consumption.is_bigger_than(current_resource):
            result = False
        return result

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
    from piperabm.actions import Move
    from piperabm.society.agent.config import Walk

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