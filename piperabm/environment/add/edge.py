from piperabm.unit import Date
from piperabm.environment.structures import Road
from piperabm.environment.elements import Link
from piperabm.boundary.rectangular import Rectangular
from piperabm.tools.coordinate import slope, euclidean_distance, center
from piperabm.tools.symbols import SYMBOLS


class Edge:
    """
    Manage edges
    Extends Add class
    """

    def add_road(
            self,
            _from=None,
            _to=None,
            name: str = '',
            width: float = None,
            actual_length: float = None,
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
        Create a new road on a new link object and add it to the model
        """
        start_index, end_index = self.input_to_index_edge(_from, _to, start_date, end_date)
        start_pos, end_pos = self.index_to_pos_edge(start_index, end_index)
        length = euclidean_distance(start_pos, end_pos)
        angle = slope(start_pos, end_pos)
        boundary = self.create_boundary(length, width, angle)
        road = Road(
            boundary=boundary,
            active=active,
            start_date=start_date,
            end_date=end_date,
            actual_length=actual_length,
            sudden_degradation_dist=sudden_degradation_dist,
            sudden_degradation_unit_size=sudden_degradation_unit_size,
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
    
    def create_boundary(self, length, width, slope):
        """
        Create boundary for the link
        """
        if width is None:
            width = SYMBOLS['eps']
        return Rectangular(
            width=length,
            height=width,
            angle=slope
        )

    def add_link(
            self,
            _from,
            _to,
            name: str = None,
            start_date: Date = None,
            end_date: Date = None,
            structure = None 
        ):
        """
        Create a new link object and add it to the model
        """
        start_index, end_index = self.input_to_index_edge(_from, _to, start_date, end_date)
        start_pos, end_pos = self.index_to_pos_edge(start_index, end_index)
        pos_center = center(start_pos, end_pos)
        link = Link(
            name=name,
            start_date=start_date,
            end_date=end_date,
            structure=structure
        )
        link.pos = pos_center
        self.add_link_object(_from, _to, link)

    def add_link_object(self, _from, _to, link):
        """
        Add a current link object to the model
        """
        start_date = link.start_date
        end_date = link.end_date
        start_index, end_index = self.input_to_index_edge(_from, _to, start_date, end_date)
        self.add_edge(start_index, end_index, element=link)

    def add_edge(self, start_index: int, end_index: int, element=None):
        """
        Add aa edge to the model together with its element
        """
        start_pos, end_pos = self.index_to_pos_edge(start_index, end_index)
        length = euclidean_distance(start_pos, end_pos)
        angle = slope(start_pos, end_pos)
        width = element.structure.boundary.shape.height
        boundary = self.create_boundary(length, width, angle)
        element.structure.boundary = boundary
        self.G.add_edge(
            start_index,
            end_index,
            element=element
        )

    def input_to_index_edge(self, _from, _to, start_date: Date = None, end_date: Date = None):
        start_index = self.find_node(_from)
        if start_index is None and isinstance(_from, list):
            start_index = self.add_hub(
                pos=_from,
                start_date=start_date,
                end_date=end_date,
                structure=None
            )
        end_index = self.find_node(_to)
        if end_index is None and isinstance(_to, list):
            end_index = self.add_hub(
                pos=_to,
                start_date=start_date,
                end_date=end_date,
                structure=None
            )
        return start_index, end_index
    
    def index_to_pos_edge(self, start_index, end_index):
        start_hub = self.get_node_element(start_index)
        start_pos = start_hub.pos
        end_hub = self.get_node_element(end_index)
        end_pos = end_hub.pos
        return start_pos, end_pos
    