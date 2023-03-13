try: from .graphics import Graphics
except: from graphics import Graphics


class TravelLength(Graphics):

    def __init__(self):
        self.length_list = []
        self.duration_list = []
        super().__init__()

    def add_data(self, society, start_date, end_date):
        """
        Read all the required parameters from society
        """
        length = None #############
        duration = end_date - start_date
        self.add(length, duration)

    def add(self, length, duration):
        self.length_list.append(length)
        self.duration_list.append(duration)
    
    def total(self):
        """
        Total traveled length
        """
        result = 0
        if len(self.length_list) > 0:
            result = sum(self.length_list)
        return result     


if __name__ == "__main__":
    pass