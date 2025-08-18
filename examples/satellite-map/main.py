import piperabm as pa
from piperabm.tools.coordinate.projection import latlong_xy
from piperabm.tools.mesh import Triangle, Patch
from points import points
from streets import streets
from mesh import triangles, densities

# Source: https://en.wikipedia.org/wiki/Parker,_Pennsylvania
latitude_0 = 41.094167
longitude_0 = -79.682778
homes_num = 300

model = pa.Model(seed=2)

# Convert points to XY coordinates
points_xy = {}
for id in points:
    point = points[id]
    point_xy = latlong_xy(
        latitude_0, longitude_0, latitude=point[0], longitude=point[1]
    )
    points_xy[id] = point_xy

# Add streets to the model
for street in streets:
    for i in range(len(street) - 1):
        point_1 = points_xy[street[i]]
        point_2 = points_xy[street[i + 1]]
        model.infrastructure.add_street(pos_1=point_1, pos_2=point_2)

# Add homes to the model
patch = Patch()
for id in triangles:
    triangle = triangles[id]
    point_1 = points_xy[triangle[0]]
    point_2 = points_xy[triangle[1]]
    point_3 = points_xy[triangle[2]]
    density = densities[id]
    patch.add(Triangle(point_1, point_2, point_3, density))
for _ in range(homes_num):
    point = patch.random_point()
    model.infrastructure.add_home(pos=point)

model.bake()
model.infrastructure.show()
