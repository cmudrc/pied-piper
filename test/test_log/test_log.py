import unittest
from copy import deepcopy

from piperabm.log import Log


class TestLogClass(unittest.TestCase):


    class First:
        log = Log()
        def do(self):
            self.log.add('first')


    class Second:
        log = Log()
        def do(self):
            self.log.add('second')


    def test_reset(self):
        log = Log()
        log.reset()
        txt = log.show()
        self.assertEqual(len(txt), 0)

    def test_add(self):
        log = Log()
        log.reset()

        f = self.First()
        f.do()
        result = log.show()
        expected_result = 'first' + '\n'
        self.assertEqual(result, expected_result)

        s = self.Second()
        s.do()
        result = log.show()
        expected_result += 'second' + '\n'
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
