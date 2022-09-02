from multiprocessing import connection
import unittest

from graph import Graph, Node
from model import Link, Resource, Entity, Model


class TestLink(unittest.TestCase):
    ''' tests related to Link class '''
    def test_adding_neighbor_to_entities(self):
        link = Link(end='city_1')
        link.chance = 1
        link.active = False
        self.assertFalse(link.active)


class TestResources(unittest.TestCase):
    ''' tests related to Resource class '''
    def test_adding_resource_to_entities(self):
        ''' tests adding resources to entities '''
        from samples import r1_1, r2_1, r3_1
        e_1 = Entity(
        name = 'city_1',
        resources=[r1_1, r2_1, r3_1]
            )
        self.assertEqual(len(e_1.resources), 3)

    def test_is_alive(self):
        ''' tests entity.is_alive() function '''
        r1_1 = Resource(
            name = 'water',
            source = 5,
            demand = 4,
            deficiency_current = 20,
            deficiency_max = 10,
            storage_current = 2,
            storage_max = 10
            )
        e_1 = Entity(
        name = 'city_1',
        resources=[r1_1]
            )
        self.assertFalse(e_1.is_alive())


class TestEntity(unittest.TestCase):
    ''' tests related to Entity class '''
    def test_adding_neighbor_to_entities(self):
        ''' tests adding neighbors to entities '''
        r_1 = Resource(
            name = 'water',
            connections = [Link(end='city_2')]
            )
        e_1 = Entity(
            name = 'city_1',
            resources = [r_1]
            )
        r_2 = Resource(
            name = 'water',
            connections = []
            )
        e_2 = Entity(
            name = 'city_2',
            resources = [r_2]
            )

        m = Model(entities=[e_1, e_2])
        self.assertTrue(m.analyze())


if __name__ == '__main__':
    unittest.main()