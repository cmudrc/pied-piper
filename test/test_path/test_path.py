import unittest

from piperabm.path import Path


class TestPathClass(unittest.TestCase):

    path = Path()
    path.add(pos=[0, 0])
    path.add(pos=[0, 3])
    path.add(pos=[4, 3])
    
    def test_total_length(self):
        self.assertEqual(self.path.total_length(), 7)

    def test_total_length_1(self):
        self.path.add(pos=[0, 0])
        self.assertEqual(self.path.total_length(), 12)

    def test_pos_0(self):
        current_length = 0
        self.assertListEqual(self.path.pos(current_length), [0, 0])

    def test_pos_1(self):
        current_length = 3
        self.assertListEqual(self.path.pos(current_length), [0, 3])

    def test_pos_2(self):
        current_length = 8
        self.assertListEqual(self.path.pos(current_length), [4, 3])

    def test_dict_conversion(self):
        """
        Test to_dict and from_dict methods
        """
        dictionary = self.path.to_dict()
        path_new = Path()
        path_new.from_dict(dictionary)
        dictionary_new = path_new.to_dict()
        self.assertDictEqual(dictionary, dictionary_new)


if __name__ == "__main__":
    unittest.main()