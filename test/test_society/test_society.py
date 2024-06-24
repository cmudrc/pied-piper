import unittest

from piperabm.infrastructure.samples import model_0, model_1, model_2


class TestSocietyClass_0(unittest.TestCase):

    def setUp(self):
        self.model = model_0
        self.home_id = self.model.infrastructure.homes[0]

    def test_relationships(self):
        # Add agent 1
        self.model.society.add_agent(
            home_id=self.home_id,
            id=1
        )
        self.assertEqual(self.model.society.stat['node']['total'], 1)
        self.assertEqual(self.model.society.stat['edge']['family'], 0)
        self.assertEqual(self.model.society.stat['edge']['friend'], 0)
        self.assertEqual(self.model.society.stat['edge']['neighbor'], 0)
        
        # Add agent 2 to the same home
        self.model.society.add_agent(
            home_id=self.home_id,
            id=2
        )
        self.assertEqual(self.model.society.stat['node']['total'], 2)
        self.assertEqual(self.model.society.stat['edge']['family'], 1)
        self.assertEqual(self.model.society.stat['edge']['friend'], 0)
        self.assertEqual(self.model.society.stat['edge']['neighbor'], 0)

        # Family can also be friend
        self.model.society.add_friend(id_1=1, id_2=2)
        self.assertEqual(self.model.society.stat['node']['total'], 2)
        self.assertEqual(self.model.society.stat['edge']['family'], 1)
        self.assertEqual(self.model.society.stat['edge']['friend'], 1)
        self.assertEqual(self.model.society.stat['edge']['neighbor'], 0)

    def test_serialization(self):
        edges = self.model.society.edges
        #print(edges)
        attrs = self.model.society.get_edge_attributes(ids=edges[0])
        print(attrs)
        print(self.model.society.serialize())


class TestSocietyClass_2(unittest.TestCase):

    def setUp(self):
        self.model = model_2
        homes = self.model.infrastructure.homes
        self.model.society.neighbor_radius = 270
        self.model.society.add_agent(home_id=homes[0], id=1)
        self.model.society.add_agent(home_id=homes[0], id=2)
        self.model.society.add_agent(home_id=homes[1], id=3)
        self.model.society.add_friend(id_1=2, id_2=3)

    def test_relationships(self):
        self.assertEqual(self.model.society.stat['node']['total'], 3)
        self.assertEqual(self.model.society.stat['edge']['family'], 1)
        self.assertEqual(self.model.society.stat['edge']['friend'], 1)
        self.assertEqual(self.model.society.stat['edge']['neighbor'], 2)


if __name__ == "__main__":
    unittest.main()