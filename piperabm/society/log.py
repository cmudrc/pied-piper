from piperabm.log import Log


class Log(Log):
    
    def __init__(self, prefix):
        super().__init__(prefix)
    
    def message__agent_died(self, agent_index, agent_name='', agent_pos=None):
        txt = ''
        
        self.add(txt)