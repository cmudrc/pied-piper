import matplotlib.pyplot as plt


class Accessibility:

    name = 'accessibility'
    category = 'measure'

    def __init__(self):
        self.library = {}
        self.dates = []
        self.measures = None  # Binding
        self.resource_names = ['food', 'water', 'energy']

    @property
    def model(self):
        return self.measures.model
    
    @property
    def len(self):
        """
        Return number of entries
        """
        return len(self.dates) - 1
    
    @property
    def agents(self):
        """
        Return a list of agents id
        """
        return list(self.library.keys())
    
    def agent_resource_accessilibity(self, id, resource_name):
        """
        Return accessibility values for each agent and each resource
        """
        resources_values = self.library[id]
        values = []
        for resources_value in resources_values:
            values.append(resources_value[resource_name])
        return values
    
    def agent_resources_accessibility(self, id):
        """
        Return accessibility values for each agent and for all its resources
        """
        resources_values = self.library[id]
        values = []
        for resources_value in resources_values:
            agent_resources_value = []
            for resource_name in self.resource_names:
                agent_resources_value.append(resources_value[resource_name])
            values.append(average_geometric(agent_resources_value))
        return values
    
    def agents_resource_accessibility(self, resource_name):
        """
        Return accessibility values for a resource for across agents
        """
        values = []
        for i in range(self.len):
            agent_resource_values = []
            for id in self.agents:
                agent_resource_values.append(self.library[id][i][resource_name])
            values.append(average(agent_resource_values))
        return values

    def agents_resources_accessibility(self):
        """
        Return accessibility values for all resources for across agents
        """
        values = []
        for i in range(self.len):
            agent_resource_value = []
            for resource_name in self.resource_names:
                agent_resource_values = []
                for id in self.agents:
                    agent_resource_values.append(self.library[id][i][resource_name])
                agent_resource_value.append(average(agent_resource_values))
            values.append(average_geometric(agent_resource_value))
        return values

    @property
    def xs(self):
        """
        Convert dates to xs for plotting
        """
        xs_raw = self.dates[1:]
        xs = []
        for x in xs_raw:
            # Date part
            date_part = str(x.month) + "/" + str(x.day) + "/" + str(x.year)
            # Hour part
            hour = str(x.hour)
            if len(hour) < 2:
                hour = "0" + hour
            minute = str(x.minute)
            if len(minute) < 2:
                minute = "0" + minute
            hour_part = hour + ":" + minute
            # Date and Hour parts combined
            x_formatted = date_part + "\n" + hour_part
            xs.append(x_formatted)
        return xs

    def average(self, values):
        """
        Calculate average accessibility
        """
        accessibilities = []
        for i in range(self.len):
            delta_time = self.dates[i + 1] - self.dates[i]
            accessibility_i = delta_time.total_seconds() * values[i]
            accessibilities.append(accessibility_i)
        duration = self.dates[-1] - self.dates[0]
        return sum(accessibilities) / duration.total_seconds()
    
    def read(self):
        """
        Read current data from model
        """
        self.dates.append(self.model.current_date)
        # There has to be one more members in date than accessibility values
        if len(self.dates) > 1:
            accessibility = None ###################
            self.values.append(accessibility)
    
    def show(self, scale_y=False, average=True, id='all', resource_name='all'):
        """
        Show the data as plot
        """
        xs = self.xs
        if id == 'all':
            if resource_name == 'all':
                ys = self.agents_resources_accessibility()
                title = self.name + " " + "over time"
            else:
                ys = self.agents_resource_accessibility(resource_name)
                title = resource_name + " " + self.name + " " + "over time"
        else:
            if resource_name == 'all':
                ys = self.agent_resources_accessibility(id)
                title = self.name + " " + "over time"
            else:
                ys = self.agent_resource_accessilibity(id, resource_name)
                title = resource_name + " " + self.name + " " + "over time"

        plt.plot(xs, ys)

        """ Title """
        plt.title(
            '"' + title + '"',
            #fontsize=14,
            fontweight='bold',
        )

        """ Labels and Ticks """
        plt.xlabel(
            "date",
            #fontsize=14,
            fontweight='bold',
        )
        plt.ylabel(
            "accessibility",
            #fontsize=14,
            fontweight='bold',
        )
        plt.xticks(fontsize=8)
        #plt.yticks(fontsize=ticks_font_size)
        if scale_y is False:
            plt.ylim(0, 1)

        """ Adjust spacing """
        plt.subplots_adjust(
            bottom=0.15,
            right=0.9,
            top=0.9,
        )

        """ Extra info """
        if average is True:
            plt.text(
                0.95,
                0.95,
                "average: {:.2f}".format(self.average(ys)),
                horizontalalignment='right',
                verticalalignment='top',
                transform=plt.gca().transAxes,
                fontsize=12,
                bbox={
                    'facecolor': 'white',
                    'alpha': 0.5,
                }
            )

        plt.show()


def average_geometric(values):
    total = 1
    for value in values:
        total *= value
    total = total ** (1 / len(values))
    return total


def average(values):
    return sum(values) / len(values)

    
if __name__ == "__main__":

    from piperabm.time import Date

    measure = Accessibility()
    measure.library = {
        1: [
            {
                'food': 1,
                'water': 1,
                'energy': 1,
            },
            {
                'food': 0.9,
                'water': 0.8,
                'energy': 0.7,
            },
            {
                'food': 0.8,
                'water': 0.7,
                'energy': 0.6,
            },
            {
                'food': 0.7,
                'water': 0.6,
                'energy': 0.5,
            },
            {
                'food': 0.6,
                'water': 0.5,
                'energy': 0.4,
            },
        ],
        2: [
            {
                'food': 0.8,
                'water': 0.7,
                'energy': 0.6,
            },
            {
                'food': 0.5,
                'water': 0.6,
                'energy': 0.4,
            },
            {
                'food': 0.2,
                'water': 0.4,
                'energy': 0.3,
            },
            {
                'food': 0,
                'water': 0.3,
                'energy': 0.2,
            },
            {
                'food': 0,
                'water': 0.3,
                'energy': 0.2,
            },
        ],
    }
    measure.dates = [
        Date(2020, 1, 1),
        Date(2020, 1, 2),
        Date(2020, 1, 3),
        Date(2020, 1, 4),
        Date(2020, 1, 5),
        Date(2020, 1, 6),
    ]
    #print(measure.agent_resource_accessilibity(id=1, resource_name='food'))
    #print(measure.agent_resources_accessibility(id=1))
    #print(measure.agents_resource_accessibility(resource_name='food'))
    #print(measure.agents_resources_accessibility())
    #print(measure.average)
    #measure.show(resource_name='food')
    #measure.show(resource_name='water')
    #measure.show(resource_name='energy')
    #measure.show(id=2)
    #measure.show(resource_name='food', id=2)
    #measure.show()
