import unittest

from piperabm.model import Model
from piperabm.infrastructure import Road
from piperabm.society import Agent
from piperabm.actions.move_new.track_new import TrackNew
from piperabm.transportation.samples import transportation_0 as transportation


class TestTrackClass(unittest.TestCase):

    def setUp(self):
        self.model = Model(
            proximity_radius=1,  # Meters
            step_size=60  # Seconds
        )

        self.pos_1 = [0, 0]
        self.pos_2 = [5000, 0]
        road = Road(
            pos_1=self.pos_1,
            pos_2=self.pos_2,
            roughness=2
        )
        self.model.add(road)
        '''
        agent = Agent(name="Sample")
        agent.queue.add(move)
        '''
        index_start, _ = self.model.find_nearest_node(pos=self.pos_1)
        index_end, _ = self.model.find_nearest_node(pos=self.pos_2)
        self.track = TrackNew(index_start, index_end)
        self.track.model = self.model

    def test_pos_start_pos_end(self):
        self.assertEqual(self.track.pos_start, self.pos_1)
        self.assertEqual(self.track.pos_end, self.pos_2)

    def test_length(self):
        self.assertEqual(self.track.length_real, 5000)
        self.assertEqual(self.track.length_adjusted, 10000)

    def test_vector(self):
        self.assertListEqual(list(self.track.vector), [5000, 0])
        self.assertListEqual(list(self.track.unit_vector), [1, 0])

    def test_progress_state(self):
        self.assertFalse(self.track.started)
        self.assertFalse(self.track.done)

    def test_progress_by_pos(self):
        pos = [0, 0]
        progress = self.track.progress_by_pos(pos)
        self.assertEqual(progress, 0)

        pos = [2500, 0]
        progress = self.track.progress_by_pos(pos)
        self.assertEqual(progress, 0.5)

        pos = [5000, 0]
        progress = self.track.progress_by_pos(pos)
        self.assertEqual(progress, 1)
    
    '''
    def test_duration(self):
        self.assertEqual(self.track.duration(transportation).total_seconds(), 7200)
    '''
    def test_pos_by_progress(self):
        progress = -0.5
        pos = self.track.pos_by_progress(progress)
        self.assertListEqual(pos, [0, 0])

        progress = 0
        pos = self.track.pos_by_progress(progress)
        self.assertListEqual(pos, [0, 0])

        progress = 0.5
        pos = self.track.pos_by_progress(progress)
        self.assertListEqual(pos, [2500, 0])

        progress = 1
        pos = self.track.pos_by_progress(progress)
        self.assertListEqual(pos, [5000, 0])

        progress = 1.5
        pos = self.track.pos_by_progress(progress)
        self.assertListEqual(pos, [5000, 0])

    def test_pos(self):
        delta_time = 0
        pos = self.track.pos(delta_time, transportation)
        self.assertListEqual(pos, [0, 0])

        delta_time = 3600
        pos = self.track.pos(delta_time, transportation)
        self.assertListEqual(pos, [2500, 0])

        delta_time = 7200
        pos = self.track.pos(delta_time, transportation)
        self.assertListEqual(pos, [5000, 0])

    def test_update(self):
        step_size = 3600

        self.track.update(step_size, transportation)
        self.assertEqual(self.track.progress, 0.5)

        self.track.update(step_size, transportation)
        self.assertEqual(self.track.progress, 1)

    
if __name__ == '__main__':
    unittest.main()