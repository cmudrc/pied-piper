import matplotlib.pyplot as plt


class Graphics:

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