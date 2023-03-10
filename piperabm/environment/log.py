from piperabm.log import Log


class Log(Log):
    
    def __init__(self):
        super().__init__()
    
    def message__link_initiated(
            self,
            start_node_index,
            start_node_type,
            end_node_index,
            end_node_type,
            start_node_name='',
            start_node_pos=None,
            end_node_name='',
            end_node_pos=None
        ):
        txt = '>'
        txt += edge_info(
                start_node_index,
                start_node_type,
                end_node_index,
                end_node_type,
                start_node_name,
                start_node_pos,
                end_node_name,
                end_node_pos
            )
        txt += ' ' + 'initiated.'
        self.add(txt)

    def message__link_degraded(
            self,
            start_node_index,
            start_node_type,
            end_node_index,
            end_node_type,
            start_node_name='',
            start_node_pos=None,
            end_node_name='',
            end_node_pos=None
        ):
        txt = '>'
        txt += edge_info(
                start_node_index,
                start_node_type,
                end_node_index,
                end_node_type,
                start_node_name,
                start_node_pos,
                end_node_name,
                end_node_pos
            )
        txt += ' ' + 'degradaded.'
        self.add(txt)

    def message__node_initiated(self, node_index, node_type, node_name='', node_pos=None):
        txt = '- INITIATED: '
        txt += node_info(node_index, node_type, node_name, node_pos)
        self.add(txt)

    def message__node_degraded(self, node_index, node_type, node_name='', node_pos=None):
        txt = '- DEGRADED: '
        txt += node_info(node_index, node_type, node_name, node_pos)
        self.add(txt)
    

def node_info(
        node_index,
        node_type,
        node_name='',
        node_pos=None
    ):
    txt = node_type + ' ' + 'node' + ' ' + str(node_index) + ' '
    if node_name != '' or node_pos is not None:
        # extra node info
        txt += '('
        if node_name != '':
            txt += 'name: '
            txt += node_name
        if node_name != '' and node_pos is not None:
            txt += ', '
        if node_pos is not None:
            txt += 'pos: '
            txt += str(node_pos)
        txt += ')'
    return txt


def edge_info(
        start_node_index,
        start_node_type,
        end_node_index,
        end_node_type,
        start_node_name='',
        start_node_pos=None,
        end_node_name='',
        end_node_pos=None
    ):
    txt = 'link from' + ' '
    txt += node_info(
        node_index=start_node_index,
        node_type=start_node_type,
        node_name=start_node_name,
        node_pos=start_node_pos
    )
    txt += ' ' + 'to' + ' '
    txt += node_info(
        node_index=end_node_index,
        node_type=end_node_type,
        node_name=end_node_name,
        node_pos=end_node_pos
    )
    return txt


if __name__ == "__main__":
    kwargs = {
        "start_node_index": 1,
        "start_node_type": "settlement",
        "end_node_index": 2,
        "end_node_type": "settlement",
        "start_node_name": "John's House",
        "start_node_pos": [1, 1],
        "end_node_name": "Peter's House",
        "end_node_pos": [2, 2],
    }
    txt = edge_info(**kwargs)
    print(txt)