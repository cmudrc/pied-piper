from piperabm.boundary.circular import Circular
from piperabm.boundary.point import Point


def load_boundary(dictionary: dict):
    boundary_dict = dictionary['boundary']
    if boundary_dict['type'] == 'point':
        boundary = Point()          
    elif boundary_dict['type'] == 'circular':
        boundary = Circular()
    boundary.from_dict(boundary_dict)
    return boundary