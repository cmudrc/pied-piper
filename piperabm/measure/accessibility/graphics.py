import matplotlib.pyplot as plt


class Graphics:

    def to_plt(self, resource_name):
        """
        Plot the accessibility over time
        """
        def create_x():
            result = []
            for i, _ in enumerate(self.duration_list):
                val = sum(self.duration_list[1:i+1])
                result.append(val)
            return result

        def create_y():
            result_current = {
                'food': [],
                'water': [],
                'energy': [],
            }
            result_ideal = {
                'food': [],
                'water': [],
                'energy': [],
            }
            for i, _ in enumerate(self.duration_list):
                for name in result_current:
                    #current = self.total_current_resource_list[i].current_resource[name]
                    current = self.total_current_resource_list[i](name)
                    result_current[name].append(current)
                    #ideal = self.total_max_resource_list[i].current_resource[name]
                    ideal = self.total_max_resource_list[i](name)
                    result_ideal[name].append(ideal)
            return result_current, result_ideal

        title = resource_name + ' ' + "accessibility vs. time"
        plt.title(title)
        plt.xlabel('Time')
        plt.ylabel('Accessibity')
        x = create_x()
        y_current, y_ideal = create_y()
        plt.plot(x, y_current[resource_name], color='r', label='real')
        plt.plot(x, y_ideal[resource_name], color='b', label='ideal')
        #plt.xlim([25, 50])
        plt.ylim(bottom=0)
        plt.legend()

    def show(self, resource_name='all'):
        """
        Show the plt plot
        """
        if resource_name == 'all':
            for resource_name in ['food', 'water', 'energy']:
                self.to_plt(resource_name)
                plt.show()
        else:
            self.to_plt(resource_name)
            plt.show()