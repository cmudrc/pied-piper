from transportation import Foot
from model import Model
from difflib import unified_diff
import unittest


#################################### model.py ####################################

from datetime import date

from tools import Unit
from infrastructure import Road


class City:
    """
    A helper class.
    """
    
    def __init__(self, name, pos):
        self.name = name
        self.pos = pos


class TestRoadClass(unittest.TestCase):
    def test_road_length_calc(self):
        r = Road(
            start_node='city_1',
            end_node='city_2'
        )
        all_nodes = [
            City(name='city_1', pos=[0, 0]),
            City(name='city_2', pos=[0, 1]),
        ]
        length = r.length_calc(all_nodes=all_nodes)
        self.assertEqual(length, 1, msg="Should be equal")


#################################### transportation.py ####################################

from datetime import date

from tools import Unit
from infrastructure import Road


class TestModelClass(unittest.TestCase):
    def test_infrastructure_update_0(self):
        infrastructures = [
            Road(
                start_node='city_1',
                end_node='city_2',
                double_sided=True,
                name='sample road',
                initiation_date=date(2000, 1, 1),
                distribution={
                    'type': 'dirac delta',
                    'main': Unit(10, 'day'),
                },
                seed=None
            )
        ]
        m = Model(
            step_size=Unit(15, 'day'),
            current_step=0,
            current_date=date(2000, 1, 1),
            infrastructures=infrastructures,
        )
        m.run_step()
        self.assertEqual(len(m.current_infrastructures),
                         0, msg="Should be equal")

    def test_infrastructure_update_1(self):
        infrastructures = [
            Road(
                start_node='city_1',
                end_node='city_2',
                double_sided=True,
                name='sample road',
                initiation_date=date(2000, 1, 1),
                distribution={
                    'type': 'dirac delta',
                    'main': Unit(10, 'day'),
                },
                seed=None
            )
        ]
        m = Model(
            step_size=Unit(5, 'day'),
            current_step=0,
            current_date=date(2000, 1, 1),
            infrastructures=infrastructures,
        )
        m.run_step()
        self.assertEqual(len(m.current_infrastructures),
                         1, msg="Should be equal")


#################################### transportation.py ####################################


class TestTransportationClass(unittest.TestCase):
    def test_how_long(self):
        transportation = Foot(speed=Unit(5, 'km/h'))
        delta_t = transportation.how_long([0, 0], [1, 0])  # km
        dt_minutes = delta_t.seconds / 60
        self.assertEqual(dt_minutes, 12, msg="Should be equal")

    def test_how_much_fuel(self):
        transportation = Foot(
            speed=Unit(5, 'km/h'),
            fuel_rate=Unit(1, 'kg/h')  # food
        )
        delta_m = transportation.how_much_fuel([0, 0], [1, 0])  # km
        self.assertEqual(delta_m['food'], 0.2, msg="Should be equal")


if __name__ == '__main__':
    unittest.main()
