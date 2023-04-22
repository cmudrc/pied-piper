import unittest

from piperabm.unit import Date
from piperabm.environment import Environment
from piperabm.environment.elements.link.samples import link_0


class TestAddClass_Hub(unittest.TestCase):

    def setUp(self):
        self.env = Environment()

    def test_add_edge(self):
        self.env.add_edge(start_index=0, end_index=1, element=link_0)
        edges = self.env.G.edges()
        self.assertListEqual(list(edges), [(0, 1)])
        
    def test_input_to_index(self):
        start_index, end_index = self.env.input_to_index_edge(
            _from=[0, 0],
            _to=[1, 0]
        )
        self.assertEqual(start_index, 0)
        self.assertEqual(end_index, 1)

    def test_add_link_object(self):
        self.env.add_link_object(
            _from=[0, 0],
            _to=[1, 0],
            link=link_0
        )
        edges = self.env.G.edges()
        self.assertListEqual(list(edges), [(0, 1)])
    '''
    def test_add_hub(self):
        self.env.add_hub(
            name='',
            pos=[0, 0],
            start_date=Date(2020, 1, 1),
            end_date=Date(2020, 1, 2),
            structure=None
        )
        nodes = self.env.G.nodes()
        self.assertListEqual(list(nodes), [0])
        
    def test_add_settlement(self):
        self.env.add_settlement(
            name='',
            pos=[0, 0],
            boundary=None,
            active=True,
            start_date=None,
            end_date=None,
            sudden_degradation_dist=None,
            sudden_degradation_unit_size=None,
            progressive_degradation_formula=None,
            progressive_degradation_current=None,
            progressive_degradation_max=None
        )
        nodes = self.env.G.nodes()
        self.assertListEqual(list(nodes), [0])
    '''

if __name__ == "__main__":
    unittest.main()