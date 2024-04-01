"""
A dictionary of labels in form of {label: [latitude, longitude]}
"""

coordinates = {
    1: {
        'name': 'Stuaqpak Quick Stop',
        'location': [71.292266, -156.785431],
    },
    2: {
        'name': 'Alaska Commercial Company',
        'location': [71.286998, -156.798909],
    },
    3: {
        'name': 'Stuaqpak',
        'location': [71.298905, -156.755679],
    },
    4: {
        'name': "Kannika's Market",
        'location': [71.299297, -156.753426],
    },
}


if __name__ == "__main__":
    print(len(coordinates))