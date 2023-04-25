import unittest
from copy import deepcopy

from piperabm.environment.samples import environment_1
from piperabm.unit import Date


class TestEnvironmentQuery(unittest.TestCase):

    def setUp(self) -> None:
        self.env = deepcopy(environment_1)

    def test_oldest_date(self):
        date = self.env.oldest_date()
        self.assertEqual(date, Date(2020, 1, 2))


if __name__ == "__main__":
    unittest.main()