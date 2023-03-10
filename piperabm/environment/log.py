from piperabm.log import Log


class Log(Log):
    
    def __init__(self):
        super().__init__()
    
    def message__link_initiated(self):
        txt = ''
        self.add(txt)

    def message__link_degraded(self, start_node, end_node):
        txt = ''
        txt += '> link ' + str(start_node) + '-' + \
        str(end_node) + ' degradaded.'
        self.add(txt)

    def message__node_initiated(self):
        txt = ''
        self.add(txt)

    def message__node_degraded(self, node_index, node_type, node_name=None, node_pos=None):
        txt = '>' + node_type + ' ' + 'node' + ' ' + str(node_index)
        if node_name is not None or node_pos is not None:
            # extra node info
            txt += '('
            if node_name is not None:
                txt += 'name: '
                txt += node_name
            if node_name is not None and node_pos is not None:
                txt += ', '
            if node_pos is not None:
                txt += 'pos: '
                txt += str(node_pos)
            txt += ')'
        txt += ' ' + 'degradaded.'
        self.add(txt)