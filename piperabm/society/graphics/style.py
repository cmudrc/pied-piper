from piperabm.model.graphics.style import *


node_radius = DEFAULT_NODE_RADIUS * 2
font_size = DEFAULT_FONT_SIZE + 2

#FONT_SIZE = 8
#NODE_ITEM_DEFAULT_RADIUS = 5


society_node_style = {
    "agent": {
        "color": {
            "dead": "r",
            "alive": "magenta",
        },
        #"shape": "x",
        "size": node_radius,
    }
}

society_edge_style = {
    "family": {
        "color": "b",
    },
    "neighbor": {
        "color": "b",
    },
    "friend": {
        "color": "b",
    },
}

society_style = {
    "font": font_size,
    "node": society_node_style,
    "edge": society_edge_style,
}


if __name__ == "__main__":
    print(society_style)