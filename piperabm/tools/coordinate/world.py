import matplotlib.pyplot as plt
import numpy as np


def plot_3d_earth(latitudes, longitudes, title="Earth"):
    scale = 6378137  # Earth's radius in meters

    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')

    # Convert latitude and longitude to 3D coordinates
    x = np.cos(np.radians(latitudes)) * np.cos(np.radians(longitudes))
    y = np.cos(np.radians(latitudes)) * np.sin(np.radians(longitudes))
    z = np.sin(np.radians(latitudes))

    # Scale for the globe (radius)
    x, y, z = x * scale, y * scale, z * scale

    # Plot the points
    ax.scatter(x, y, z, color='red', s=100)

    # Create a wireframe for the globe
    u = np.linspace(0, 2 * np.pi, 360)
    v = np.linspace(0, np.pi, 360)
    wx = scale * np.outer(np.cos(u), np.sin(v))
    wy = scale * np.outer(np.sin(u), np.sin(v))
    wz = scale * np.outer(np.ones(np.size(u)), np.cos(v))

    ax.plot_wireframe(wx, wy, wz, color='blue', rstride=10, cstride=10, alpha=0.1)
    ax.plot_surface(wx, wy, wz, color='blue', rstride=10, cstride=10, alpha=0.1)

    # Set scaling
    max_range = scale * 1.05
    ax.set_xlim(-max_range, max_range)
    ax.set_ylim(-max_range, max_range)
    ax.set_zlim(-max_range, max_range)

    # Hide axis values
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    ax.grid(False)

    # Hide the panes
    ax._axis3don = False
    ax.set_title(title)

    plt.show()

# Example usage
latitudes = [0, 20, 40]  # Replace with your latitude data
longitudes = [0, 30, 60]  # Replace with your longitude data
plot_3d_earth(latitudes, longitudes)
