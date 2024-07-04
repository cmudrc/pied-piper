from scipy.interpolate import griddata
from scipy.interpolate import LinearNDInterpolator
from scipy.interpolate import NearestNDInterpolator
from scipy.interpolate import RBFInterpolator


class Fit3D:
    """
    Interpolate 3d data
    """

    def __init__(self):
        self.xs = []
        self.ys = []
        self.zs = []

    def add(self, x: float, y: float, z: float):
        """
        Add new data point
        """
        self.xs.append(x)
        self.ys.append(y)
        self.zs.append(z)

    @property
    def len(self):
        """
        Number of data points
        """
        return len(self.zs)
    
    @property
    def points(self):
        """
        Prepare data for interpolation
        """
        return list(zip(self.xs, self.ys))

    def z(
            self,
            x: float,
            y: float,
            method: str = 'RBFInterpolator'
        ):
        """
        Return interpolated value
        """
        if self.len == 0:
            result = 0
        else:
            if method == 'griddata':
                result = griddata(
                    points=(self.xs, self.ys),
                    values=self.zs,
                    xi=(x, y),
                    method='cubic'
                )
            elif method == 'LinearNDInterpolator':
                interpolator = LinearNDInterpolator(self.points, self.zs)
                result = interpolator(x, y)
            elif method == 'NearestNDInterpolator':
                interpolator = NearestNDInterpolator(self.points, self.zs)
                result = interpolator(x, y)
            elif method == 'RBFInterpolator':
                rbf = RBFInterpolator(self.points, self.zs, kernel='cubic')
                return rbf([(x, y)])[0]
        return result
    
    def serialize(self):
        """
        Serialize
        """
        return {
            'xs': self.xs,
            'ys': self.ys,
            'zs': self.zs
        }
    
    def deserialize(self, dictionary: dict):
        """
        Deserialize
        """
        self.xs = dictionary['xs']
        self.ys = dictionary['ys']
        self.zs = dictionary['zs']


if __name__ == "__main__":
    interpolate = Fit3D()
    interpolate.add(x=10, y=0, z=10)
    interpolate.add(x=-10, y=0, z=-10)
    interpolate.add(x=0, y=10, z=5)
    interpolate.add(x=0, y=-10, z=-5)
    print("griddata: ", interpolate.z(x=0, y=0, method='griddata'))
    print("LinearNDInterpolator: ", interpolate.z(x=0, y=0, method='LinearNDInterpolator'))
    print("NearestNDInterpolator: ", interpolate.z(x=0, y=0, method='NearestNDInterpolator'))
    print("RBFInterpolator: ", interpolate.z(x=0, y=0, method='RBFInterpolator'))