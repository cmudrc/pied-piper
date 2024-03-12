name = 'utqiavik_uptown'

# Boundary
point_1_latitude, point_1_longitude = 71.322109, -156.688674
point_2_latitude, point_2_longitude = 71.333940, -156.665691

latitude_min = min([point_1_latitude, point_2_latitude])
latitude_max = max([point_1_latitude, point_2_latitude])
longitude_min = min([point_1_longitude, point_2_longitude])
longitude_max = max([point_1_longitude, point_2_longitude])

settlements_num = 10

proximity_radius = 3
