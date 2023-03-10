from piperabm.log import Log


class Log(Log):
    
    def __init__(self, prefix):
        super().__init__(prefix)
    
    def message__xxx(self):
        txt = ''
        self.add(txt)