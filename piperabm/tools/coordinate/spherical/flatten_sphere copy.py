import numpy as np


class FlattenSphere:

    def __init__(self, phi_0, l_0, radius=1):
        self.phi_0 = phi_0
        self.l_0 = l_0
        self.R = radius
        self.preprocess()
        
    def preprocess(self):
        """
        Dynamic programming
        """
        self.sin_phi_0 = np.sin(self.phi_0)
        self.cos_phi_0 = np.cos(self.phi_0)

    def calcualte_alpha_theta(self, phi, l):
        """
        Calculate alpha and theta
        """
        delta_l = l - self.l_0
        cos_alpha = self.sin_phi_0 * np.sin(phi) + self.cos_phi_0 * np.cos(phi) * np.cos(delta_l)
        alpha = np.arccos(cos_alpha)
        cos_theta = self.sin_phi_0 * np.cos(alpha) + self.cos_phi_0 * np.sin(alpha) * np.sin(phi)
        theta = np.arccos(cos_theta)
        #print("alpha: ", rad_to_deg(alpha), ", theta: ", rad_to_deg(theta))
        return alpha, theta
    
    def calculate_x_y(self, alpha, theta):
        """
        Calculate x and y
        """
        length = self.R * alpha
        x = length * np.sin(theta)
        y = length * np.cos(theta)
        #print("length: ", length)
        return x, y

    def convert(self, phi, l):
        """
        Convert spherical coordinate into cartesian coordinate
        """
        alpha, theta = self.calcualte_alpha_theta(phi, l)
        x, y = self.calculate_x_y(alpha, theta)
        return x, y
    

def deg_to_rad(deg):
    return (np.pi / 180) * deg
    

def rad_to_deg(rad):
    return (180 / np.pi) * rad


if __name__ == "__main__":
    '''
    phi_0 = deg_to_rad(70)
    l_0 = deg_to_rad(150)
    radius = 6400
    flatten_sphere = FlattenSphere(phi_0, l_0, radius)
    phi = deg_to_rad(70)
    l = deg_to_rad(151)
    x, y = flatten_sphere.convert(phi, l)
    print("x: ", x, ", y: ", y)
    '''
    '''
    phi_0 = deg_to_rad(71.287916)
    l_0 = deg_to_rad(-156.799801)
    radius = 6400
    flatten_sphere = FlattenSphere(phi_0, l_0, radius)
    phi = deg_to_rad(71.287925)
    l = deg_to_rad(-156.786445)
    x, y = flatten_sphere.convert(phi, l)
    print("x: ", x, ", y: ", y)
    '''
    phi_0 = deg_to_rad(71.297671)
    l_0 = deg_to_rad(-156.767303)
    radius = 6400
    flatten_sphere = FlattenSphere(phi_0, l_0, radius)
    phi = deg_to_rad(71.303646)
    l = deg_to_rad(-156.729171)
    x, y = flatten_sphere.convert(phi, l)
    print("x: ", x, ", y: ", y)
