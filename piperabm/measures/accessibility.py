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
    def society(self):
        return self.model.society
    
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
    
    def accessibility(self, agents='all', resources='all'):
        """
        Return accessibility values for all resources for across agents
        """
        values = []

        if agents == 'all':
            ids = self.agents
        elif isinstance(agents, list):
            ids = agents
        elif isinstance(agents, int):
            ids = [agents]
        elif agents is None:
            ids = self.agents
        else:
            raise ValueError
        
        if resources == 'all':
            resource_names = self.resource_names
        elif isinstance(resources, list):
            resource_names = resources
        elif isinstance(resources, str) and \
        resources != 'all':
            resource_names = [resources]
        elif resources is None:
            resource_names = self.resource_names
        else:
            raise ValueError
        
        for i in range(self.len):
            agent_resource_value = []
            for resource_name in resource_names:
                agent_resource_values = []
                for agent_id in ids:
                    agent_resource_values.append(self.library[agent_id][i][resource_name])
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
        if len(self.dates) > 1: # There has to be one more members in date than accessibility values
            accessibility = None ###################
            self.values.append(accessibility)
    
    def show(self, scale_y=False, average=True, agents='all', resources='all'):
        """
        Show the data as plot
        """

        def create_title(agents, resources):
            title_name = ''
            if isinstance(resources, str):
                if resources == 'all':
                    title_name = 'all resources'
                else:
                    title_name = resources
            elif isinstance(resources, list):
                for name in resources:
                    title_name += name
                    title_name += ', '
                title_name = title_name[:-2]
            result = self.name + " " + "of" + " " + title_name + " " + "over time"
            return result

        title = create_title(agents=agents, resources=resources)
        xs = self.xs
        ys = self.accessibility(agents=agents, resources=resources)

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

    #print(measure.accessibility(agents=[1, 2], resources='food'))
    #print(measure.accessibility(agents='all', resources='food'))
    measure.show(agents=[1, 2], resources=['food', 'water'])

