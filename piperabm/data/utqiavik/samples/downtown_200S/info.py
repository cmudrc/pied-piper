name = 'utqiavik_downtown'

# Boundary
point_1_latitude, point_1_longitude = 71.293255, -156.776608
point_2_latitude, point_2_longitude = 71.324514, -156.674813

latitude_min = min([point_1_latitude, point_2_latitude])
latitude_max = max([point_1_latitude, point_2_latitude])
longitude_min = min([point_1_longitude, point_2_longitude])
longitude_max = max([point_1_longitude, point_2_longitude])

settlements_num = 200

proximity_radius = 3
