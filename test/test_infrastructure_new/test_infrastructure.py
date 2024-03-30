import unittest

from piperabm.infrastructure_new import Infrastructure, Street, Junction


class TestInfrastructureClass(unittest.TestCase):

    def setUp(self):
        self.infrastructure = Infrastructure(proximity_radius=1)
        object_1 = Street(pos_1=[0, 0.1], pos_2=[0, 10])
        object_2 = Street(pos_1=[0.1, 0], pos_2=[10, 0])
        self.infrastructure.add(object_1)
        self.infrastructure.add(object_2)

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
        print(new_id)
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


if __name__ == '__main__':
    unittest.main()