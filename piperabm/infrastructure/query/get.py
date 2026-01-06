"""
.. module:: piperabm.infrastructure.query.get
:synopsis: Get attributes from network elements.
"""

from piperabm.tools.nx_query import NxGet
from piperabm.resource import Resource


class Get(NxGet):
    """
    Get attributes from network elements
    """

    def get_pos(self, id: int):
        """
        Get node position
        """
        return [
            self.get_node_attribute(id, "x", None),
            self.get_node_attribute(id, "y", None),
        ]

    def get_node_type(self, id: int) -> str:
        """
        Get node type
        """
        return self.get_node_attribute(id=id, attribute="type")

    def get_edge_type(self, ids: list) -> str:
        """
        Get edge type
        """
        return self.get_edge_attribute(ids=ids, attribute="type")

    def get_node_name(self, id: int) -> str:
        """
        Get node name
        """
        return self.get_node_attribute(id=id, attribute="name")

    def get_edge_name(self, ids: list) -> str:
        """
        Get edge name
        """
        return self.get_edge_attribute(ids=ids, attribute="name")

    def get_length(self, ids: list) -> float:
        """
        Get edges length
        """
        return self.get_edge_attribute(ids=ids, attribute="length")

    def get_adjusted_length(self, ids: list) -> float:
        """
        Get edges *adjusted_length*
        """
        return self.get_edge_attribute(ids=ids, attribute="adjusted_length")

    def get_usage_impact(self, ids: list) -> float:
        """
        Get edges *usage_impact*
        """
        return self.get_edge_attribute(ids=ids, attribute="usage_impact")

    def get_age_impact(self, ids: list) -> float:
        """
        Get edges *age_impact*
        """
        return self.get_edge_attribute(ids=ids, attribute="age_impact")

    def get_resource(self, id: int, name: str, object=False) -> float | Resource:
        """
        Get market *resource* value. If object is False, return a float, otherwise return a Resource object.
        """
        value = self.get_node_attribute(id=id, attribute=name)
        if object is True:
            return Resource(**{name: value})
        return value

    def get_resources(self, id: int, object=False) -> dict | Resource:
        """
        Get market resources value. If object is False, return a dict, otherwise return a Resource object.
        """
        result = {}
        for name in self.resource_names:
            result[name] = self.get_resource(id=id, name=name)
        if object is False:
            return Resource(**result)
        return result

    def get_enough_resource(self, id: int, name: str) -> float:
        """
        Get market *enough_resource* value
        """
        attribute = "enough_" + name
        return self.get_node_attribute(id=id, attribute=attribute)

    def get_balance(self, id: int) -> float:
        """
        Get market *balance* value
        """
        return self.get_node_attribute(id=id, attribute="balance")
