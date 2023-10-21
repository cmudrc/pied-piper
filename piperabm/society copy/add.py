from piperabm.unit import Date
from piperabm.agent import Agent
from piperabm.society.relationship import Family, Neighbor, FellowCitizen
from piperabm.tools.coordinate import euclidean_distance


class Add:
    """
    *** Extends Society Class ***
    Add new elements to the society
    """
    
    def find_next_index(self):
        """
        Check all indexes in self.node_types dictionary and suggest a new index
        """
        all = self.all_indexes()
        if len(all) > 0:
            max_index = max(all)
            new_index = max_index + 1
        else:
            new_index = 0
        return new_index

    def add_edge(self, start_index: int, end_index: int, relationship):
        """
        Add an edge to the model together with its object
        """
        if relationship is not None:
            self.G.add_edge(
                start_index,
                end_index,
                object=relationship
            )

    def add_node(self, index: int, pos: list=[0, 0], agent=None):
        """
        Add a node to the model together with its element
        """
        if agent is not None:
            ''' binding '''
            agent.environment = self.environment # binding to the environment
            agent.society = self # binding to the society
            agent.index = index

            agent.queue.environment = agent.environment
            agent.queue.society = agent.society
            agent.queue.agent_index = agent.index

            self.G.add_node(
                index,
                pos=pos,
                object=agent
            )
            
    def add_agent(
            self,
            name: str = '',
            active=True,
            start_date: Date = None,
            end_date: Date = None,
            origin: int = None,
            transportation=None,
            resource=None,
            fuel_rate_idle=None
        ):
        """
        Create a new agent
        """
        agent = Agent(
            name=name,
            active=active,
            start_date=start_date,
            end_date=end_date,
            origin=origin,
            transportation=transportation,
            resource=resource,
            fuel_rate_idle=fuel_rate_idle
        )
        index = self.add_agent_object(agent)
        return index
    
    def add_agent_object(self, agent):
        """
        Add agent object to a new node with a new index assigned
        """
        pos = self.environment.get_node_pos(agent.origin)
        index = self.find_next_index()
        self.add_node(index, pos, agent)
        self.add_relationships(index)
        return index
    
    def add_relationships(self, index):
        """
        Check and add eligible relationships
        """
        for other_index in self.all_indexes():
            if index != other_index:
                relationships = {}
                ''' add edge between all nodes '''
                self.add_edge(index, other_index, relationships)
                ''' add relationships to the relationships dictionary '''
                self.add_family_relationship(index, other_index)
                self.add_fellow_citizen_relationship(index, other_index)
                self.add_neighbor_relationship(index, other_index)

    def add_family_relationship(self, agent_index, other_index):
        """
        Create family relationship between agents
        """
        agent = self.get_agent_object(agent_index)
        other = self.get_agent_object(other_index)
        if other.origin == agent.origin: # family constraint
            start_date, end_date = self.calculate_dates(agent, other)
            agent_pos = self.get_agent_pos(agent_index)
            other_pos = self.get_agent_pos(other_index)
            distance = euclidean_distance(agent_pos, other_pos)
            relationship = Family(start_date, end_date, distance)
            relationships = self.get_relationship_object(agent_index, other_index)
            relationships['family'] = relationship
    
    def add_fellow_citizen_relationship(self, agent_index, other_index):
        """
        Create fellow citizen relationship between agents
        """
        agent = self.get_agent_object(agent_index)
        other = self.get_agent_object(other_index)
        start_date, end_date = self.calculate_dates(agent, other)
        agent_pos = self.get_agent_pos(agent_index)
        other_pos = self.get_agent_pos(other_index)
        distance = euclidean_distance(agent_pos, other_pos)
        relationship = FellowCitizen(start_date, end_date, distance)
        relationships = self.get_relationship_object(agent_index, other_index)
        relationships['fellow citizen'] = relationship

    def add_neighbor_relationship(self, agent_index, other_index):
        """
        Create neighbor relationship between agents
        """
        agent = self.get_agent_object(agent_index)
        other = self.get_agent_object(other_index)
        if agent.origin != other.origin: # neighbor constraint
            start_date, end_date = self.calculate_dates(agent, other)
            agent_pos = self.environment.get_node_pos(agent_index)
            other_pos = self.environment.get_node_pos(other_index)
            distance = euclidean_distance(agent_pos, other_pos)
            relationship = Neighbor(start_date, end_date, distance)
            relationships = self.get_relationship_object(agent_index, other_index)
            relationships['neighbor'] = relationship

    def calculate_dates(self, agent, other):
        """
        Calcualte start_date and end_date of a relationship
        """
        start_date = None
        if agent.start_date is not None and other.start_date is not None:
            start_date = max(agent.start_date, other.start_date)
        elif agent.start_date is None and other.start_date is not None:
            start_date = other.start_date
        elif agent.start_date is not None and other.start_date is None:
            start_date = agent.start_date
        end_date = None
        if agent.end_date is not None and other.end_date is not None:
            end_date = min(agent.end_date, other.end_date)
        elif agent.end_date is None and other.end_date is not None:
            end_date = other.end_date
        elif agent.end_date is not None and other.end_date is None:
            end_date = agent.end_date
        return start_date, end_date

