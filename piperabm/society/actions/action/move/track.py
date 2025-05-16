import numpy as np
from copy import deepcopy

from piperabm.tools.coordinate import distance as ds
from piperabm.tools.print.serialized import Print


class Track(Print):
    """
    Move action segments
    """

    type = "track"

    def __init__(
        self,
        action = None,
        id_start: int = None,
        id_end: int = None,
    ):
        super().__init__()
        self.action = action # Binding
        self.id_start = id_start
        self.id_end = id_end

    def preprocess(self, kwargs: dict = None):
        """
        Calculate the neccessary pieces using the kwargs
        """
        if kwargs is None:
            self.done = False
            self.elapsed = 0
            self.remaining = self.adjusted_length() / self.speed
            self.total_duration = deepcopy(self.remaining)
            pos_start = self.pos_start
            pos_end = self.pos_end
            if pos_start != pos_end:
                unit_vector = list(ds.point_to_point(self.pos_start, self.pos_end, vector=True, ndarray=True) / self.length)
                self.unit_vector = [float(i) for i in unit_vector]
                self.adjustment_factor = self.adjusted_length() / self.length
            else:
                self.unit_vector = None
                self.adjustment_factor = None
        else: # Equivalent of deserialization
            self.done = kwargs["done"]
            self.elapsed = kwargs["elapsed"]
            self.remaining = kwargs["remaining"]
            self.total_duration = kwargs["total_duration"]
            if kwargs["unit_vector"] is None:
                self.unit_vector = None
                self.adjustment_factor = None
            else:
                self.unit_vector = kwargs["unit_vector"]
                self.adjustment_factor = kwargs["adjustment_factor"]

    @property
    def action_queue(self):
        """
        Alias to access action queue
        """
        return self.action.action_queue
    
    @property
    def society(self):
        """
        Alias to access society
        """
        return self.action_queue.society
    
    @property
    def model(self):
        """
        Alias to access model
        """
        return self.society.model
    
    @property
    def infrastructure(self):
        """
        Alias to access infrastructure
        """
        return self.model.infrastructure

    @property
    def agent_id(self) -> int:
        """
        Alias to access agent id
        """
        return self.action_queue.agent_id

    @property
    def edge_ids(self) -> list:
        """
        Return corresponding edge ids
        """
        return [self.id_start, self.id_end]

    @property
    def pos_start(self) -> list:
        """
        Starting node position
        """
        return self.infrastructure.get_pos(id=self.id_start)

    @property
    def pos_end(self) -> list:
        """
        Ending node position
        """
        return self.infrastructure.get_pos(id=self.id_end)
    
    def pos(self, new_val: list = None) -> list:
        """
        Return current agent position
        """
        if new_val is None:
            return self.society.get_pos(id=self.agent_id)
        else:
            self.society.set_pos(id=self.agent_id, value=new_val)
    
    @property
    def speed(self) -> float:
        """
        Alias to access agent transportation speed
        """
        return self.society.speed

    @property
    def length(self) -> float:
        """
        Alias to access edge length
        """
        return self.infrastructure.get_length(ids=self.edge_ids)

    def adjusted_length(self) -> float:
        """
        Alias to access edge adjusted length
        """
        return self.infrastructure.get_adjusted_length(ids=self.edge_ids)
    
    def set_usage_impact(self, value: float) -> None:
        """
        Alias to set usage_impact value
        """
        self.infrastructure.set_usage_impact(ids=self.edge_ids, value=value)

    def update(self, duration: float, measure: bool = False):
        """
        Update track
        """
        if duration <= self.remaining and \
            self.unit_vector is not None:
            excess_duration = 0
            self.elapsed += duration
            self.remaining -= duration
            delta_length_adjusted = self.speed * duration
            delta_length = delta_length_adjusted / self.adjustment_factor
            new_pos = list(np.array(self.pos()) + np.array(self.unit_vector) * delta_length)
            self.pos(new_val=new_pos)
            if measure is True:
                delta_length
        else:
            excess_duration = duration - self.remaining
            self.elapsed = self.total_duration
            self.remaining = 0
            pos_old = deepcopy(self.pos())
            self.pos(new_val=self.pos_end)
            self.done = True
            # Update usage
            usage_impact = self.infrastructure.get_usage_impact(ids=self.edge_ids)
            delta = self.action.usage
            new_usage_impact = usage_impact + delta
            self.set_usage_impact(value=new_usage_impact)
            # Update adjusted_length
            #self.infrastructure.update_adjusted_length(ids=self.edge_ids)
            if measure is True:
                pos_new = deepcopy(self.pos())
                delta_length = ds.point_to_point(pos_old, pos_new)
        # Update fuel consumption
        delta_t = duration - excess_duration
        fuel_food = self.society.transportation_resource_rates["food"] * delta_t
        fuel_water = self.society.transportation_resource_rates["water"] * delta_t
        fuel_energy = self.society.transportation_resource_rates["energy"] * delta_t
        new_food = self.society.get_resource(name="food", id=self.agent_id) - fuel_food
        new_water = self.society.get_resource(name="water", id=self.agent_id) - fuel_water
        new_energy = self.society.get_resource(name="energy", id=self.agent_id) - fuel_energy
        self.society.set_resource(name="food", id=self.agent_id, value=new_food)
        self.society.set_resource(name="water", id=self.agent_id, value=new_water)
        self.society.set_resource(name="energy", id=self.agent_id, value=new_energy)
        return excess_duration
    
    def reverse(self):
        """
        Create a reversed track
        """
        reversed_track = Track(
            action=self.action,
            id_start=self.id_end,
            id_end=self.id_start
        )
        reversed_track.preprocess()
        return reversed_track

    def serialize(self):
        """
        Serialize
        """
        dictionary = {}
        dictionary["id_start"] = self.id_start
        dictionary["id_end"] = self.id_end
        dictionary["elapsed"] = self.elapsed
        dictionary["remaining"] = self.remaining
        dictionary["total_duration"] = self.total_duration
        if self.unit_vector is not None:
            dictionary["unit_vector"] = self.unit_vector
        else:
            dictionary["unit_vector"] = None
        dictionary["adjustment_factor"] = self.adjustment_factor
        dictionary["done"] = self.done
        dictionary["type"] = self.type
        return dictionary