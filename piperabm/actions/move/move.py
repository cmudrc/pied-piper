import numpy as np

from piperabm.unit import Date, DT
from piperabm.actions.action import Action
from piperabm.resources import resource_sum
from piperabm.tools.coordinate import move_point
from piperabm.transporation import Transportation


class Move(Action):

    def __init__(
            self,
            start_date: Date = None,
            path: list = None,
            transportation=None,
            environment=None,
            agent_index: int = None,
        ):
        self.environment = environment
        self.agent_index = agent_index

        self.transportation = transportation
        self.path = path
        try:
            duration = self.total_duration
        except:
            duration = None
        super().__init__(
            start_date=start_date,
            duration=duration
        )
        #try:
        #    self.fuel_consumption = self.total_fuel()
        #except:
        #    self.fuel_consumption = None
        self.done = False
        self.type = 'move'

    def get_track_object(self, track):
        return self.environment.get_edge_object(track[0], track[1])

    @property
    def total_duration(self):
        """
        Calculate the duration for the movement
        """
        total = 0
        for track in self.path:
            structure = self.get_track_object(track)
            total += structure.duration(self.transportation).total_seconds()
        return DT(seconds=total)

    @property
    def total_fuel(self):
        """
        Calculate total fuel needed for the movement
        """
        fuels = []
        for track in self.path:
            structure = self.get_track_object(track)
            fuels.append(structure.fuel(self.transportation))
        return resource_sum(fuels)
    
    def progress(self, date: Date):
        result = None
        if date <= self.start_date:
            result = 0
        elif date >= self.end_date:
            result = 1
        else:
            elapsed_time = date - self.start_date
            result = elapsed_time / self.duration
        return result
    
    def current_track(self, date: Date):
        current_index = None
        current_elapsed = None
        duration = self.total_duration * self.progress(date)
        duration = duration.total_seconds()
        for index, track in enumerate(self.path):
            structure = self.get_track_object(track)
            track_duration = structure.duration(self.transportation)
            track_duration = track_duration.total_seconds()
            duration -= track_duration
            if duration < 0:
                current_index = index
                current_elapsed = duration + track_duration
                break
        return current_index, current_elapsed

    def pos(self, date: Date):
        """
        Calculate position on an specific date
        """
        index, elapsed = self.current_track(date)
        track = self.path[index]
        return self.track_pos(track, elapsed)

    def track_pos(self, track, elapsed):
        """
        Calculate the position on current *track* when *elapsed* time
        """
        object = self.environment.get_edge_object(track[0], track[1])
        start_pos = self.environment.get_node_pos(track[0])
        track_progress = elapsed / object.duration(self.transportation).total_seconds()
        length = object.length('ideal') * track_progress
        vector = [
            length * np.cos(object.angle),
            length * np.sin(object.angle)
        ]
        return move_point(
            pos=start_pos,
            vector=vector
        )

    def to_dict(self) -> dict:
        dictionary = super().to_dict()
        dictionary['path'] = self.path
        if self.transportation is None:
            transportation = None
        else:
            transportation = self.transportation.to_dict()
        dictionary['transportation'] = transportation
        return dictionary
    
    def from_dict(self, dictionary: dict) -> None:
        super().from_dict(dictionary)
        self.path = dictionary['path']
        transportation = Transportation()
        transportation.from_dict(dictionary['transportation'])
        self.transportation = transportation

    
if __name__ == "__main__":
    from piperabm.actions.move.samples import move_0 as move

    print(move)