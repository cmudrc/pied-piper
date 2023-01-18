import networkx as nx
from environment import Environment

from piperabm.unit import DT, Date
from piperabm.tools import euclidean_distance


class Society:
    def __init__(self, env: Environment):
        self.env = env
        self.G = nx.Graph()
        self.index_list = []

    def find_next_index(self):
        """
        Check self.index_list (indexes) and suggest a new index
        """
        index_list = self.index_list
        if len(index_list) > 0:
            max_index = max(index_list)
            new_index = max_index + 1
        else:
            new_index = 0
        return new_index

    def add_agent(self):
        index = self.find_next_index()
        self.index_list.append(index)
        settlement_index = self.env.random_settlement()
        settlement_node = self.env.G.nodes[settlement_index]
        pos = settlement_node['boundary'].center
        self.G.add_node(
            index,
            settlement=settlement_index,
            pos=pos,
            queue=Queue()
            )

    def update_agents(self, start_date, end_date):
        pass

    def add_agents(self, n):
        for _ in range(n):
            self.add_agent()

    def path_to_pos(self, path: list):
        """
        Convert edge path data to a list of pos
        """
        pos_list = []
        for index in path:
            node = self.env.G.nodes[index]
            pos = node['boundary'].center
            pos_list.append(pos)
        return pos_list

    def path_real_length_list(self, path: list):
        """
        Convert edge path data to a list of real length
        """
        real_length_list = []
        for index in path:
            node = self.env.G.nodes[index]
            length = node['length']
            real_length_list.append(length)
        return real_length_list


class Transporation:
    def __init__(self, speed, fuel_consumption=None):
        self.speed = speed
        self.fuel_consumption = fuel_consumption


class Walk(Transporation):
    def __init__(self):
        super().__init__(
            speed=Unit(1, 'm/second').to_SI(),
            fuel_consumption=None
            )


class Queue:
    def __init__(self):
        self.action_list = []

    def add(self, action):
        self.action_list.append(action)

    def execute(self, date: Date):
        current_i = None
        result = None
        for i, action in enumerate(self.action_list):
            if action.is_current(date) is True:
                current_i = i
                if isinstance(action, Move):
                    result = action.pos(date), "pos"
        self.action_list = self.action_list[i:]
        return result


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
        progress = (date - self.start_date).total_seconds() / (self.end_date - self.start_date).total_seconds() 
        x = self.start_pos[0] + ((self.end_pos[0] - self.start_pos[0]) * progress)
        y = self.start_pos[1] + ((self.end_pos[1] - self.start_pos[1]) * progress)
        return [x, y]


if __name__ == "__main__":
    from piperabm.unit import Unit, Date


    m = Move(
        start_date=Date(2020, 1, 1),
        start_pos=[0, 0],
        end_pos=[10000, 10000],
        adjusted_length=20000,
        transportation=Walk()
        )
    print(m.end_date)
    print(m.pos(date=Date(2020, 1, 1)+DT(hours=1)))
