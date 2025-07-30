In this example, we demonstrate how to work with satellite data and maps to create model.

# Running the Example

To run this example, execute the [`main.py`](https://github.com/cmudrc/pied-piper/blob/main/examples/satellite-map/main.py) file.

# Understanding the Steps:

This example follows the materials already covered in [Working with Satellite Data](https://pied-piper.readthedocs.io/latest/satellite.html).

![Map](https://github.com/cmudrc/pied-piper/blob/main/examples/satellite-map/parker,pa-map.png?raw=true)  
*Map of the Parker, PA.*

### [`points.py`](https://github.com/cmudrc/pied-piper/blob/main/examples/satellite-map/points.py)

This file contains latitude and longitude of the points that are labeled in the figure below:

![Labeled Points on the Map](https://github.com/cmudrc/pied-piper/blob/main/examples/satellite-map/parker,pa-points.png?raw=true)  
*Points of labeled on the map*

These points are used for both loading the streets and meshing the residential areas to randomly generate home nodes.

### [`streets.py`](https://github.com/cmudrc/pied-piper/blob/main/examples/satellite-map/streets.py)

This file contains a list of lists. Each element of this list is the label of points that create one street.

### [`mesh.py`](https://github.com/cmudrc/pied-piper/blob/main/examples/satellite-map/mesh.py)

This file contains a list of triangles that cover the residential areas of the city with meshes. Each triangle has a corresponding density. For example, the triangle 6 has a lower density of homes so the density value for this triangle is lower than the rest.

![Meshed Residential Areas](https://github.com/cmudrc/pied-piper/blob/main/examples/satellite-map/parker,pa-mesh.png?raw=true)  
*Meshes covering the residential areas on the map*

## Putting Them Together

As it has been descussed earlier, [Mercator Projection](https://pied-piper.readthedocs.io/latest/satellite.html#mercator-projection) is used when needing to convert latitude and longitude to x, y coordiantes. First, we need to find the reference point, which is in this case, the coodinates of the city. Then, using that reference point and Mercator formula, all we convert all the points to x, y coordinates.

After that, we generate random locations for homes that are in the residential areas using the methods covered in [Meshing Residential Areas](https://pied-piper.readthedocs.io/latest/satellite.html#meshing-residential-areas).

![Model of the City](https://github.com/cmudrc/pied-piper/blob/main/examples/satellite-map/parker,pa-model.png?raw=true)  
*Final model of the city*