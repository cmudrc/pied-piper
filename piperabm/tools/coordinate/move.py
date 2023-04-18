from piperabm.tools.coordinate.inverse_function import inverse_function


"""
move point in coordinate system based on the vector
return new pos
"""
def move(
        pos: list=[0,0],
        vector: list=[0, 0],
        inverse: bool=False
    ) -> list:
    inverse_factor = inverse_function(inverse)
    new_x = pos[0] + vector[0]
    new_x *= inverse_factor
    new_y = pos[1] + vector[1]
    new_y *= inverse_factor
    result = [new_x, new_y]
    return result

def move_coordinate(pos, vector) -> list:
    return move(pos, vector, inverse=True)

def move_point(pos, vector) -> list:
    return move(pos, vector, inverse=False)


if __name__ == "__main__":
    pos = [0, 0]
    vector = [-10, -10]
    new_pos = move_coordinate(pos, vector)
    print(new_pos)