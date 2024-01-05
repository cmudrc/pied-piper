def point_to_line_segment_vector(point, line):
    x = point[0]
    y = point[1]
    pos_1 = line[0]
    x1 = pos_1[0]
    y1 = pos_1[1]
    pos_2 = line[1]
    x2 = pos_2[0]
    y2 = pos_2[1]

    A = x - x1
    B = y - y1
    C = x2 - x1
    D = y2 - y1

    dot = A * C + B * D
    len_sq = C * C + D * D
    param = -1
    if len_sq != 0:  # in case of 0 length line
        param = dot / len_sq

    if param < 0:
        xx = x1
        yy = y1
    elif param > 1:
        xx = x2
        yy = y2
    else:
        xx = x1 + param * C
        yy = y1 + param * D

    dx = xx - x
    dy = yy - y
    return [dx, dy] # vector from point to line


if __name__ == "__main__":
    point = [0, 2]
    line = [[1, 1], [2, 1]]
    vector = point_to_line_segment_vector(point, line)
    print(vector)
