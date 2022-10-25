try:
    from ..tools import dt
except:
    from tools import dt


class Action:

    def __init__(self, start_date):
        self.start_date = start_date
    
    def progress(self, time):
        """
        Calculate the progress ratio in the desired time

        Args:
            time: a datetime object

        Returns:
            float value between 0 and 1
        """
        return None

    def status(self, time):
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


class Move(Action):

    def __init__(
        self,
        start_date,
        path,
        transportation,
        instant=False
    ):
        super().__init__(
            start_date
        )
        '''
        self.start_point = start_point
        self.start_pos = None
        self.end_point = end_point
        self.end_pos = None
        '''
        self.path = path
        self.transportation = transportation
        self.instant = instant

    def progress(self, time):
        """
        Calculate the progress ratio in the desired time

        Args:
            time: a datetime object

        Returns:
            float value between 0 and 1
        """
        result = None
        if self.instant:
            if self.start_date > time:
                result = 0
            else:
                result = 1
        else:
            if self.start_date > time:
                result = 0
            else:
                delta_t = time - self.start_date
                speed = self.transportation.speed
                current_length = speed * delta_t.seconds
                result = self.path.progress(current_length)
        return result

    def pos(self, time):
        """
        Calculate position based on time.
        """
        result = None
        if self.instant:
            if self.start_date < time:
                result = self.origin(mode='pos')
            else:
                result = self.destination(mode='pos')
        else:
            delta_t = time - self.start_date
            speed = self.transportation.speed
            current_length = speed * delta_t
            result = self.path.pos(current_length)
        return result
    
    def action_duration(self):
        """
        Total duration of the action.
        """
        result = None
        if self.instant:
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


class Queue:

    def __init__(self, actions:list=[]):
        self.actions = actions

    def add(self, action):
        self.actions.append(action)