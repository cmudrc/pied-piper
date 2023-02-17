import unittest

from piperabm.measure import TravelLength


class TestTravelLengthClass(unittest.TestCase):

    tl = TravelLength()
    tl.add(length=10, duration=10)
    tl.add(length=20, duration=15)
    tl.add(length=30, duration=10)

    def test_total(self):
        self.assertEqual(self.tl.total(), 60)

    def test_show(self):
        self.tl.to_plt()
        #self.tl.show()


if __name__ == "__main__":
    unittest.main()
