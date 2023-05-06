from copy import deepcopy

from piperabm.unit import Date
from piperabm.society.relationship import Family


class Edge:
    """
    *** Extends Add Class ***
    Manage edges
    """

    def add_family(
            self,
            _from=None,
            _to=None,
            active=True,
            start_date: Date = None,
            end_date: Date = None,
        ):
        """
        Create a new road on a new link object and add it to the model
        """
        relationship = Family(
            active=active,
            start_date=start_date,
            end_date=end_date
        )
        self.add_edge_object(
            _from=_from,
            _to=_to,
            object=relationship
        )

    def add_edge_object(self, _from, _to, object):
        """
        Add a current link object to the model
        """
        start_index = self.find_node(_from)
        end_index = self.find_node(_to)
        if object is not None:
            self.add_edge(
                start_index=start_index,
                end_index=end_index,
                object=object
            )

    def add_edge(self, start_index: int, end_index: int, object):
        """
        Add aa edge to the model together with its object
        """
        if object is not None:
            self.G.add_edge(
                start_index,
                end_index,
                object=object
            )
    