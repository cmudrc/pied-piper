"""
Lists containing mesh labels in each map
"""
try:
    from .coordinates import coordinates
    from .meshes import meshes
except:
    from coordinates import coordinates
    from meshes import meshes

map_1 = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
    31,
    32,
]

map_2 = [
    33,
]

map_3 = [
]

map_4 = [
    34,
    35,
    36,
    37,
    38,
    39,
    40,
    41,
    42,
    43,
    44,
    45,
    46,
    47,
    48,
    49,
    50,
    51,
    52,
    53,
    54,
    55,
]

map_5 = [
    56,
    57,
]

def filter_labels(
        latitude_min,
        latitude_max,
        longitude_min,
        longitude_max
    ):
    permitted_labels = []
    permitted_coordinate_labels = []
    for id in coordinates:
        coordinate = coordinates[id]
        latitude = coordinate[0]
        longitude = coordinate[1]
        if latitude >= latitude_min and \
        latitude <= latitude_max and \
        longitude >= longitude_min and \
        longitude <= longitude_max:
            permitted_coordinate_labels.append(id)
    for id in meshes:
        mesh = meshes[id]
        if mesh[0] in permitted_coordinate_labels and \
        mesh[1] in permitted_coordinate_labels and \
        mesh[2] in permitted_coordinate_labels:
            permitted_labels.append(id)
    return permitted_labels