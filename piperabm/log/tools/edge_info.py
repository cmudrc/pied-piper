try: from .node_info import node_info
except: from node_info import node_info


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