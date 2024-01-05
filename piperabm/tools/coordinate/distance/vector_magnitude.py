from piperabm.tools.coordinate.distance import point_to_point


def vector_magnitude(vector):
    return point_to_point(vector, [0, 0])


if __name__ == "__main__":
    vector = [3, 4]
    magnitude = vector_magnitude(vector)
    print(magnitude)
    