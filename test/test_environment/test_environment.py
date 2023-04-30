import unittest
from copy import deepcopy

from piperabm.environment import Environment
from piperabm.environment.samples import environment_0, environment_1
from piperabm.unit import Date


class TestEnvironmentClass_0(unittest.TestCase):

    def setUp(self):
        self.env = deepcopy(environment_0)

    def test_dict(self):
        dictionary = self.env.to_dict()
        expected_result = {
            'edges': [],
            'nodes': [{'index': 0,
                       'pos': [-2, -2],
                       'structure': {'active': True,
                                     'boundary': {'shape': {'radius': 2.220446049250313e-16,
                                                            'type': 'dot'}},
                                     'end_date': None,
                                     'name': "John's Home",
                                     'progressive_degradation': {'formula_name': 'formula_01',
                                                                 'usage_current': 0,
                                                                 'usage_max': float('inf')},
                                     'start_date': {'day': 2,
                                                    'hour': 0,
                                                    'minute': 0,
                                                    'month': 1,
                                                    'second': 0,
                                                    'year': 2020},
                                     'sudden_degradation': {'distribution': {'main': 864000.0,
                                                                             'type': 'dirac '
                                                                             'delta'},
                                                            'unit_size': None},
                                     'type': 'settlement'}}],
            'type': 'environment'
        }
        self.maxDiff = None
        self.assertDictEqual(dictionary, expected_result)
        new_env = Environment()
        new_env.from_dict(dictionary)
        new_dictionary = new_env.to_dict()
        self.assertDictEqual(dictionary, new_dictionary)

    def test_delta(self):
        start_date = Date(2020, 1, 5)
        end_date = Date(2020, 1, 15)
        self.env.update(start_date, end_date)
        env_old = deepcopy(environment_0)
        delta = self.env - env_old
        expected_delta = {'nodes': {0: {'structure': {'active': True}}}}
        self.assertDictEqual(delta, expected_delta)


