import matplotlib.pyplot as plt


class TravelLength:

    def __init__(self):
        self.length_list = []
        self.duration_list = []

    def read(self, society, start_date, end_date):
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
    
    def to_plt(self):
        """
        Plot the travel length over time
        """
        def create_x():
            result = [0]
            for i, _ in enumerate(self.duration_list):
                val = sum(self.duration_list[0:i+1])
                result.append(val)
            return result

        def create_y():
            result = [0]
            for i, _ in enumerate(self.duration_list):
                val = sum(self.length_list[:i+1])
                result.append(val)
            return result
            
        title = "travel length vs. time"
        plt.title(title)
        plt.xlabel('Time')
        plt.ylabel('Travel Length')
        x = create_x()
        y = create_y()
        plt.plot(x, y, color='b', label='Travel Length')
        #plt.xlim([25, 50])
        plt.ylim(bottom=0)
        #plt.legend()

    def show(self):
        """
        Show the plt plot
        """
        self.to_plt()
        plt.show()        

'''
class TravelLength:

    def __init__(self):
        self.path_length_list = []

    def add(self, length):
        self.path_length_list.append(length)

    def average(self):
        return self.total() / len(self.path_length_list)
    
    def total(self):
        return sum(self.path_length_list)
'''


if __name__ == "__main__":
    pass