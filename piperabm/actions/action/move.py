from piperabm.unit import Date, DT


class Move:
    def __init__(self, start_date: Date, start_pos, end_pos, adjusted_length, transportation):
        self.start_date = start_date
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.adjusted_length = adjusted_length
        self.transportation = transportation
        self.end_date  = self.calculate_end_date()

    def calculate_end_date(self):
        """
        Calculate end_date based on given data
        """
        travel_duration = self.adjusted_length / self.transportation.speed
        end_date = self.start_date + DT(seconds=travel_duration)
        return end_date

    def is_current_action(self, date: Date):
        """
        Assess whether the action is in the progress
        """
        if date > self.start_date and date < self.end_date:
            current = True
        else:
            current = False
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
        return (date - self.start_date).total_seconds() / (self.end_date - self.start_date).total_seconds() 