from piperabm.log import Log, node_info, edge_info


class Log(Log):
    
    def __init__(self, prefix, indentation_depth):
        super().__init__(prefix, indentation_depth)
    
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
        txt = 'INITIATED: '
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
        txt = 'DEGRADED: '
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
        self.add(txt)

    def message__node_initiated(self, node_index, node_type, node_name='', node_pos=None):
        txt = 'INITIATED: '
        txt += node_info(node_index, node_type, node_name, node_pos)
        self.add(txt)

    def message__node_degraded(self, node_index, node_type, node_name='', node_pos=None):
        txt = 'DEGRADED: '
        txt += node_info(node_index, node_type, node_name, node_pos)
        self.add(txt)
