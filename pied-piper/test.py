import unittest


from datetime import date

from model import Model
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
        self.assertEqual(len(m.current_infrastructures), 0, msg="Should be equal")

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
        self.assertEqual(len(m.current_infrastructures), 1, msg="Should be equal")


if __name__ == '__main__':
    unittest.main()