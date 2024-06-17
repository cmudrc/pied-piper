import unittest

from piperabm.infrastructure import Infrastructure, Street, Junction, Home


class TestInfrastructureClass(unittest.TestCase):

    def setUp(self):
        self.infrastructure = Infrastructure()
        object_1 = Street(pos_1=[0, 0.1], pos_2=[0, 10])
        object_2 = Street(pos_1=[0.1, 0], pos_2=[10, 0])
        self.infrastructure.add(object_1, id=1)
        self.infrastructure.add(object_2, id=2)

    def test_find_node_by_pos(self):
        id = self.infrastructure.find_node_by_pos([0.01, 0.1])
        object = self.infrastructure.get(id)
        self.assertEqual(object.pos, [0, 0.1])

    def test_replace_node(self):
        # Old id
        id = self.infrastructure.find_node_by_pos([0.1, 0])
        # New id
        new_node = Junction(pos=[0, 0])
        new_id = self.infrastructure.add(new_node)
        # Replace
        self.infrastructure.replace_node(id, new_id)
        # Check
        edges_ids = self.infrastructure.adjacents_ids(new_id)
        edge_id = self.infrastructure.edge_id(*edges_ids[0])
        id = self.infrastructure.find_node_by_pos([0, 0])
        node_object = self.infrastructure.get(id)
        edge_object = self.infrastructure.get(edge_id)
        result = node_object.pos == edge_object.pos_1 or \
            node_object.pos == edge_object.pos_2
        self.assertTrue(result)
        self.assertEqual(len(self.infrastructure.junctions), 4)
        self.assertEqual(len(self.infrastructure.streets), 2)
        self.assertEqual(len(self.infrastructure.library), 6)

    def test_edges_closer_than(self):
        edges_id = self.infrastructure.edges_closer_than(pos=[10, 1], max_distance=3)
        self.assertEqual(len(edges_id), 1)
        edges_id = self.infrastructure.edges_closer_than(pos=[10, 1], max_distance=13)
        self.assertEqual(len(edges_id), 2)

    def test_bake(self):
        self.assertFalse(self.infrastructure.baked)
        self.assertFalse(self.infrastructure.baked_streets)
        self.assertFalse(self.infrastructure.baked_neighborhood)
        self.assertEqual(len(self.infrastructure.junctions), 4)
        self.assertEqual(len(self.infrastructure.streets), 2)
        self.infrastructure.bake(proximity_radius=1) # bake
        self.assertTrue(self.infrastructure.baked)
        self.assertTrue(self.infrastructure.baked_streets)
        self.assertTrue(self.infrastructure.baked_neighborhood)
        self.assertEqual(len(self.infrastructure.junctions), 3)
        self.assertEqual(len(self.infrastructure.streets), 2)

    def test_path(self):
        object = Home(pos=[5, 2])
        self.infrastructure.add(object, id=3)
        object = Home(pos=[2, 5])
        self.infrastructure.add(object, id=4)
        self.assertEqual(len(list(self.infrastructure.paths.G.nodes())), 0)
        self.assertEqual(len(list(self.infrastructure.paths.G.edges())), 0)
        self.infrastructure.bake(proximity_radius=1) # bake
        #self.infrastructure.show()
        self.assertEqual(len(list(self.infrastructure.paths.G.nodes())), 2)
        self.assertEqual(len(list(self.infrastructure.paths.G.edges())), 3)

    def test_remove_edges(self):
        self.infrastructure.bake(proximity_radius=1)
        self.infrastructure.removes_edges(id_list=[1])
        self.assertEqual(len(self.infrastructure.junctions), 2)
        self.assertEqual(len(self.infrastructure.streets), 1)

    def test_serialization(self):
        dictionary = self.infrastructure.serialize()
        new = Infrastructure()
        new.deserialize(dictionary)
        self.assertEqual(self.infrastructure, new)
        

if __name__ == "__main__":
    unittest.main()