class TestEnvironmentClass_1(unittest.TestCase):

    def setUp(self):
        self.env = deepcopy(environment_1)

    def test_shape(self):
        edges = self.env.G.edges()
        self.assertEqual(len(edges), 2)
        self.assertListEqual(list(edges), [(0, 2), (1, 2)])
        nodes = self.env.G.nodes()
        self.assertEqual(len(nodes), 3)
        self.assertListEqual(list(nodes), [0, 1, 2])

    def test_delta(self):
        env = deepcopy(self.env)
        start_date = Date(2020, 1, 5)
        end_date = Date(2020, 1, 15)
        env.update(start_date, end_date)
        env_old = deepcopy(self.env)
        delta = env - env_old
        expected_delta = {
            'nodes': {
                0: {'structure': {'active': True}},
                1: {'structure': {'active': True}}
            },
            'edges': {
                0: {'structure': {'active': True}},
                1: {'structure': {'active': True}}
            }
        }
        self.assertDictEqual(delta, expected_delta)

    def test_dict(self):
        dictionary = self.env.to_dict()
        # self.env.print()
        expected_result = {'edges': [{'index_end': 2,
                                      'index_start': 0,
                                      'structure': {'active': True,
                                                    'actual_length': None,
                                                    'boundary': {'shape': {'angle': 0.090659887200745,
                                                                           'height': 2.220446049250313e-16,
                                                                           'type': 'rectangle',
                                                                           'width': 22.090722034374522}},
                                                    'difficulty': 1,
                                                    'end_date': None,
                                                    'name': 'Halfway 0',
                                                    'progressive_degradation': {'formula_name': 'formula_01',
                                                                                'usage_current': 0,
                                                                                'usage_max': float('inf')},
                                                    'start_date': {'day': 2,
                                                                   'hour': 0,
                                                                   'minute': 0,
                                                                   'month': 1,
                                                                   'second': 0,
                                                                   'year': 2020},
                                                    'sudden_degradation': {'distribution': {'main': 864000.0,
                                                                                            'type': 'dirac '
                                                                                            'delta'},
                                                                           'unit_size': None},
                                                    'type': 'road'}},
                                     {'index_end': 2,
                                      'index_start': 1,
                                      'structure': {'active': True,
                                                    'actual_length': None,
                                                    'boundary': {'shape': {'angle': 1.5707963267948966,
                                                                           'height': 2,
                                                                           'type': 'rectangle',
                                                                           'width': 20.0}},
                                                    'difficulty': 1.5,
                                                    'end_date': None,
                                                    'name': 'Halfway 1',
                                                    'progressive_degradation': {'formula_name': 'formula_01',
                                                                                'usage_current': 0,
                                                                                'usage_max': float('inf')},
                                                    'start_date': {'day': 4,
                                                                   'hour': 0,
                                                                   'minute': 0,
                                                                   'month': 1,
                                                                   'second': 0,
                                                                   'year': 2020},
                                                    'sudden_degradation': {'distribution': {'main': 864000.0,
                                                                                            'type': 'dirac '
                                                                                            'delta'},
                                                                           'unit_size': None},
                                                    'type': 'road'}}],
                           'nodes': [{'index': 0,
                                      'pos': [-2, -2],
                                      'structure': {'active': True,
                                                    'boundary': {'shape': {'radius': 2.220446049250313e-16,
                                                                           'type': 'dot'}},
                                                    'end_date': None,
                                                    'name': "John's Home",
                                                    'progressive_degradation': {'formula_name': 'formula_01',
                                                                                'usage_current': 0,
                                                                                'usage_max': float('inf')},
                                                    'start_date': {'day': 2,
                                                                   'hour': 0,
                                                                   'minute': 0,
                                                                   'month': 1,
                                                                   'second': 0,
                                                                   'year': 2020},
                                                    'sudden_degradation': {'distribution': {'main': 864000.0,
                                                                                            'type': 'dirac '
                                                                                            'delta'},
                                                                           'unit_size': None},
                                                    'type': 'settlement'}},
                                     {'index': 1,
                                      'pos': [20, 20],
                                      'structure': {'active': True,
                                                    'boundary': {'shape': {'radius': 5,
                                                                           'type': 'circle'}},
                                                    'end_date': None,
                                                    'name': "Peter's Home",
                                                    'progressive_degradation': {'formula_name': 'formula_01',
                                                                                'usage_current': 0,
                                                                                'usage_max': float('inf')},
                                                    'start_date': {'day': 4,
                                                                   'hour': 0,
                                                                   'minute': 0,
                                                                   'month': 1,
                                                                   'second': 0,
                                                                   'year': 2020},
                                                    'sudden_degradation': {'distribution': {'main': 864000.0,
                                                                                            'type': 'dirac '
                                                                                            'delta'},
                                                                           'unit_size': None},
                                                    'type': 'settlement'}},
                                     {'index': 2, 'pos': [20, 0], 'structure': None}],
                           'type': 'environment'}
        self.maxDiff = None
        self.assertDictEqual(dictionary, expected_result)
        new_env = Environment()
        new_env.from_dict(dictionary)
        new_dictionary = new_env.to_dict()
        self.assertDictEqual(dictionary, new_dictionary)
        # print(dictionary)


