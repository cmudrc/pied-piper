#from log import Log
from piperabm.log import Log


class Second:

    log = Log()
    
    def do(self):
        self.log.add('from second')


if __name__ == "__main__":
    s = Second()
    s.do()