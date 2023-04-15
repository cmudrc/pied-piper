from piperabm.unit import Date
from piperabm.tools import euclidean_distance
from piperabm.environment.structures import Settlement
from piperabm.environment.elements import Hub


class Add:

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
        hub = Hub(
            name=name,
            pos=pos,
            start_date=start_date,
            end_date=end_date,
            structure=settlement
        )
        index = self.add_node(hub)
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
        index = self.add_node(hub)
        return index

    def add_node(self, object):
        """
        Add object to the model
        """
        index = self.find_next_index()
        self.G.add_node(
            index,
            element=object
        )
        return index

