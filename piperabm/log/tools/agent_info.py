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