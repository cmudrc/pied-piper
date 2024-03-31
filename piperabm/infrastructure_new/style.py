FONT_SIZE = 8

NODE_ITEM_DEFAULT_RADIUS = 5

infrastructure_node_style = {
    "home": {
        "color": "b",    
    "radius": NODE_ITEM_DEFAULT_RADIUS,
    },
    "junction": {
        "color": "k",
        "radius": 0,
    },
    "market": {
        "color": "g",
        "radius": NODE_ITEM_DEFAULT_RADIUS,
    }
}

infrastructure_edge_style = {
    "street": {
        "color": "k",
    },
    "neighborhood_access": {
        "color": "g",
    },
}

infrastructure_style = {
    "font": FONT_SIZE,
    "node": infrastructure_node_style,
    "edge": infrastructure_edge_style,
}