import unittest
from piperabm.resource import Resource


class TestResource(unittest.TestCase):

    def setUp(self) -> None:
        self.resource_dict = {"food": 10, "water": 20, "energy": 30}
        self.resource = Resource(**self.resource_dict)

    def test_resource(self):
        self.assertDictEqual(dict(self.resource), self.resource_dict)

    def test_resource_addition(self):
        other_resource_dict = {"food": 10, "water": 20, "energy": 30}
        other_resource = Resource(**other_resource_dict)
        resource = self.resource + other_resource
        expected_dict = {
            "food": self.resource_dict["food"] + other_resource_dict["food"],
            "water": self.resource_dict["water"] + other_resource_dict["water"],
            "energy": self.resource_dict["energy"] + other_resource_dict["energy"],
        }
        self.assertDictEqual(dict(resource), expected_dict)

    def test_resource_addition_dict(self):
        other_resource_dict = {"food": 10, "water": 20, "energy": 30}
        resource = self.resource + other_resource_dict
        expected_dict = {
            "food": self.resource_dict["food"] + other_resource_dict["food"],
            "water": self.resource_dict["water"] + other_resource_dict["water"],
            "energy": self.resource_dict["energy"] + other_resource_dict["energy"],
        }
        self.assertDictEqual(dict(resource), expected_dict)

    def test_resource_subtraction(self):
        other_resource_dict = {"food": 10, "water": 20, "energy": 30}
        other_resource = Resource(**other_resource_dict)
        resource = self.resource - other_resource
        expected_dict = {
            "food": self.resource_dict["food"] - other_resource_dict["food"],
            "water": self.resource_dict["water"] - other_resource_dict["water"],
            "energy": self.resource_dict["energy"] - other_resource_dict["energy"],
        }
        self.assertDictEqual(dict(resource), expected_dict)

    def test_resource_subtraction_dict(self):
        other_resource_dict = {"food": 10, "water": 20, "energy": 30}
        resource = self.resource - other_resource_dict
        expected_dict = {
            "food": self.resource_dict["food"] - other_resource_dict["food"],
            "water": self.resource_dict["water"] - other_resource_dict["water"],
            "energy": self.resource_dict["energy"] - other_resource_dict["energy"],
        }
        self.assertDictEqual(dict(resource), expected_dict)

    def test_resource_multiplication(self):
        resource = self.resource * 2
        expected_dict = {
            "food": self.resource_dict["food"] * 2,
            "water": self.resource_dict["water"] * 2,
            "energy": self.resource_dict["energy"] * 2,
        }
        self.assertDictEqual(dict(resource), expected_dict)

    def test_resource_multiplication_dict(self):
        resource = self.resource * {"food": 2}
        expected_dict = {
            "food": self.resource_dict["food"] * 2,
            "water": self.resource_dict["water"] * 1,
            "energy": self.resource_dict["energy"] * 1,
        }
        self.assertDictEqual(dict(resource), expected_dict)

    def test_resource_division(self):
        resource = self.resource / 2
        expected_dict = {
            "food": self.resource_dict["food"] / 2,
            "water": self.resource_dict["water"] / 2,
            "energy": self.resource_dict["energy"] / 2,
        }
        self.assertDictEqual(dict(resource), expected_dict)

    def test_resource_division_dict(self):
        resource = self.resource / {"food": 2}
        expected_dict = {
            "food": self.resource_dict["food"] / 2,
            "water": self.resource_dict["water"] / 1,
            "energy": self.resource_dict["energy"] / 1,
        }
        self.assertDictEqual(dict(resource), expected_dict)

    def test_len(self):
        self.assertEqual(self.resource.__len__(), 3)

    def test_getitem(self):
        self.assertEqual(self.resource.__getitem__("food"), self.resource_dict["food"])
        self.assertEqual(self.resource.__getitem__("water"), self.resource_dict["water"])
        self.assertEqual(self.resource.__getitem__("energy"), self.resource_dict["energy"])

    def test_iter(self):
        self.assertEqual(
            list(iter(self.resource)),
            [("food", 10), ("water", 20), ("energy", 30)],
        )


if __name__ == "__main__":
    unittest.main()
