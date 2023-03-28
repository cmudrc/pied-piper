from piperabm.log import Log, agent_info


class Log(Log):
    
    def __init__(self, prefix, indentation_depth):
        super().__init__(prefix, indentation_depth)
    
    def message__agent_died(self, agent_index, agent_name='', agent_pos=None, death_reason=None):
        txt = 'DIED' + ':' + ' '
        txt += agent_info(agent_index, agent_name, agent_pos)
        if death_reason is not None:
            txt += ' ' + '('
            txt += 'reason'
            txt += ':' + ' '
            txt += death_reason
            txt += ')'
        self.add(txt)
        return txt

    def message__agent_decided(self, route, agent_index, agent_name, agent_pos):
        txt = 'DECIDED' + ':' + ' '
        txt += agent_info(agent_index, agent_name, agent_pos)
        txt += ' ' + 'will go from' + ' '
        txt += str(route[0])
        txt += ' ' + 'to' + ' '
        txt += str(route[1])
        self.add(txt)
        return txt
    
    def message__agent_reached(self, route, agent_index, agent_name, agent_pos):
        txt = 'REACHED' + ':' + ' '
        txt += agent_info(agent_index, agent_name, agent_pos)
        txt += ' ' + 'came from' + ' '
        txt += str(route[0])
        txt += ' ' + 'and reached to' + ' '
        txt += str(route[1])
        self.add(txt)
        return txt