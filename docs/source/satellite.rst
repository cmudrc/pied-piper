Working with Satellite Data
========================

PiperABM can seamlessly ingest satellite imagery and geospatial datasets to build simulation-ready infrastructure models. Below are guides to help you import, preprocess, and integrate satellite data into your modeling workflows.


Mercator Projection
--------------------------------
As we already saw in the Step 1 section, the PiperABM framework expects x, y coordinates for the positions.

.. code-block:: python

    from piperabm.tools.coordinate.projection import latlong_xy

    # Reference points
    latitude_0 = 40.0520
    longitude_0 = -74.0232

    # Points in latitude and longitude
    points = [
        [40.7128, -74.0060],
        [40.0522, -74.0240],
        [40.1234, -74.0567]
    ]

    # Convert to x, y coordinates using Mercator projection
    for point in points:
        x, y = latlong_xy(latitude_0, longitude_0, latitude=point[0], longitude=point[1])
        print(x, y)


Meshing Residential Areas
--------------------------------
To add home nodes to the model, we already see that we can use the `add_home` method of the `Infrastructure` class. However, it is not always practical to add hundreds or thausand of homes one by one.
When working with satellite data and maps, we can create mesh patches that represent and cover the residential areas. These patches are then used to generate random points that represent the homes in the model.

To do so, first, we define the points that form the vertices of the triangles. If the points are in latitude and longitude, convert them to x and y coordinates using the Mercator projection that has been discussed above.
Then, we create `Triangle` instances for each triangle formed by the points. Finally, we create a `Patch` instance that contains these triangles.
The `Patch` instance can then be used to generate random points within the defined area.
Another capability of the `Triangle` is that it can have a `density` atttribute, defaulting to 1, which controles chance of point generation in the area. This is useful since not all residential areas have the same density of homes.

.. code-block:: python
    
    import piperabm as pa
    from piperabm.tools.mesh import Triangle, Patch
    
    model = pa.Model()

    # First, we define the points that from the vertices of the triangle.
    point_1 = [0, 0]
    point_2 = [10, 0]
    point_3 = [10, 12]
    ...

    # Then, we create Triangle instances for each triangle formed by the points.
    triangle_1 = Triangle(point_1, point_23, point_8)
    triangle_2 = Triangle(point_3, point_43, point_5)
    triangle_3 = Triangle(point_6, point_52, ponint_27)
    ...

    # Finally, we create a Patch instance that containts these triangles.
    patch = Patch([
        triangle_1,
        triangle_2,
        triangle_3,
        ...
    ])

    # We can now generate random points within the defined area.
    for _ in range(100):  # Generate 100 random points within the patched area
        point = patch.random_point()
        model.infrastructure.add_home(pos=point, name='home')