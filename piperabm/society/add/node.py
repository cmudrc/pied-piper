from piperabm.unit import Date
from piperabm.society.agent import Agent


class Node:
    """
    *** Extends Add Class ***
    Manage nodes
    """

    def add_agent(
            self,
            name: str = '',
            initial_node: int = None,
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
        index = self.add_agent_object(initial_node, agent)
        return index
    
    def add_agent_object(self, initial_node, object):
        pos = self.environment.get_node_pos(initial_node)
        index = self.find_next_index()
        self.add_node(index, pos, object)
        return index

    def add_node(self, index: int, pos: list=[0, 0], agent=None):
        """
        Add a node to the model together with its element
        """
        self.G.add_node(
            index,
            pos=pos,
            object=agent
        )
