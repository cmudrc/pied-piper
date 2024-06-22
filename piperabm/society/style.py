FONT_SIZE = 8

NODE_ITEM_DEFAULT_RADIUS = 5

society_node_style = {
    "agent": {
        "color": {
            "dead": "r",
            "alive": "magenta",
        },
        "shape": "x",
        "size": NODE_ITEM_DEFAULT_RADIUS * 1.5,
    }
}

society_edge_style = {}

society_style = {
    "font": FONT_SIZE,
    "node": society_node_style,
    "edge": society_edge_style,
}


if __name__ == "__main__":
    print(society_style)