import numpy as np

from piperabm.unit import Date
from piperabm.environment.structures import Road
from piperabm.environment.elements import Link
from piperabm.boundary.rectangular import Rectangular
from piperabm.tools.distance import euclidean_distance
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
            active=True,
            start_date: Date = None,
            end_date: Date = None,
            sudden_degradation_dist=None,
            sudden_degradation_unit_size: float=None,
            progressive_degradation_formula=None,
            progressive_degradation_current: float=None,
            progressive_degradation_max: float=None
        ):
        if width is None:
            width = SYMBOLS['eps']
        boundary = Rectangular(width=width)
        road = Road(
            boundary=boundary,
            active=active,
            start_date=start_date,
            end_date=end_date,
            sudden_degradation_dist=sudden_degradation_dist,
            sudden_degradation_coeff=None,
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

    def calculate_pos(self, start_pos: list, length: float, angle: float):
        x = start_pos[0] + (length/2) * np.cos(angle)
        y = start_pos[1] + (length/2) * np.sin(angle)
        return [x, y]
    
    def slope(self, start_pos: list, end_pos: list):
        result = None
        start_x = start_pos[0]
        start_y = start_pos[1]
        end_x = end_pos[0]
        end_y = end_pos[1]
        delta_x = end_x - start_x
        delta_y = end_y - start_y
        if delta_x != 0:
            result = np.arctan(delta_y / delta_x)
        else:
            if delta_y > 0:
                result = np.pi / 2
            else:
                result = np.pi * 3 / 2
        return result

    def calculate_height_and_angle(self, start_index, end_index):
        if width is None:
            width = SYMBOLS['eps']
        start_hub = self.get_node_element(start_index)
        start_pos = start_hub.pos
        end_hub = self.get_node_element(end_index)
        end_pos = end_hub.pos
        distance = euclidean_distance(*start_pos, *end_pos)
        angle = self.slope(start_pos, end_pos)
        return distance, angle

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
            height, angle = self.calculate_height_and_angle(start_index, end_index)
            structure.boundary.height = height
            structure.boundary.angle = angle
            structure.sudden_degradation_coeff = 
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