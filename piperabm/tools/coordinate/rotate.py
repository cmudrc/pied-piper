import numpy as np


class rotate:

    @staticmethod
    def x(
        vector,
        angle,
        unit: str = 'degree',
        rotate: str = 'axis',
        ndarray: bool = True
    ):
        """
        Rotate a 3D vector around the x-axis by a given angle in degrees.
        
        :param vector: A numpy array or list representing a 2D or 3D vector.
        :param angle: The angle of rotation.
        :param unit: The unit of angle, values: 'degree', 'radian'.
        :param rotate: The way the rotation is applied, values: 'axis', 'vector'.
        :param ndarray: The output format is ndarray or list.
        :return: Rotated vector.
        """
        result = None

        vector, angle_radians, factor = preprocess(vector, angle, unit, rotate)

        # Rotation matrix around x-axis
        rotation_matrix = np.array([
            [1, 0, 0],
            [0, np.cos(angle_radians), factor * np.sin(angle_radians)],
            [0, -1 * factor * np.sin(angle_radians), np.cos(angle_radians)]
        ])
        result = np.dot(rotation_matrix, vector)
        
        if ndarray is False:
            result = [float(num) for num in result]  # Convert np.float64 to float explicitly

        return result
    

    @staticmethod
    def y(
        vector,
        angle,
        unit: str = 'degree',
        rotate: str = 'axis',
        ndarray: bool = True
    ):
        """
        Rotate a 3D vector around the y-axis by a given angle in degrees.
        
        :param vector: A numpy array or list representing a 2D or 3D vector.
        :param angle: The angle of rotation.
        :param unit: The unit of angle, values: 'degree', 'radian'.
        :param rotate: The way the rotation is applied, values: 'axis', 'vector'.
        :param ndarray: The output format is ndarray or list.
        :return: Rotated vector.
        """
        result = None

        vector, angle_radians, factor = preprocess(vector, angle, unit, rotate)

        # Rotation matrix around y-axis
        rotation_matrix = np.array([
            [np.cos(angle_radians), 0, -1 * factor * np.sin(angle_radians)],
            [0, 1, 0],
            [factor * np.sin(angle_radians), 0, np.cos(angle_radians)]
        ])
        result = np.dot(rotation_matrix, vector)
        
        if ndarray is False:
            result = [float(num) for num in result]  # Convert np.float64 to float explicitly
            
        return result


    @staticmethod
    def z(
        vector,
        angle,
        unit: str = 'degree',
        rotate: str = 'axis',
        ndarray: bool = True
    ):
        """
        Rotate a 3D vector around the z-axis by a given angle in degrees.
        
        :param vector: A numpy array or list representing a 2D or 3D vector.
        :param angle: The angle of rotation.
        :param unit: The unit of angle, values: 'degree', 'radian'.
        :param rotate: The way the rotation is applied, values: 'axis', 'vector'.
        :param ndarray: The output format is ndarray or list.
        :return: Rotated vector.
        """
        result = None

        vector, angle_radians, factor = preprocess(vector, angle, unit, rotate)

        # Rotation matrix around z-axis
        rotation_matrix = np.array([
            [np.cos(angle_radians), factor * np.sin(angle_radians), 0],
            [-1 * factor * np.sin(angle_radians), np.cos(angle_radians), 0],
            [0, 0, 1]
        ])
        result = np.dot(rotation_matrix, vector)
        
        if ndarray is False:
            result = [float(num) for num in result]  # Convert np.float64 to float explicitly
            
        return result


def preprocess(vector, angle, unit='degree', rotate='axis'):
    
    vector = np.array(vector)
    
    while len(vector) < 3:
        vector = np.append(vector, 0)

    if rotate == 'axis':
        factor = 1
    elif rotate == 'vector':
        factor = -1

    if unit == 'radian':
        angle_radians = angle
    elif unit == 'degree':
        angle_radians = np.radians(angle)

    return vector, angle_radians, factor


if __name__ == "__main__":
    vector = np.array([0, 1, 0])
    angle = 45
    rotated_vector = rotate.x(vector, angle, unit='degree', rotate='axis')

    print(f'Original Vector: {vector}')
    print(f'Rotated Vector: {rotated_vector}')