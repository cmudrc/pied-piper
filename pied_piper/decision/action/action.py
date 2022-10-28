class Action:

    def __init__(self, start_date, instant=True):
        self.start_date = start_date
        self.instant = instant
    
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