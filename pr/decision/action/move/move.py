from pr.tools import dt, date
#from pr.decision.action import Action
#try:
#    from .action import Action
#except:
#    from action import Action
#from pr.decision import action
from pr.decision.action.action import Action


class Move(Action):

    def __init__(
        self,
        start_date,
        path,
        transportation,
        instant=False
    ):
        self.path = path
        self.transportation = transportation
        end_date = start_date + self.action_duration(instant)
        super().__init__(
            start_date,
            end_date,
            instant
        )

    def add_path(self, pos, name=None, mode='linear', length=None):
        self.path.add(pos, name, mode, length)
        self.end_date = self.start_date + self.action_duration(self.instant)

    def pos(self, time: date):
        """
        Calculate position based on time.
        """
        result = None
        progress = self.progress(time)
        total_length = self.path.total_length()
        result = self.path.pos(total_length * progress)
        return result
    
    def action_duration(self, instant):
        """
        Total duration of the action.

        Returns:
            dt object
        """
        result = None
        if instant is True:
            result = dt(seconds=0)
        else:
            length = self.path.total_length()
            result = self.transportation.how_long(length)
        return result

    def when_reach(self):
        """
        Calculate the date in which the destination will be reached.
        """
        delta_t = self.action_duration()
        return self.start_date + delta_t

    def how_much_fuel(self, time):
        ##########
        self.total_fuel() * self.progress(time)

    def total_fuel(self):
        #########
        pass

    def origin(self, mode='name'):
        """
        Return info about the origin point.
        """
        return self.path.origin(mode)

    def destination(self, mode='name'):
        """
        Return info about the destination point.
        """
        return self.path.destination(mode)

    def __str__(self):
        txt = ''
        txt += 'from ' + self.origin() + ' '
        txt += 'to ' + self.destination()
        return txt


if __name__ == "__main__":
    from pr.decision.action.move import Path
    from pr.transportation import Foot


    path = Path()
    path.add(pos=[0, 0])
    path.add(pos=[0, 3])
    path.add(pos=[4, 3])

    m = Move(
        start_date=date(2020, 1, 1),
        path=path,
        transportation=Foot(),
        instant=True
    )