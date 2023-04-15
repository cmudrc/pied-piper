from piperabm.unit import Date
from piperabm.tools import euclidean_distance
from piperabm.environment.structures import Settlement, Road
from piperabm.environment.elements import Hub, Link


class Add:
    """
    Contains methods for Environment class
    Add new elements to the environment
    """

    # node methods:
    def add_settlement(
            self,
            name: str = '',
            pos: list = [0, 0],
            boundary=None,
            active=True,
            start_date: Date = None,
            end_date: Date = None,
            sudden_degradation_dist=None,
            sudden_degradation_coeff: float=None,
            progressive_degradation_formula=None,
            progressive_degradation_current: float=None,
            progressive_degradation_max: float=None
        ):
        """
        Create a new settlement on a new hub object and add to the model
        """
        settlement = Settlement(
            boundary=boundary,
            active=active,
            start_date=start_date,
            end_date=end_date,
            sudden_degradation_dist=sudden_degradation_dist,
            sudden_degradation_coeff=sudden_degradation_coeff,
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
        Create a new hub object and add to the model
        """
        hub = Hub(
            name=name,
            pos=pos,
            start_date=start_date,
            end_date=end_date,
            structure=structure
        )
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
        self.add_node(
            index=index,
            element=hub
        )
        return index

    def add_node(self, index: int, element):
        """
        Add a node to the model together with its element
        """
        self.G.add_node(
            index,
            element=element
        )

    # edge methods:
    def add_road(
            self,
            _from=None,
            _to=None,
            name: str = '',
            boundary=None,
            active=True,
            start_date: Date = None,
            end_date: Date = None,
            sudden_degradation_dist=None,
            sudden_degradation_coeff: float=None,
            progressive_degradation_formula=None,
            progressive_degradation_current: float=None,
            progressive_degradation_max: float=None
        ):
        road = Road(
            boundary=boundary, ######### rectangular / line
            active=active,
            start_date=start_date,
            end_date=end_date,
            sudden_degradation_dist=sudden_degradation_dist,
            sudden_degradation_coeff=sudden_degradation_coeff,
            progressive_degradation_formula=progressive_degradation_formula,
            progressive_degradation_current=progressive_degradation_current,
            progressive_degradation_max=progressive_degradation_max
        )
        self.add_link(
            _from=_from,
            _to=_to,
            name=name,
            start_date=start_date,
            end_date=end_date,
            structure=road
        )

    def add_link(
            self,
            _from=None,
            _to=None,
            name: str = '',
            start_date: Date = None,
            end_date: Date = None,
            structure = None
        ):
        start_index = self.find_node(_from)
        if start_index is None and isinstance(_from, list):
            start_index = self.add_hub(
                name=name,
                pos=_from,
                start_date=start_date,
                end_date=end_date,
                structure=None
            )
        end_index = self.find_node(_to)
        if end_index is None and isinstance(_to, list):
            end_index = self.add_hub(
                name=name,
                pos=_to,
                start_date=start_date,
                end_date=end_date,
                structure=None
            )
        if start_index is not None and end_index is not None:
            link = Link(
                name=name,
                start_date=start_date,
                end_date=end_date,
                structure=structure
            )
            self.add_edge(
                start_index=start_index,
                end_index=end_index,
                element=link
            )
    
    def add_edge(self, start_index: int, end_index: int, element):
        """
        Add aa edge to the model together with its element
        """
        self.G.add_edge(
            start_index,
            end_index,
            element=element
        )
