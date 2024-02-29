import numpy as np

from piperabm.object import PureObject
from piperabm.tools.coordinate import distance as ds
from piperabm.transportation import Transportation
from piperabm.tools.symbols import SYMBOLS


class Track(PureObject):

    type = 'track'

    def __init__(
        self,
        id_start: list = None,
        id_end: list = None
    ):
        super().__init__()
        self.id_start = id_start
        self.id_end = id_end
        self.progress = 0
        self.action = None  # Binding

    @property
    def queue(self):
        return self.action.queue

    @property
    def agent(self):
        return self.queue.agent

    @property
    def model(self):
        return self.agent.model
    
    @property
    def infrastructure(self):
        return self.model.infrastructure
    
    @property
    def id(self):
        """
        Return edge id
        """
        return self.infrastructure.edge_id(self.id_start, self.id_end)

    @property
    def pos_start(self):
        item = self.model.get(self.id_start)
        return item.pos

    @property
    def pos_end(self):
        item = self.model.get(self.id_end)
        return item.pos
    
    @property
    def done(self):
        result = True
        if self.progress <= 1 - SYMBOLS['eps']:
            result = False
        return result
    
    @property
    def started(self):
        result = False
        if self.progress < 1 and \
        self.progress > 0:
            result = True
        return result

    @property
    def length_real(self):
        object = self.model.get(self.id)
        return object.length
        #return ds.point_to_point(
        #    point_1=self.pos_start,
        #    point_2=self.pos_end
        #)
    
    @property
    def length_adjusted(self):
        infrastructure = self.infrastructure
        return infrastructure.adjusted_length(self.id_start, self.id_end)
        #object = self.model.get(self.id)
        #return object.adjusted_length
    
    @property
    def adjustment_factor(self):
        object = self.model.get(self.id)
        return object.adjustment_factor
        #return self.length_adjusted / self.length_real

    @property
    def vector(self):
        """
        Movement vector
        """
        return ds.point_to_point(self.pos_start, self.pos_end, vector=True, ndarray=True)
    
    @property
    def unit_vector(self):
        """
        Unit vector showing the direction of movement
        """
        return self.vector / self.length_real

    def length_real_remaining(self, pos):
        return ds.point_to_point(pos, self.pos_end)
                       
    def update(self, delta_time, transportation: Transportation):
        excess_delta_time = 0

        if self.done is False:
            # Load current info
            adjustment_factor = self.adjustment_factor
            pos_current = self.agent.pos

            # Calculate movement
            delta_length = transportation.length_by_duration(delta_time) / adjustment_factor

            # When after delta_time the position falls out of track
            remaining_length = self.length_real_remaining(pos_current)
            excess_length = 0
            if delta_length > remaining_length:
                excess_length = delta_length - remaining_length
                delta_length = remaining_length
            excess_delta_time = transportation.duration_by_length(excess_length) * adjustment_factor
            
            # Update pos
            pos = np.array(pos_current) + delta_length * self.unit_vector
            self.agent.pos = list(pos)

            # Update resources
            fuels = transportation.fuels_by_length(delta_length) * adjustment_factor
            self.agent.resources - fuels

            # Update progress
            self.progress = self.progress_by_pos(pos)

            # Update infrastructure after finishing track
            if self.done is True:
                #edge_index = self.model.infrastructure.find_edge_index(self.index_start, self.index_end)
                edge = self.model.get(self.id)
                edge.degradation.add(self.action.usage)

        return excess_delta_time

    def progress_by_pos(self, pos: list) -> float:
        distance = ds.point_to_point(
            point_1=self.pos_start,
            point_2=pos
        )
        progress = distance / self.length_real
        if progress >= 1 - SYMBOLS['eps']:
            progress = 1
        if progress < 0:
            progress = 0
        return progress
    '''
    def pos_by_progress(self, progress: float) -> list:
        """
        Calcualte position based on ratio of track
        """
        result = None
        if progress > 1:
            progress = 1
        if progress < 0:
            progress = 0
        
        result = np.array(self.pos_start) + self.unit_vector * progress * self.length_real
        return list(result)
    '''
    '''
    def reverse(self):
        """
        Create an inverse track
        """
        return TrackNew(
            index_start=self.index_end,
            index_end=self.index_start
        )
    '''

    def serialize(self):
        dictionary = {}
        dictionary['index_start'] = self.index_start
        dictionary['index_end'] = self.index_end
        dictionary['progress'] = self.progress
        dictionary['type'] = self.type
        return dictionary
    
    def deserialize(self, dictionary: dict) -> None:
        if dictionary['type'] != self.type:
            raise ValueError
        self.index_start = dictionary['index_start']
        self.index_end = dictionary['index_end']
        self.progress = dictionary['progress']


if __name__ == '__main__':

    from piperabm.transportation.samples import transportation_0 as transportation
    '''
    track = Track(
        pos_start=[0, 0],
        pos_end=[100, 100],
        adjustment_factor=1
    )
    #delta_time = 60
    #pos = track.pos(delta_time, transportation)
    #print(pos)
    track.print
    '''