'''
    def test_edge_boundary_creation(self):
        settlement_0 = self.env.get_node_element(0)
        settlement_1 = self.env.get_node_element(1)
        hub = self.env.get_node_element(2)
        
        road_0 = self.env.get_edge_element(0, 2)
        road_1 = self.env.get_edge_element(1, 2)

        pos_settlement_0 = settlement_0.pos
        pos_settlement_1 = settlement_1.pos
        pos_hub = hub.pos

        shape_road_0 = road_0.structure.boundary.shape
        shape_road_1 = road_1.structure.boundary.shape

        self.assertListEqual(pos_settlement_0, [-2, -2])
        self.assertListEqual(pos_settlement_1, [20, 20])
        self.assertListEqual(pos_hub, [20, 0])

        angle_0 = slope(start_pos=pos_settlement_0, end_pos=pos_hub)
        angle_1 = slope(start_pos=pos_hub, end_pos=pos_settlement_1)

        length_0 = euclidean_distance(start_pos=pos_settlement_0, end_pos=pos_hub)
        length_1 = euclidean_distance(start_pos=pos_hub, end_pos=pos_settlement_1)

        self.assertEqual(shape_road_0.angle, angle_0)
        self.assertEqual(shape_road_1.angle, angle_1)

        print(road_0)
        self.assertEqual(shape_road_0.width, length_0)
        self.assertEqual(road_0.length('ideal'), length_0)
        self.assertEqual(shape_road_1.width, length_1)
        self.assertEqual(road_1.length('ideal'), length_1)
        

        self.assertEqual(road_0.width(), 2)
        self.assertEqual(road_1.width(), 2)
'''


'''
class TestEnvironmentClass1(unittest.TestCase):

    def setUp(self):
        self.env = env_0

    def test_find_node(self):
        env = deepcopy(self.env)
        index = env.find_node("John's Home")
        self.assertEqual(index, 0, msg="find node by name")
        index = env.find_node([-1, -1])
        self.assertEqual(index, 0, msg="find node by pos")
        index = env.find_node(0)
        self.assertEqual(index, 0, msg="find node by index")

    def test_edge_info_path(self):
        env = deepcopy(self.env)
        start_date = Date(2020, 1, 5)
        end_date = Date(2020, 1, 7)
        env.update_elements(start_date, end_date)
        path_graph = env.to_path_graph(start_date, end_date)
        all_settlements = env.all_nodes('settlement')
        path = path_graph.edge_info(all_settlements[0], all_settlements[1], 'path')
        expected_result = [0, 2, 1]
        self.assertListEqual(path.path, expected_result)
        self.assertEqual(0, path.start_pos())
        self.assertEqual(1, path.end_pos())

    def test_path(self): ###########
        env = deepcopy(self.env)
        start_date = Date(2020, 1, 5)
        end_date = Date(2020, 1, 7)
        env.update_elements(start_date, end_date)
        path_graph = env.to_path_graph(start_date, end_date)
        all_settlements = env.all_nodes('settlement')
        path = path_graph.edge_info(all_settlements[0], all_settlements[1], 'path')
        #result = path.path
        #self.assertListEqual(result, expected_result)

    def test_all_settlements(self):
        settlements = self.env.all_nodes('settlement')
        self.assertEqual(len(settlements), 2)

    def test_node_info(self):
        env = deepcopy(self.env)
        info = env.node_info(
            node=0,
            property="boundary"
        )
        expected_result = [-2, -2]
        self.assertListEqual(info.center, expected_result)
        node_type = env.node_info("Peter's Home", 'type')
        self.assertEqual(node_type, 'settlement')

    def test_edge_info(self):
        env = deepcopy(self.env)
        info = env.edge_info(
            start="John's Home",
            end=[20, 0],
            property="initiation_date"
        )
        expected_result = Date(2020, 1, 2)
        self.assertEqual(info.year, expected_result.year)
        self.assertEqual(info.month, expected_result.month)
        self.assertEqual(info.day, expected_result.day)


class TestEnvironmentClass2(unittest.TestCase):

    def setUp(self):
        self.env = env_1

    #env.show(Date.today(), Date.today()+DT(hours=1))

    def to_link_graph(self):
        env = deepcopy(self.env)
        start_date = Date.today()
        end_date = start_date + DT(days=3)
        link_graph = env.to_link_graph(start_date, end_date)

    def to_path_graph(self):
        env = deepcopy(self.env)
        start_date = Date.today()
        end_date = start_date + DT(days=3)
        path_graph = env.to_path_graph(start_date, end_date)
'''

if __name__ == "__main__":
    unittest.main()
