import unittest

from piperabm.tools import check_existance
from piperabm.unit import Date


class TestExistanceFunction(unittest.TestCase):

    start_date = Date(2020, 1, 2)
    end_date = Date(2020, 1, 4)

    def test_0(self):
        initiation_date = Date(2020, 1, 1)
        result = check_existance(initiation_date, None, None)
        self.assertTrue(result)

    def test_1(self):
        initiation_date = Date(2020, 1, 1)
        result = check_existance(initiation_date, self.start_date, self.end_date)
        self.assertTrue(result)
    
    def test_2(self):
        initiation_date = Date(2020, 1, 2)
        result = check_existance(initiation_date, self.start_date, self.end_date)
        self.assertTrue(result)

    def test_3(self):
        initiation_date = Date(2020, 1, 3)
        result = check_existance(initiation_date, self.start_date, self.end_date)
        self.assertTrue(result)

    def test_4(self):
        initiation_date = Date(2020, 1, 4)
        result = check_existance(initiation_date, self.start_date, self.end_date)
        self.assertFalse(result)

    def test_5(self):
        initiation_date = Date(2020, 1, 5)
        result = check_existance(initiation_date, self.start_date, self.end_date)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()