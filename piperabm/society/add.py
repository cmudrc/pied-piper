from piperabm.unit import Date
from piperabm.society.agent import Agent
from piperabm.society.relationship import Family, Neighbor, FellowCitizen


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
        Create a new settlement on a new hub object and add it to the model
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
        index = self.add_agent_object(origin, agent)
        return index
    
    def add_agent_object(self, agent):
        """
        Add agent object to a new node with a new index assigned
        """
        pos = self.environment.get_node_pos(agent.origin)
        index = self.find_next_index()
        self.add_node(index, pos, agent)
        self.add_relationships(index, agent)
        return index
    
    def add_relationships(self, index, agent):
        """
        Check and add eligible relationships
        """
        for other_index in self.all_indexes():
            if index != other_index:
                relationships = {}
                self.add_edge(index, other_index, relationships)

        self.add_family_relationship(index, agent.origin)
        self.add_fellow_citizen_relationship(index)
        self.add_neighbor_relationship(index)

    def add_family_relationship(self, agent_index, origin_index):
        """
        Check the eligibility of agents to be family
        """
        for index in self.all_indexes():
            if index != agent_index:
                other_agent = self.get_node_object(index)
                if other_agent.origin == origin_index: # family constraint
                    relationship = Family(
                        start_date=None, ####
                        end_date=None
                    )
                    relationships = self.get_edge_object(index, agent_index)
                    relationships['family'] = relationship
    
    def add_fellow_citizen_relationship(self, agent_index):
        """
        Check the eligibility of agents to be fellow citizen
        """
        for index in self.all_indexes():
            if index != agent_index: ###### rank is missing
                relationship = FellowCitizen(
                    start_date=None, ####
                    end_date=None
                )
                relationships = self.get_edge_object(index, agent_index)
                relationships['fellow citizen'] = relationship

    def add_neighbor_relationship(self, agent_index):
        """
        Check the eligibility of agents to be neighbors
        """
        for index in self.all_indexes():
            if index != agent_index: ###### rank is missing
                relationship = Neighbor(
                    start_date=None, ####
                    end_date=None
                )
                relationships = self.get_edge_object(index, agent_index)
                relationships['neighbor'] = relationship
