from piperabm.log import Log, agent_info


class Log(Log):
    
    def __init__(self, prefix):
        super().__init__(prefix)
    
    def message__agent_died(self, agent_index, agent_name='', agent_pos=None):
        txt = ''
        txt += agent_info(agent_index, agent_name, agent_pos)
        self.add(txt)