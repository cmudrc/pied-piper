from piperabm.tools.geometry import Triangle, Patch
from piperabm.data.utqiavik.settlements.read_data import read_data


def generate_settlements(settlements_num, latitude_0, longitude_0, permitted_labels='all'):
    patch = Patch()
    triangles = read_data(latitude_0, longitude_0, permitted_labels)
    for triangle in triangles:
        point_1 = triangle[0]
        point_2 = triangle[1]
        point_3 = triangle[2]
        patch.add(Triangle(point_1, point_2, point_3))
    points = []
    for _ in range(settlements_num):
        points.append(patch.random_point())
    return points


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    latitude_0 = 0
    longitude_0 = 0
    points = generate_settlements(1500, latitude_0, longitude_0)

    xs = []
    ys = []
    for point in points:
        xs.append(point[0])
        ys.append(point[1])
    plt.scatter(xs, ys)  # Plot points
    plt.show()
    