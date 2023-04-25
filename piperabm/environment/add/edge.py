from copy import deepcopy

from piperabm.unit import Date
from piperabm.environment.structures import Road
from piperabm.boundary.rectangular import Rectangular
from piperabm.tools.coordinate import slope, euclidean_distance, center


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
        road = Road(
            name=name,
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
        road.boundary = Rectangular(height=width)
        self.add_edge_object(
            _from=_from,
            _to=_to,
            structure=road
        )
    
    def modify_boundary(self, length, slope, boundary):
        """
        Create boundary for the link
        """
        shape = boundary.shape
        shape.width = length
        shape.angle = slope
        return boundary

    def add_edge_object(self, _from, _to, structure):
        """
        Add a current link object to the model
        """
        start_index, end_index = self.input_to_index_edge(_from, _to)
        if structure is not None:
            self.add_edge(
                start_index=start_index,
                end_index=end_index,
                structure=structure
            )

    def add_edge(self, start_index: int, end_index: int, structure):
        """
        Add aa edge to the model together with its element
        """
        def swap(start_index, end_index):
            start_pos, end_pos = self.index_to_pos_edge(start_index, end_index)
            angle = slope(start_pos, end_pos)
            angle_inverse = slope(end_pos, start_pos)
            if angle > angle_inverse:
                temp = deepcopy(start_index)
                start_index = deepcopy(end_index)
                end_index = temp
            return start_index, end_index
        
        start_index, end_index = swap(start_index, end_index)
        start_pos, end_pos = self.index_to_pos_edge(start_index, end_index)
        length = euclidean_distance(start_pos, end_pos)
        angle = slope(start_pos, end_pos)
        structure.boundary = self.modify_boundary(length, angle, structure.boundary)
        pos = center(start_pos, end_pos)
        
        if structure is not None:
            self.G.add_edge(
                start_index,
                end_index,
                pos=pos,
                structure=structure
            )

    def input_to_index_edge(self, _from, _to):

        def to_index(input):
            index = self.find_node(input)
            if index is None and isinstance(input, list):
                index = self.append_node(
                    pos=input,
                    structure=None
                )
            return index
        
        start_index = to_index(_from)
        end_index = to_index(_to)
        return start_index, end_index
    
    def index_to_pos_edge(self, start_index, end_index):
        start_pos = self.get_node_pos(start_index)
        end_pos = self.get_node_pos(end_index)
        return start_pos, end_pos
    