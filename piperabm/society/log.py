from piperabm.log import Log


class Log(Log):
    
    def __init__(self, prefix):
        super().__init__(prefix)
    
    def message__agent_died(self, agent_index, agent_name='', agent_pos=None):
        txt = ''
        txt += agent_info(agent_index, agent_name, agent_pos)
        self.add(txt)


def agent_info(
        agent_index,
        agent_name='',
        agent_pos=None
    ):
    txt = 'agent' + ' ' + str(agent_index)
    if agent_name != '' or agent_pos is not None:
        # extra agent info
        txt +=  ' ' + '('
        if agent_name != '':
            txt += 'name: '
            txt += '"' + agent_name + '"'
        if agent_name != '' and agent_pos is not None:
            txt += ', '
        if agent_pos is not None:
            txt += 'pos: '
            txt += str(agent_pos)
        txt += ')'
    return txt


if __name__ == "__main__":
    kwargs = {
        "agent_index": 1,
        "agent_name": "Peter",
        "agent_pos": [0, 0]
    }
    txt = agent_info(**kwargs)
    print(txt)
