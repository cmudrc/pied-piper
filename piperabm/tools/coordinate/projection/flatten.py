import numpy as np


class Flatten:

    def __init__(self, latitude_0=0, longitude_0=0, radius=1):
        self.latitude_0 = latitude_0
        self.longitude_0 = longitude_0
        self.radius = radius
        self.preprocess()
        
    def preprocess(self):
        """
        Dynamic programming
        """
        self.sin_latitude_0 = np.sin(self.latitude_0)
        self.cos_latitude_0 = np.cos(self.latitude_0)

    def calcualte_alpha_theta(self, latitude=0, longitude=0):
        """
        Calculate alpha and theta
        """
        delta_longitude = longitude - self.longitude_0
        cos_latitude = np.cos(latitude)

        # Calcualte alpha:
        cos_alpha = self.sin_latitude_0 * np.sin(latitude) + self.cos_latitude_0 * cos_latitude * np.cos(delta_longitude)
        alpha = np.arccos(cos_alpha)

        # Calculate theta:
        if alpha == 0:
            theta = 0
        else:
            sin_theta = cos_latitude * np.sin(delta_longitude) / np.sin(alpha)
            if sin_theta > 1:
                sin_theta = 1
            theta = np.arcsin(sin_theta)
            
        return alpha, theta
    
    def calculate_latitude_longitude_prime(self, alpha, theta):
        """
        Calculate new latitude and longitude based on new pole and equator
        """
        sin_latitude_prime = np.sin(alpha) * np.cos(theta)
        latitude_prime = np.arcsin(sin_latitude_prime)
        cos_longitude_prime = np.cos(alpha) / np.cos(latitude_prime)
        longitude_prime = np.arccos(cos_longitude_prime)
        return latitude_prime, longitude_prime

    def mercator_projection(self, latitude, longitude):
        """
        Project using Mercator formula to cartesian coordinates
        """
        x = self.radius * longitude
        y = self.radius * np.log(np.tan(np.pi / 4 + latitude / 2))
        return x, y

    def convert(self, latitude=0, longitude=0):
        """
        Convert spherical coordinate into cartesian coordinate
        """
        alpha, theta = self.calcualte_alpha_theta(latitude, longitude)
        latitude_prime, longitude_prime = self.calculate_latitude_longitude_prime(alpha, theta)
        x, y = self.mercator_projection(latitude_prime, longitude_prime)
        return x, y
    

def deg_to_rad(deg):
    return (np.pi / 180) * deg
    

def rad_to_deg(rad):
    return (180 / np.pi) * rad


if __name__ == "__main__":
    #latitude_0 = deg_to_rad(71.297671)
    #longitude_0 = deg_to_rad(-156.767303)
    latitude_0 = deg_to_rad(45)
    longitude_0 = deg_to_rad(0)
    radius = 6378000
    projection = Flatten(latitude_0, longitude_0, radius)

    #latitude = deg_to_rad(71.303646)
    #longitude = deg_to_rad(-156.729171)
    latitude = deg_to_rad(45)
    longitude = deg_to_rad(0)
    alpha, theta = projection.calcualte_alpha_theta(latitude, longitude)
    print("alpha: ", rad_to_deg(alpha), ", theta: ", rad_to_deg(theta))
    latitude_prime, longitude_prime = projection.calculate_latitude_longitude_prime(alpha, theta)
    print("latitude_prime: ", rad_to_deg(latitude_prime), ", longitude_prime: ", rad_to_deg(longitude_prime))
    x, y = projection.convert(latitude, longitude)
    print(x, y)
