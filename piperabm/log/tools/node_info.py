def node_info(
        node_index,
        node_type,
        node_name='',
        node_pos=None
    ):
    txt = node_type + ' ' + 'node' + ' ' + str(node_index)
    if node_name != '' or node_pos is not None:
        # extra node info
        txt +=  ' ' + '('
        if node_name != '':
            txt += 'name: '
            txt += '"' + node_name + '"'
        if node_name != '' and node_pos is not None:
            txt += ', '
        if node_pos is not None:
            txt += 'pos: '
            txt += str(node_pos)
        txt += ')'
    return txt


if __name__ == "__main__":
    kwargs = {
        "node_index": 1,
        "node_type": "settlement",
        "node_name": "John's House",
        "node_pos": [1, 1],
    }
    txt = node_info(**kwargs)
    print(txt)