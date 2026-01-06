"""
.. module:: piperabm.infrastructure.query.set
:synopsis: Set attributes to network elements.
"""

from piperabm.tools.nx_query import NxSet
from piperabm.resource import Resource


class Set(NxSet):
    """
    Set attributes to network elements
    """

    def set_adjusted_length(self, ids: list, value: float) -> None:
        """
        Set edge *adjusted_length* value
        """
        self.set_edge_attribute(ids=ids, attribute="adjusted_length", value=value)

    def set_usage_impact(self, ids: list, value: float) -> None:
        """
        Set edge *usage_impact* value
        """
        self.set_edge_attribute(ids=ids, attribute="usage_impact", value=value)

    def set_age_impact(self, ids: list, value: float) -> None:
        """
        Set edge *age_impact* value
        """
        self.set_edge_attribute(ids=ids, attribute="age_impact", value=value)

    def set_resource(self, id: int, name: str, value: float) -> None:
        """
        Set market *resource* value
        """
        if value <= 0:
            value = 0
        self.set_node_attribute(id=id, attribute=name, value=value)

    def set_resources(self, id: int, values: dict | Resource) -> None:
        """
        Set agent resources values.
        """
        if isinstance(values, Resource):
            values = dict(values)
            for name in values:
                # Delete the key if the value is 0
                if values[name] == 0:
                    del values[name]
        for name in values:
            self.set_resource(id=id, name=name, value=values[name])

    def set_balance(self, id: int, value: float) -> None:
        """
        Set market *balance* value
        """
        if value < 0:
            value = 0
        self.set_node_attribute(id=id, attribute="balance", value=value)
