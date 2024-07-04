from piperabm.tools.fit_3d import Fit3D
from piperabm.tools.coordinate.projection import latlong_xy


class ClimateImpact(Fit3D):

    def __init__(self, coeff: float = 1):
        self.coeff = coeff
        super().__init__()
    
    def add_xy(
            self,
            x: float,
            y: float,
            temperature: float
        ) -> None:
        """
        Add new data point by x and y coordiante
        """
        self.add(x=x, y=y, z=temperature)
    
    def add_latlong(
            self,
            latitude: float,
            longitude: float,
            temperature: float,
            latitude_0: float,
            longitude_0: float
        ) -> None:
        """
        Add new data point by latitude and longitude coordiante
        """
        x, y = latlong_xy(
            latitude_0=latitude_0,
            longitude_0=longitude_0,
            latitude=latitude,
            longitude=longitude
        )
        self.add_xy(x=x, y=y, temperature=temperature)

    def temperature(self, x: float, y: float):
        """
        Interpolate temperature
        """
        return self.z(x=x, y=y)
    
    def impact(self, x: float, y: float):
        """
        Interpolate climate impact
        """
        return self.temperature(x=x, y=y) * self.coeff
    

if __name__ == "__main__":
    cliamte_impact = ClimateImpact(coeff=0.01)
    cliamte_impact.add_xy(x=10, y=0, temperature=10)
    cliamte_impact.add_xy(x=-10, y=0, temperature=-10)
    cliamte_impact.add_xy(x=0, y=10, temperature=5)
    cliamte_impact.add_xy(x=0, y=-10, temperature=0)
    print(cliamte_impact.impact(x=10, y=10))