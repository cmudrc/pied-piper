from piperabm.society.actions.action.move.track import Track
from piperabm.tools.print.serialized import Print


class Move(Print):
    """
    Move action
    """

    type = 'move'

    def __init__(
            self,
            action_queue=None,
            path: list = [],
            usage: float = 1,
        ):
        super().__init__()
        self.action_queue = action_queue  # Binding
        self.tracks = self.path_to_tracks(path)
        self.usage = usage

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
    def agent_id(self):
        """
        Alias to access agent id
        """
        return self.action_queue.agent_id

    def path_to_tracks(self, path):
        """
        Convert path to track segments
        """
        tracks = []
        for i, _ in enumerate(path):
            if i != 0:
                id_start = path[i-1]
                id_end = path[i]
                track = Track(
                    action=self, # Binding
                    id_start=id_start,
                    id_end=id_end
                )
                track.preprocess()
                tracks.append(track)
        return tracks
    
    @property
    def total_duration(self):
        """
        Return how long the action will take
        """
        total = 0
        for track in self.tracks:
            total += track.total_duration
        return total
    
    @property
    def destination(self):
        """
        Destionation id
        """
        last_track = self.tracks[-1]
        return last_track.id_end
    
    @property
    def active_track(self):
        """
        Return the track which is currently in progress
        """
        result = None
        for track in self.tracks:
            #print(track.done)
            if track.done is False:
                result = track
                break
        return result
    
    @property
    def done(self):
        """
        Check whether the action is already complete
        """
        result = True
        for track in self.tracks:
            status = track.done
            if status is False:
                result = False
                break
        return result
    
    @property
    def elapsed(self):
        """
        Return how long has been passed
        """
        result = 0
        for track in self.tracks:
            result += track.elapsed
        return result
    
    @property
    def remaining(self):
        """
        Return how long is still remaining
        """
        result = 0
        for track in self.tracks:
            result += track.remaining
        return result
    
    def reverse(self):
        reversed_tracks = []
        for track in self.tracks:
            reversed_tracks.append(track.reverse())
        reversed_tracks = list(reversed(reversed_tracks))
        reversed_move = Move(
            action_queue=self.action_queue,
            path=[],
            usage=self.usage
        )
        reversed_move.tracks = reversed_tracks
        return reversed_move

    def update(self, duration, measure: bool = False):
        """
        Update status of action
        """
        self.society.set_current_node(self.agent_id, None)
        excess_delta_time = duration
        while excess_delta_time > 0:
            track = self.active_track
            if track is not None:
                excess_delta_time = track.update(excess_delta_time, measure=measure)
            else: # Action ended
                self.society.set_current_node(self.agent_id, self.destination)
                break
        return excess_delta_time

    def serialize(self) -> dict:
        """
        Serialize
        """
        dictionary = {}
        dictionary['type'] = self.type
        tracks_serialized = []
        for track in self.tracks:
            track_serialized = track.serialize()
            tracks_serialized.append(track_serialized)
        dictionary['tracks'] = tracks_serialized
        dictionary['usage'] = self.usage
        return dictionary

    def deserialize(self, dictionary: dict) -> None:
        """
        Deserialize
        """
        tracks_serialized = dictionary['tracks']
        for track_serialized in tracks_serialized:
            track = Track(
                action=self,
                id_start=track_serialized['id_start'],
                id_end=track_serialized['id_end']
            )
            track.preprocess(track_serialized)
            self.tracks.append(track)
        self.usage = dictionary['usage']


if __name__ == "__main__":

    from piperabm.society.samples import model_1 as model

    agent_id = 1
    destination_id = 2
    action_queue = model.society.actions[agent_id]
    path = model.society.path(agent_id, destination_id)
    move = Move(
        action_queue=action_queue,
        path=path,
        usage=1
    )
    action_queue.add(move)

    print(model.infrastructure.edge_degradation(0))
    print(model.society.pos(agent_id))
    model.update(duration=28)
    print(model.society.pos(agent_id))
    model.update(duration=28)
    print(model.society.pos(agent_id))
    print(model.infrastructure.edge_degradation(0))
