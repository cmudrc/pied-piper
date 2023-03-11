from piperabm.log import Log, agent_info


class Log(Log):
    
    def __init__(self, prefix):
        super().__init__(prefix)
    
    def message__transaction(self):
        txt = ''
        return txt