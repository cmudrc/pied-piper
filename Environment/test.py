from multiprocessing import connection
import unittest

from graph import Graph, Node
from model import Resource, Entity, Model


class TestEntity(unittest.TestCase):
    def test_adding_resource_to_entities(self):
        """
        Test adding resources to entities
        """
        r1_1 = Resource(
            name = 'water',
            source = 5,
            demand = 4,
            deficiency_current = 0,
            deficiency_max = 10,
            storage_current = 2,
            storage_max = 10
            )
        r2_1 = Resource(
            name = 'energy',
            source = 7,
            demand = 4,
            deficiency_current = 0,
            deficiency_max = 12,
            storage_current = 0,
            storage_max = 8
            )
        r3_1 = Resource(
            name = 'food',
            source = 4,
            demand = 5,
            deficiency_current = 9,
            deficiency_max = 8,
            storage_current = 3,
            storage_max = 15
            )
        e_1 = Entity(
        name = 'city_1',
        resources=[r1_1, r2_1, r3_1]
            )
        self.assertEqual(len(e_1.resources), 3)

    def test_is_alive(self):
        """
        Test entity.is_alive() function
        """
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

    def test_adding_neighbor_to_entities(self):
        """
        Test adding neighbors to entities
        """
        r_1 = Resource(
            name = 'water',
            connections = ['city_2']
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