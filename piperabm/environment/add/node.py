from piperabm.unit import Date
from piperabm.infrastructure import Settlement


class Node:
    """
    *** Extends Add Class ***
    Manage nodes
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
        structure = Settlement(
            name=name,
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
        index = self.append_node(pos, structure)
        return index
    
    def append_node(self, pos: list=[0, 0], structure=None):
        if structure is not None:
            name = structure.name
        else:
            name = ''
        index = self.input_to_index_node(name=name, pos=pos)
        self.add_node(index, pos, structure)
        return index

    def add_node(self, index: int, pos: list=[0, 0], structure=None):
        """
        Add a node to the model together with its element
        """
        self.G.add_node(
            index,
            pos=pos,
            structure=structure
        )

    def input_to_index_node(self, name: str, pos: list):
        """
        Return index based on inputs
        """
        index = None
        index_by_name = self.find_node(name)
        index_by_pos = self.find_node(pos)
        if index_by_name is None and index_by_pos is None:
            # create node:
            index = self.find_next_index()
        elif index_by_name is not None or index_by_pos is not None:
            # update node:
            print('node already exists.')
            if index_by_name is not None:
                index = index_by_name
            elif index_by_pos is not None:
                index = index_by_pos
        elif index_by_name is not None and index_by_pos is not None:
            raise ValueError
        return index
