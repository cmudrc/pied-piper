name = 'utqiavik_downtown'

# Boundary
point_1_latitude, point_1_longitude = 71.293255, -156.776608
point_2_latitude, point_2_longitude = 71.308299, -156.713090

latitude_min = min([point_1_latitude, point_2_latitude])
latitude_max = max([point_1_latitude, point_2_latitude])
longitude_min = min([point_1_longitude, point_2_longitude])
longitude_max = max([point_1_longitude, point_2_longitude])

settlements_num = 100

proximity_radius = 5
