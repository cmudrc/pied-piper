from piperabm.model.graphics.style import *


node_radius = DEFAULT_NODE_RADIUS
font_size = DEFAULT_FONT_SIZE


infrastructure_node_style = {
    "home": {
        "color": "b",    
    "radius": node_radius,
    },
    "junction": {
        "color": "k",
        "radius": 0,
    },
    "market": {
        "color": "g",
        "radius": node_radius * 10,
    }
}

infrastructure_edge_style = {
    "street": {
        "color": "k",
    },
    "neighborhood_access": {
        "color": "silver",
    },
}

infrastructure_style = {
    "font": font_size,
    "node": infrastructure_node_style,
    "edge": infrastructure_edge_style,
}


if __name__ == "__main__":
    print(infrastructure_style)