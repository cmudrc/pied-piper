from piperabm.unit import Date
from piperabm.environment.structures import Settlement
from piperabm.environment.elements import Hub


class Node:
    """
    Manage nodes
    Extends Add class
    """

    def add_settlement(
            self,
            name: str = '',
            pos: list = [0, 0],
            boundary=None,
            active=True,
            start_date: Date = None,
            end_date: Date = None,
            sudden_degradation_dist=None,
            sudden_degradation_unit_size: float=None,
            progressive_degradation_formula=None,
            progressive_degradation_current: float=None,
            progressive_degradation_max: float=None
        ):
        """
        Create a new settlement on a new hub object and add it to the model
        """
        settlement = Settlement(
            boundary=boundary,
            active=active,
            start_date=start_date,
            end_date=end_date,
            sudden_degradation_dist=sudden_degradation_dist,
            sudden_degradation_unit_size=sudden_degradation_unit_size,
            progressive_degradation_formula=progressive_degradation_formula,
            progressive_degradation_current=progressive_degradation_current,
            progressive_degradation_max=progressive_degradation_max
        )
        index = self.add_hub(
            name=name,
            pos=pos,
            start_date=start_date,
            end_date=end_date,
            structure=settlement
        )
        return index

    def add_hub(
            self,
            name: str = '',
            pos: list = [0, 0],
            start_date: Date = None,
            end_date: Date = None,
            structure = None
        ):
        """
        Create a new hub object and add it to the model
        """
        hub = Hub(
            name=name,
            pos=pos,
            start_date=start_date,
            end_date=end_date,
            structure=structure
        )
        index = self.add_hub_object(hub)
        return index

    def add_hub_object(self, hub):
        """
        Add a current hub object to the model
        """
        index = self.input_to_index_node(
            name=hub.name,
            pos=hub.pos
        )
        self.add_node(
            index=index,
            element=hub
        )
        return index

    def add_node(self, index: int, element=None):
        """
        Add a node to the model together with its element
        """
        self.G.add_node(
            index,
            element=element
        )
    
    def append_node(self, element):
        """
        Add a node to the model together with its element
        """
        index = self.find_next_index()
        self.add_node(index, element)

    def input_to_index_node(self, name: str, pos: list):
        """
        Return index based on inputs
        """
        index = None
        hub_index_by_name = self.find_node(name)
        hub_index_by_pos = self.find_node(pos)
        if hub_index_by_name is None and hub_index_by_pos is None:
            # create node:
            index = self.find_next_index()
        else:
            # update node:
            print('hub already exists.')
            if hub_index_by_name is not None:
                index = hub_index_by_name
            elif hub_index_by_pos is not None:
                index = hub_index_by_pos
        return index
