# Infrastructure
NODE_ITEM_DEFAULT_RADIUS = 25
infrastructure_node_style = {
    "settlement": {
        "color": "b",    
    "radius": NODE_ITEM_DEFAULT_RADIUS,
    },
    "junction": {
        "color": "k",
        "radius": 5,
    },
    "market": {
        "color": "g",
        "radius": NODE_ITEM_DEFAULT_RADIUS,
    }
}
infrastructure_edge_style = {
    "road": {
        "color": "k",
    },
}

# Society
society_node_style = {
    "agent": {
        "color": {
            "dead": "r",
            "alive": "magenta",
        },
        "shape": "x",
        "size": NODE_ITEM_DEFAULT_RADIUS,
    }
}
society_edge_style = {}


style = {
    "infrastructure": {
        "node": infrastructure_node_style,
        "edge": infrastructure_edge_style,
    },
    "society": {
        "node": society_node_style,
        "edge": society_edge_style,
    },
}
