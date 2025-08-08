import unittest
from copy import deepcopy

from piperabm.society import Society
from piperabm.infrastructure.samples.infrastructure_0 import model as model_0
from piperabm.infrastructure.samples.infrastructure_2 import model as model_2


class TestSocietyClass_0(unittest.TestCase):

    def setUp(self) -> None:
        self.model = deepcopy(model_0)
        self.home_id = self.model.infrastructure.homes[0]

    def test_relationships(self):
        # Add agent 1
        self.model.society.add_agent(home_id=self.home_id, id=1)
        # print(self.model.society.stat) ######
        self.assertEqual(self.model.society.stat["node"]["total"], 1)
        self.assertEqual(self.model.society.stat["edge"]["family"], 0)
        self.assertEqual(self.model.society.stat["edge"]["friend"], 0)
        self.assertEqual(self.model.society.stat["edge"]["neighbor"], 0)

        # Add agent 2 to the same home
        self.model.society.add_agent(home_id=self.home_id, id=2)
        self.assertEqual(self.model.society.stat["node"]["total"], 2)
        self.assertEqual(self.model.society.stat["edge"]["family"], 1)
        self.assertEqual(self.model.society.stat["edge"]["friend"], 0)
        self.assertEqual(self.model.society.stat["edge"]["neighbor"], 0)

        # Family can also be friend
        self.model.society.add_friend(id_1=1, id_2=2)
        self.assertEqual(self.model.society.stat["node"]["total"], 2)
        self.assertEqual(self.model.society.stat["edge"]["family"], 1)
        self.assertEqual(self.model.society.stat["edge"]["friend"], 1)
        self.assertEqual(self.model.society.stat["edge"]["neighbor"], 0)


class TestSocietyClass_2(unittest.TestCase):

    def setUp(self) -> None:
        self.model = deepcopy(model_2)
        homes = self.model.infrastructure.homes
        self.model.society.neighbor_radius = 270
        self.model.society.add_agent(home_id=homes[0], id=1)
        self.model.society.add_agent(home_id=homes[0], id=2)
        self.model.society.add_agent(home_id=homes[1], id=3)
        self.model.society.add_friend(id_1=2, id_2=3)

    def test_relationships(self):
        self.assertEqual(self.model.society.stat["node"]["total"], 3)
        self.assertEqual(self.model.society.stat["edge"]["family"], 1)
        self.assertEqual(self.model.society.stat["edge"]["friend"], 1)
        self.assertEqual(self.model.society.stat["edge"]["neighbor"], 2)

    def test_serialization(self):
        society_serialized = self.model.society.serialize()
        society_new = Society()
        society_new.deserialize(society_serialized)
        self.assertDictEqual(society_new.serialize(), society_serialized)


if __name__ == "__main__":
    unittest.main()
