import unittest

import numpy as np

from graph import Graph, Node
from model import Link, Resource, Entity, Model


class TestLinkClass(unittest.TestCase):
    ''' tests related to Link class '''

    def test_adding_neighbor_to_entities(self):
        ''' tests creation and assigning values to a Link instance '''
        link = Link(end='city_1')
        link.chance = 1
        link.active = False
        self.assertFalse(link.active)


class TestResourceClass(unittest.TestCase):
    ''' tests related to Resource class '''

    def test_adding_resource_to_entities(self):
        ''' tests adding resources to entities '''
        from samples import r1_1, r2_1, r3_1
        e_1 = Entity(
            name='city_1',
            resources=[r1_1, r2_1, r3_1]
        )
        self.assertEqual(len(e_1.resources), 3)

    def test_is_alive(self):
        ''' tests entity.is_alive() function '''
        r1_1 = Resource(
            name='water',
            source=5,
            demand=4,
            deficiency_current=20,
            deficiency_max=10,
            storage_current=2,
            storage_max=10
        )
        e_1 = Entity(
            name='city_1',
            resources=[r1_1]
        )
        self.assertFalse(e_1.is_alive())


class TestModelClass(unittest.TestCase):
    ''' tests related to Model class '''

    def test_adding_true_neighbor_to_entities(self):
        ''' tests adding true neighbors to entities '''
        r_1 = Resource(
            name='water',
            connections=[Link(end='city_2')]
        )
        e_1 = Entity(
            name='city_1',
            resources=[r_1]
        )
        r_2 = Resource(
            name='water',
            connections=[]
        )
        e_2 = Entity(
            name='city_2',
            resources=[r_2]
        )

        m = Model(entities=[e_1, e_2])
        self.assertTrue(m.analyze())

    def test_adding_false_neighbor_to_entities(self):
        ''' tests adding false neighbors to entities '''
        r_1 = Resource(
            name='water',
            connections=[Link(end='city_2')]
        )
        e_1 = Entity(
            name='city_1',
            resources=[r_1]
        )
        r_2 = Resource(
            name='water',
            connections=[]
        )
        e_2 = Entity(
            name='city_3',
            resources=[r_2]
        )

        m = Model(entities=[e_1, e_2])
        self.assertFalse(m.analyze())

    def test_json_conversion(self):
        ''' tests json conversion of model '''
        from samples import e_1, e_2

        m = Model(entities=[e_1, e_2])
        m.analyze()
        j = m.to_json()
        m.from_json(j)
        h = m.to_json()
        self.assertEqual(j, h)

class TestGraphClass(unittest.TestCase):
    ''' tests related to Graph class '''
    from samples import n_1, n_2, n_3

    g = n_1 + n_2
    g = n_3 + g
    m_1, i = g.to_matrix()

    g = Graph()
    g.from_matrix(m_1, name=i['name'])
    m_2, i = g.to_matrix()

    np.testing.assert_allclose(m_1, m_2)




if __name__ == '__main__':
    unittest.main()
