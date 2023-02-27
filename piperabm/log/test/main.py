from class_1 import First
from class_2 import Second


class Test:

    def do(self):
        f = First()
        f.do()
        s = Second()
        s.do()


if __name__ == "__main__":
    from piperabm.log import Log
    log = Log()
    log.reset()
    
    t = Test()
    t.do()