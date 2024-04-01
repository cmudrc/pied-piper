from piperabm.tools.geometry import Triangle, Patch
from piperabm.data.utqiavik.homes.generated_data.read import read_triangles_data


def generate_homes(
        homes_num: int = 1,
        latitude_0: float = 0,
        longitude_0: float = 0,
        permitted_labels = 'all'
    ):
    patch = Patch()
    triangles = read_triangles_data(latitude_0, longitude_0, permitted_labels)
    for triangle in triangles:
        point_1 = triangle[0]
        point_2 = triangle[1]
        point_3 = triangle[2]
        patch.add(Triangle(point_1, point_2, point_3))
    points = []
    for _ in range(homes_num):
        points.append(patch.random_point())
    return points


if __name__ == "__main__":

    import matplotlib.pyplot as plt

    from piperabm.data.utqiavik.info import location, homes_num
    from piperabm.data.utqiavik.homes.generated_data.generate import generate_homes

    points = generate_homes(
        homes_num=homes_num,
        latitude_0=location['latitude'],
        longitude_0=location['longitude']
    )
    
    xs = []
    ys = []
    for point in points:
        xs.append(point[0])
        ys.append(point[1])
    plt.scatter(xs, ys)  # Plot points
    plt.show()
    