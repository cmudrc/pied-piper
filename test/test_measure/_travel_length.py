import unittest

from piperabm.measure import TravelLength


class TestTravelLengthClass(unittest.TestCase):

    def setUp(self):
        self.tl = TravelLength()
        self.tl.add(length=10, duration=10)
        self.tl.add(length=20, duration=15)
        self.tl.add(length=30, duration=10)

        #tl.show()

    def test_total(self):
        self.assertEqual(self.tl.total(), 60)


if __name__ == "__main__":
    unittest.main()
